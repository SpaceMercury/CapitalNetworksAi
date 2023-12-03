import implicit
import pandas as pd
import scipy.sparse as sparse
from sklearn.preprocessing import LabelEncoder
import numpy as np
from scipy.sparse.linalg import spsolve

import glob

def dataClean(pathUsers, pathStocks):
    # Get a list of all user transaction JSON files
    transaction_files = glob.glob(f'{pathUsers}/*.json')

    # Load and concatenate all user transactions data
    df_transactions = pd.concat([pd.read_json(file) for file in transaction_files], ignore_index=True)

    # Load stock information data
    df_stocks = pd.read_json(f'{pathStocks}/*.json')

    stock_lookup = df_stocks[['', 'item_name']]

    # Preprocess data
    user_encoder = LabelEncoder()
    item_encoder = LabelEncoder()
    df_transactions['user_id'] = user_encoder.fit_transform(df_transactions['user_id'])
    df_transactions['item_id'] = item_encoder.fit_transform(df_transactions['item_id'])

    # Create a sparse matrix
    user_item = sparse.coo_matrix((df_transactions['quantity'], (df_transactions['user_id'], df_transactions['item_id'])))

    return user_item

def modelFit(user_item):

    # Initialize the ALS model
    model = implicit.als.AlternatingLeastSquares(calculate_training_loss=True)

    # Train the model
    model.fit(user_item)

    return model

def recommendationOutput(model, user_item, user_id, item_encoder):
    # Now you can use the model to make recommendations
    recommendations = model.recommend(user_id, user_item, recalculate_user=True)

    # Print the recommendations
    for item_id, score in recommendations:
        print(f"Recommended item: {item_encoder.inverse_transform([item_id])[0]}, score: {score}")

def recommenderIter(path, user_id):
    user_item = genFit(path)
    model = modelFit(user_item)
    return recommendationOutput(model, user_item, user_id, item_encoder)

def main():
    path = "data/output/user_transactions"
    recommenderIter(path, user_id)

if __name__ == "__main__":
    main()
