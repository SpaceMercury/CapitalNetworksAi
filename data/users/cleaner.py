import glob
import pandas as pd
import concurrent.futures
import multiprocessing as mp
def process_file(filename):
    # Read the CSV file
    df = pd.read_csv(filename)
    # Remove "user" from the first column
    df.iloc[:, 1] = df.iloc[:, 1].str.replace("user", "")
    # Overwrite the original file
    df.to_csv(filename, index=False)

def main():
    csv_files = glob.glob('./*.csv')
    print(csv_files)
    # Create a pool of workers and apply `process_file` to all files
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_file, csv_files)
if __name__ == "__main__":
    mp.freeze_support()
    main()
