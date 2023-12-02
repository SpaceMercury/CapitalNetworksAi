import pandas as pd
from stockFeature import appendStockFeature
import multiprocessing as mp
def process_row(args):
    index, row = args
    appended = appendStockFeature(row)
    if appended is None:
        print(f"Index to drop: {index}")
        return index
    return appended

def extend(df):
    # Create a pool of workers
    with mp.Pool(mp.cpu_count()) as pool:
        # Use map to distribute the tasks to the workers
        rows_to_add = pool.map(process_row, df.iterrows())
    # Filter out None values
    new_rows = [row for row in rows_to_add if row is not None]

    # Create a DataFrame from new rows
    new_df = pd.DataFrame(new_rows)
    return new_df

def main():
    # Read the xlsx file
    df = pd.read_csv('data/extended/evaExtended.csv')
    newdf = extend(df)

    ## Save the updated dataframe to a new csv file
    newdf.to_csv('data/extended/evaExtended1.csv')

    ## Read the xlsx file
    df = pd.read_csv('data/extended/JosephExtended.csv')

    ## Apply the function in parallel
    newdf = extend(df)

    ## Save the updated dataframe to a new csv file
    newdf.to_csv('data/extended/JosephExtended1.csv')

if __name__ == '__main__':
    mp.freeze_support()  # Add this line
    main()
