import implicit
import pandas as pd
import scipy.sparse as sparse
from sklearn.preprocessing import LabelEncoder
import numpy as np
from scipy.sparse.linalg import spsolve
import random

import glob

def dataClean(pathUsers):
    # Return: purchases_sparse
    # Get a list of all user transaction JSON files
    transaction_files = glob.glob(f'{pathUsers}/*.json')

    # Load and concatenate all user transactions data
    df_transactions = pd.concat([pd.read_json(file) for file in transaction_files], ignore_index=True)
    print(df_transactions.head())

    transaction_lookup = df_transactions[['CLIENT', 'StockFeature_uuid', 'StockFeature_name', 'Quantity']].drop_duplicates()

    cleaned_transactions = df_transactions[['CLIENT', 'StockFeature_uuid', 'Quantity']].drop_duplicates()
    cleaned_transactions['CLIENT'] = cleaned_transactions['CLIENT'].astype(int)
    grouped_cleaned_transactions = cleaned_transactions.groupby(['CLIENT', 'StockFeature_uuid']).sum().reset_index()
    grouped_cleaned_transactions['Quantity'] = np.where(grouped_cleaned_transactions['Quantity'] > 0, 1, grouped_cleaned_transactions['Quantity']) # TODO: This correct?!?!

    print(grouped_cleaned_transactions.head())
    
    customers = list(np.sort(grouped_cleaned_transactions.CLIENT.unique())) # Get our unique customers
    stocks = list(grouped_cleaned_transactions.StockFeature_uuid.unique()) # Get our unique products that were purchased
    quantity = list(grouped_cleaned_transactions.Quantity) # All of our purchases
    rows = grouped_cleaned_transactions.CLIENT.astype('category', categories = customers).cat.codes # Get the associated row indices
    # TODO: Is this correct?

    # Get the associated column indices
    cols = grouped_cleaned_transactions.StockFeature_uuid.astype('category', categories = stocks).cat.codes

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

def recommendationOutput(product_train, alpha):
    user_vecs, stock_vecs = implicit.alternating_least_squares((product_train * alpha).astype('double'), factors= 20, regularization = 0.1, iterations = 50)

    user_vecs[0,:].dot(stock_vecs).toarray()[0,:5]
    return user_vecs, stock_vecs

def recommenderSys(pathTrans):
    path = "data/output/user_transactions"
    purchases_sparse = dataClean(path)
    product_train, product_test, product_users_altered = make_train(purchases_sparse, pct_test = 0.2)
    user_vecs, stock_vecs = recommendationOutput(product_train, 15)
    return user_vecs, stock_vecs

def main():
    path = "data/output/user_transactions"
    purchases_sparse = dataClean(path)
    product_train, product_test, product_users_altered = make_train(purchases_sparse, pct_test = 0.2)
    user_vecs, stock_vecs = recommendationOutput(product_train, 15)




if __name__ == "__main__":
    main()
