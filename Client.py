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
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.manifold import TSNE
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.utils import shuffle



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

    def client_to_csv(self):
        df = pd.DataFrame(self.transactions)
        df.to_csv(self.name + '.csv')

    def update_first_column(self):
        for transaction in self.transactions:
            transaction['CLIENT'] = self.name
            


    def  AddSyntheticData(self, num_samples=100):
        # create a synthetic data and add it to the client
        df = pd.DataFrame(self.transactions)
        synthetic_df = createSyntheticData(df, num_samples=num_samples)
        list_of_vectors = create_list_of_vectors(synthetic_df)
        self.transactions = self.transactions + list_of_vectors

       



    

        
    #TSNE does not accept missing values encoded as NaN natively. For supervised learning, you might want to consider sklearn.ensemble.HistGradientBoostingClassifier and Regressor which accept missing values encoded as NaNs natively. Alternatively, it is possible to preprocess the data, for instance by using an imputer transformer in a pipeline or drop samples with missing values. See https://scikit-learn.org/stable/modules/impute.html You can find a list of all estimators that handle NaN values at the following page: https://scikit-learn.org/stable/modules/impute.html#estimators-that-handle-nan-values
    def plot_t_sne(self, perplexity=30, n_iter=250):
        df = pd.DataFrame(self.transactions)

        # Separate numeric and non-numeric columns
        numeric_cols = df.select_dtypes(include=[np.number])
        non_numeric_cols = df.select_dtypes(exclude=[np.number])

        # Impute missing values in numeric columns
        imputer = SimpleImputer(strategy='mean')
        numeric_cols_imputed = pd.DataFrame(imputer.fit_transform(numeric_cols), columns=numeric_cols.columns)

        # Encoding non-numeric columns
        for col in non_numeric_cols.columns:
            non_numeric_cols[col] = LabelEncoder().fit_transform(non_numeric_cols[col].astype(str))

        # Combine the data back
        df_imputed = pd.concat([numeric_cols_imputed, non_numeric_cols], axis=1)

        # Standardize the data
        X = StandardScaler().fit_transform(df_imputed)

        # Adjust perplexity based on the number of samples
        if X.shape[0] < perplexity:
            perplexity = X.shape[0] - 1

        # Create and fit the t-SNE model for 3 components (3D)
        tsne = TSNE(n_components=3, verbose=1, perplexity=perplexity, n_iter=n_iter)
        tsne_results = tsne.fit_transform(X)

        # Plot the results in 3D
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(tsne_results[:,0], tsne_results[:,1], tsne_results[:,2])
        ax.set_title("User " + self.name)
        ax.set_xlabel("t-SNE 1")
        ax.set_ylabel("t-SNE 2")
        ax.set_zlabel("t-SNE 3")
        plt.show()



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


# adjust this part depending on your exact dataset and requirements use the f
one_hot_encoder = OneHotEncoder()


# Print the list of vectors, only first 10 vectors using a DataFrame
def print_list_of_vectors(list_of_vectors):
    df = pd.DataFrame(list_of_vectors)
    print(df.head(5))
    



