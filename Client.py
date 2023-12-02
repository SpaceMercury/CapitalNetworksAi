import json
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import norm
import math
import statistics
import scipy.stats as st
import random
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.manifold import TSNE
import seaborn as sns
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Import the 3D plotting toolkit

class CLIENT:
    def __init__(self, name, transactions):
        self.name = name
        self.transactions = transactions

 
    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def print_user(self):
       print(self.name)
       #T-nse print 
       self.plot_t_sne()

        
        
    def plot_t_sne(self, perplexity=30, n_iter=1000):

        # Convert to DataFrame for easier processing
        df = pd.DataFrame(self.transactions)

        # Encoding non-numeric columns
        for col in df.select_dtypes(include=['object', 'category']):
            df[col] = LabelEncoder().fit_transform(df[col])


        # Standardize the data
        X = StandardScaler().fit_transform(df)


        # Create and fit the t-SNE model for 3 components (3D)
        tsne = TSNE(n_components=3, verbose=1, perplexity=perplexity, n_iter=n_iter)
        tsne_results = tsne.fit_transform(X)


        # Plot the results in 3D
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')  # Create a 3D subplot
        ax.scatter(tsne_results[:,0], tsne_results[:,1], tsne_results[:,2])
        ax.set_title("User: " + self.name )
        ax.set_xlabel("t-SNE 1")
        ax.set_ylabel("t-SNE 2")
        ax.set_zlabel("t-SNE 3")
        plt.show()




def bagOfFeature(list_of_vectors):
    bagOfFeature = {}
    for vec in list_of_vectors:
        for i in range(1, len(vec)):
            if df.columns[i] not in bagOfFeature:
                bagOfFeature[df.columns[i]] = []
            if vec[i] not in bagOfFeature[df.columns[i]]:
                bagOfFeature[df.columns[i]].append(vec[i])
    return 

def list_of_features(list_of_vectors):
    list_of_features = []
    for fea in list_of_vectors[0]:
        list_of_features.append(fea)
    return list_of_features

       
    
# Create a list of vectors from the data with the capture of the features like in the dataset
def create_list_of_vectors(df):
    list_of_vectors = []
    for _, row in df.iterrows():
        # Create a vector with column names as keys and row values as values
        vector = {col: row[col] for col in df.columns}
        # Add the dictionary (vector) to the list
        list_of_vectors.append(vector)
    return list_of_vectors





from sklearn.preprocessing import OneHotEncoder


# Assuming these encoders are fitted on the entire dataset beforehand
# You might need to adjust this part depending on your exact dataset and requirements
one_hot_encoder = OneHotEncoder()
def one_hot_encode(df):
    for feature in df.select_dtypes(include=['object', 'category']):
        df[feature] = df[feature].astype('category')
    one_hot_encoder.fit(df[['STOCK_LIBELLE', 'CURRENCY', 'ACTION_TYPE']])
    return df

def transaction_to_vector(transaction):
    # Create a vector with column names as keys and row values as values
    vector = {col: transaction[col] for col in df.columns}
    # Encode the categorical columns
    vector['STOCK_LIBELLE'] = one_hot_encoder.transform([[vector['STOCK_LIBELLE']]]).toarray()[0]
    vector['CURRENCY'] = one_hot_encoder.transform([[vector['CURRENCY']]]).toarray()[0]
    vector['ACTION_TYPE'] = one_hot_encoder.transform([[vector['ACTION_TYPE']]]).toarray()[0]
    return vector



# Print the list of vectors, only first 10 vectors using a DataFrame
def print_list_of_vectors(list_of_vectors):
    df = pd.DataFrame(list_of_vectors)
    print(df.head(5))
    



def plot_t_sne(list_of_vectors, perplexity=30, n_iter=1000):

    # Convert to DataFrame for easier processing
    df = pd.DataFrame(list_of_vectors)

    # Encoding non-numeric columns
    for col in df.select_dtypes(include=['object', 'category']):
        df[col] = LabelEncoder().fit_transform(df[col])


    # Standardize the data
    X = StandardScaler().fit_transform(df)


    # Create and fit the t-SNE model for 3 components (3D)
    tsne = TSNE(n_components=3, verbose=1, perplexity=perplexity, n_iter=n_iter)
    tsne_results = tsne.fit_transform(X)


    # Plot the results in 3D
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')  # Create a 3D subplot
    ax.scatter(tsne_results[:,0], tsne_results[:,1], tsne_results[:,2])
    ax.set_title("3D t-SNE Transaction Visualization Transformers embeddings")
    ax.set_xlabel("t-SNE 1")
    ax.set_ylabel("t-SNE 2")
    ax.set_zlabel("t-SNE 3")



    plt.show()



import numpy as np




    








    

    