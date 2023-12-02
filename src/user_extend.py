import pandas as pd
from stockFeature import appendStockFeature
import multiprocessing as mp

def process_row(args):
    index, row = args
    appended = appendStockFeature(row)
    if appended is None:
        print(f"Index to drop: {index}")
        return index
    return None
def extend(df):
    # Create a pool of workers
    with mp.Pool(mp.cpu_count()) as pool:
        # Use map to distribute the tasks to the workers
        rows_to_drop = pool.map(process_row, df.iterrows())
    # Filter out None values
    rows_to_drop = [index for index in rows_to_drop if index is not None]
    # Drop the rows
    df = df.drop(rows_to_drop)
    return df

def main():
    # Read the xlsx file
    df = pd.read_excel('data/SwissQuote/Dataset_sq_EVA.xlsx')
    newdf = extend(df)
    ## Save the updated dataframe to a new csv file
    newdf.to_csv('data/extended/evaExtended.csv')

    ## Read the xlsx file
    df = pd.read_excel('data/SwissQuote/Dataset_sq_JOSEPH.xlsx')
    ## Apply the function in parallel
    newdf = extend(df)
    ## Save the updated dataframe to a new csv file
    newdf.to_csv('data/extended/JosephExtended.csv')

if __name__ == '__main__':
    freeze_support()
