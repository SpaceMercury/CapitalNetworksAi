import implicit
import pandas as pd
import scipy.sparse as sparse
import numpy as np
import random
from implicit.als import AlternatingLeastSquares
import glob

def dataClean(pathUsers):
    # Return: purchases_sparse
    # Get a list of all user transaction JSON files
    print(f"{pathUsers}")
    transaction_files = glob.glob(f'{pathUsers}/*.csv')
    print(transaction_files)

    # Load and concatenate all user transactions data
    df_transactions = pd.concat([pd.read_csv(file) for file in transaction_files], ignore_index=True)
    print(df_transactions.head())

    transaction_lookup = df_transactions[['CLIENT', 'Stockfeature_uuid', 'StockFeature_shortName', 'QTY']].drop_duplicates()

    cleaned_transactions = df_transactions[['CLIENT', 'StockFeature_uuid', 'QTY']].drop_duplicates()
    print(f"Client Head: \n {cleaned_transactions['CLIENT'].head()}")
    cleaned_transactions['CLIENT'] = cleaned_transactions['CLIENT'].astype(int)
    grouped_cleaned_transactions = cleaned_transactions.groupby(['CLIENT', 'StockFeature_uuid']).sum().reset_index()
    grouped_cleaned_transactions['QTY'] = np.where(grouped_cleaned_transactions['QTY'] > 0, 1, grouped_cleaned_transactions['QTY']) # TODO: This correct?!?!

    print(grouped_cleaned_transactions.head())
    
    customers = list(np.sort(grouped_cleaned_transactions.CLIENT.unique())) # Get our unique customers
    stocks = list(grouped_cleaned_transactions.StockFeature_uuid.unique()) # Get our unique products that were purchased
    quantity = list(grouped_cleaned_transactions.QTY) # All of our purchases
    rows = grouped_cleaned_transactions.CLIENT.astype('category').cat.codes # Get the associated row indices
    print(f"ROWS \n {rows.head()}")
    # TODO: Is this correct?

    # Get the associated column indices
    cols = grouped_cleaned_transactions.StockFeature_uuid.astype('category').cat.codes

    print(f"COLS \n {cols.head()}")

    purchases_sparse = sparse.csr_matrix((quantity, (rows, cols)), shape=(len(customers), len(stocks)))
    return purchases_sparse

def make_train(ratings, pct_test=0.2):
    # Return: training_set, test_set, user_inds
    # Create two copies of the ratings matrix, one for training and another for testing
    test_set = ratings.copy()
    test_set[test_set != 0] = 1
    training_set = ratings.copy()
    nonzero_inds = training_set.nonzero()
    nonzero_pairs = list(zip(nonzero_inds[0], nonzero_inds[1]))
    random.seed(0)
    num_samples = int(np.ceil(pct_test*len(nonzero_pairs)))
    samples = random.sample(nonzero_pairs, num_samples)
    user_inds = [index[0] for index in samples]
    item_inds = [index[1] for index in samples]
    training_set[user_inds, item_inds] = 0
    training_set.eliminate_zeros()

    return training_set, test_set, list(set(user_inds))

def recommendationOutput(product_train, alpha, userId):
    model = AlternatingLeastSquares(factors=100, regularization=0.01, alpha=2.0)
    model.fit(product_train)
    ids, scores = model.recommend(userId, product_train, N=10, filter_already_liked_items=False)
    #user_vecs, stock_vecs = implicit.alternating_least_squares((product_train * alpha).astype('double'), factors= 20, regularization = 0.1, iterations = 50)

    #user_vecs[0,:].dot(stock_vecs).toarray()[0,:5]
    return ids, scores

def recommenderSys(pathTrans, userId):
    print(f"{pathTrans}")
    purchases_sparse = dataClean(pathTrans)
    print(f"Purchase Sparce \n {purchases_sparse}")

    product_train, product_test, product_users_altered = make_train(purchases_sparse, pct_test = 0.2)
    ids, scores = recommendationOutput(product_train, alpha=0.1, userId=userId)
    return ids, scores

def main():
    pathTrans = f"data/users"
    userId = 1
    ids, scores = recommenderSys(pathTrans, userId)
    print(ids)
    print(scores)

if __name__ == "__main__":
    main()