def plot_t_sne(list_of_vectors, perplexity=30, n_iter=300):

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
#,Unnamed: 0.2,Unnamed: 0.1,Unnamed: 0,CLIENT,NAME,PRODUCT_TYPE,ACTION,ACTION.1,DATE_TRANSACTION,QTY,UNIT_PRICE,ISIN_CODE,STOCK_LIBELLE,CURRENCY,TOTAL_AMOUNT,ACTION_TYPE,'CHF_'||CURRENCY,RATE_EUR,RATE_USD,StockFeature_address1,StockFeature_city,StockFeature_state,StockFeature_zip,StockFeature_country,StockFeature_phone,StockFeature_fax,StockFeature_website,StockFeature_industry,StockFeature_industryKey,StockFeature_industryDisp,StockFeature_sector,StockFeature_sectorKey,StockFeature_sectorDisp,StockFeature_longBusinessSummary,StockFeature_fullTimeEmployees,StockFeature_companyOfficers,StockFeature_auditRisk,StockFeature_boardRisk,StockFeature_compensationRisk,StockFeature_shareHolderRightsRisk,StockFeature_overallRisk,StockFeature_governanceEpochDate,StockFeature_compensationAsOfEpochDate,StockFeature_maxAge,StockFeature_priceHint,StockFeature_previousClose,StockFeature_open,StockFeature_dayLow,StockFeature_dayHigh,StockFeature_regularMarketPreviousClose,StockFeature_regularMarketOpen,StockFeature_regularMarketDayLow,StockFeature_regularMarketDayHigh,StockFeature_dividendRate,StockFeature_dividendYield,StockFeature_exDividendDate,StockFeature_payoutRatio,StockFeature_fiveYearAvgDividendYield,StockFeature_beta,StockFeature_trailingPE,StockFeature_forwardPE,StockFeature_volume,StockFeature_regularMarketVolume,StockFeature_averageVolume,StockFeature_averageVolume10days,StockFeature_averageDailyVolume10Day,StockFeature_bid,StockFeature_ask,StockFeature_bidSize,StockFeature_askSize,StockFeature_marketCap,StockFeature_fiftyTwoWeekLow,StockFeature_fiftyTwoWeekHigh,StockFeature_priceToSalesTrailing12Months,StockFeature_fiftyDayAverage,StockFeature_twoHundredDayAverage,StockFeature_trailingAnnualDividendRate,StockFeature_trailingAnnualDividendYield,StockFeature_currency,StockFeature_enterpriseValue,StockFeature_profitMargins,StockFeature_floatShares,StockFeature_sharesOutstanding,StockFeature_sharesShort,StockFeature_sharesShortPriorMonth,StockFeature_sharesShortPreviousMonthDate,StockFeature_dateShortInterest,StockFeature_sharesPercentSharesOut,StockFeature_heldPercentInsiders,StockFeature_heldPercentInstitutions,StockFeature_shortRatio,StockFeature_shortPercentOfFloat,StockFeature_impliedSharesOutstanding,StockFeature_bookValue,StockFeature_priceToBook,StockFeature_lastFiscalYearEnd,StockFeature_nextFiscalYearEnd,StockFeature_mostRecentQuarter,StockFeature_earningsQuarterlyGrowth,StockFeature_netIncomeToCommon,StockFeature_trailingEps,StockFeature_forwardEps,StockFeature_pegRatio,StockFeature_lastSplitFactor,StockFeature_lastSplitDate,StockFeature_enterpriseToRevenue,StockFeature_enterpriseToEbitda,StockFeature_52WeekChange,StockFeature_SandP52WeekChange,StockFeature_lastDividendValue,StockFeature_lastDividendDate,StockFeature_exchange,StockFeature_quoteType,StockFeature_symbol,StockFeature_underlyingSymbol,StockFeature_shortName,StockFeature_longName,StockFeature_firstTradeDateEpochUtc,StockFeature_timeZoneFullName,StockFeature_timeZoneShortName,StockFeature_uuid,StockFeature_messageBoardId,StockFeature_gmtOffSetMilliseconds,StockFeature_currentPrice,StockFeature_targetHighPrice,StockFeature_targetLowPrice,StockFeature_targetMeanPrice,StockFeature_targetMedianPrice,StockFeature_recommendationMean,StockFeature_recommendationKey,StockFeature_numberOfAnalystOpinions,StockFeature_totalCash,StockFeature_totalCashPerShare,StockFeature_ebitda,StockFeature_totalDebt,StockFeature_quickRatio,StockFeature_currentRatio,StockFeature_totalRevenue,StockFeature_debtToEquity,StockFeature_revenuePerShare,StockFeature_returnOnAssets,StockFeature_returnOnEquity,StockFeature_grossProfits,StockFeature_freeCashflow,StockFeature_operatingCashflow,StockFeature_earningsGrowth,StockFeature_revenueGrowth,StockFeature_grossMargins,StockFeature_ebitdaMargins,StockFeature_operatingMargins,StockFeature_financialCurrency,StockFeature_trailingPegRatio,StockFeature_address2



def csv_to_df(path):
    df = pd.read_csv(path)
    return df



import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.utils import shuffle
import numpy as np

import pandas as pd
from sklearn.utils import shuffle

def createSyntheticData(df, num_samples=50):
    # Prepare a container for synthetic samples
    synthetic_samples = []

    # Generate synthetic samples
    for _ in range(num_samples):
        # Select a random row from the DataFrame
        random_row = df.sample(1).copy()

        # Modify only numerical values
        for col in df.columns:
            #if col != "CLIENT"
            if col != "CLIENT" and col != "NAME" and col != "PRODUCT_TYPE" and col != "ACTION" and col != "ACTION.1" and col != "DATE_TRANSACTION" and col != "QTY" and col != "UNIT_PRICE" and col != "ISIN_CODE" and col != "STOCK_LIBELLE" and col != "CURRENCY" and col != "TOTAL_AMOUNT" and col != "ACTION_TYPE" and col != "CHF_CURRENCY" and col != "RATE_EUR" and col != "RATE_USD":
                if np.issubdtype(df[col].dtype, np.number):
                    random_row[col] = random_row[col].apply(lambda x: x * np.random.uniform(0.95, 1.05))

            if col == 'DATE_TRANSACTION':
                # Convert to datetime, add random days, and convert back to string
                random_row[col] = pd.to_datetime(random_row[col]) + pd.to_timedelta(np.random.randint(1, 1000), unit='D')
                random_row[col] = random_row[col].dt.strftime('%Y-%m-%d %H:%M:%S')


        # Add the modified row to the synthetic samples
        synthetic_samples.append(random_row)

    # Concatenate all synthetic samples into a single DataFrame
    synthetic_data = pd.concat(synthetic_samples, ignore_index=True)

    return shuffle(synthetic_data)

# Example usage
# df = pd.read_csv('your_data.csv')
# synthetic_df = createSyntheticData(df, num_samples=50)





    








    

    