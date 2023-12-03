import pandas as pd
import glob
def feedBackLoop(transaction_files, stockFeedback):
    for file in transaction_files:
        # Read the CSV file
        df = pd.read_csv(file)
        for index, row in df.iterrows():
            print(row['StockFeature_uuid'])
            print(stockFeedback['StockFeature_uuid'].values)
            if row['StockFeature_uuid'] not in stockFeedback['StockFeature_uuid'].values:
                print(f"Adding {row['StockFeature_uuid']} to stockFeedback \n")
                print("\n \n \n")
                new_row = pd.DataFrame(
                    {
                        'StockFeature_uuid': [row['StockFeature_uuid']],
                        'Feedback': [0]
                    }
                )
                stockFeedback = pd.concat([stockFeedback, new_row], ignore_index=True)
            if row['ACTION'] == 'BUY':
                stockFeedback.loc[row['StockFeature_uuid'], 'Feedback'] += 1
            elif row['ACTION'] == 'SELL':
                stockFeedback.loc[row['StockFeature_uuid'], 'Feedback'] -= 1
            break

    return stockFeedback
def main():
    pathUser = f"data/users"
    transaction_files = glob.glob(f'{pathUser}/*.csv')
    stockFeedback = pd.DataFrame(columns=['StockFeature_uuid', 'Feedback'])
    stockFeedback.concat([stockFeedback, pd.DataFrame({'StockFeature_uuid': "MFST", 'Feedback': 1})], ignore_index=True)
    print(stockFeedback.head())
    stockFeedback = feedBackLoop(transaction_files, stockFeedback)

    
    # Save the stockFeedback DataFrame to a CSV file
    stockFeedback.to_csv(f'{pathUser}/feedback.csv', index=False)
if __name__ == "__main__":
    main()
