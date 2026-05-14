import pandas as pd
import numpy as np

# --- INSTRUCTIONS ---
# Replace "YOUR_DIRECTORY_PATH_HERE" with the actual path to the folder 
# where your Kaggle CSV files are stored. 
# Keep the 'r' before the quotes so Windows file paths are read correctly.
BASE_PATH = r"YOUR_DIRECTORY_PATH_HERE"

oil = pd.read_csv(f'{BASE_PATH}/oil.csv')
oil['date'] = pd.to_datetime(oil['date'])
oil = oil.set_index('date').resample('D').mean().interpolate(method='linear').reset_index()
oil = oil.bfill()

holidays = pd.read_csv(f'{BASE_PATH}/holidays_events.csv')
holidays['date'] = pd.to_datetime(holidays['date'])
holidays = holidays[holidays['transferred'] == False]
holidays = holidays.drop_duplicates(subset=['date'], keep='first')

transactions = pd.read_csv(f'{BASE_PATH}/transactions.csv')
transactions['date'] = pd.to_datetime(transactions['date'])

stores = pd.read_csv(f'{BASE_PATH}/stores.csv')

train = pd.read_csv(f'{BASE_PATH}/train.csv')
train['date'] = pd.to_datetime(train['date'])

master = pd.merge(train, stores, on='store_nbr', how='left')
master = pd.merge(master, oil, on='date', how='left')
master = pd.merge(master, holidays[['date', 'type', 'locale', 'locale_name', 'description']], on='date', how='left')
master = pd.merge(master, transactions, on=['date', 'store_nbr'], how='left')

master['transactions'] = master['transactions'].fillna(0)

master.to_parquet(f'{BASE_PATH}/train_master.parquet', index=False)

test = pd.read_csv(f'{BASE_PATH}/test.csv')
test['date'] = pd.to_datetime(test['date'])

test_master = pd.merge(test, stores, on='store_nbr', how='left')
test_master = pd.merge(test_master, oil, on='date', how='left')
test_master = pd.merge(test_master, holidays[['date', 'type', 'locale', 'locale_name', 'description']], on='date', how='left')
test_master = pd.merge(test_master, transactions, on=['date', 'store_nbr'], how='left')

test_master['transactions'] = test_master['transactions'].fillna(0)

test_master.to_parquet(f'{BASE_PATH}/test_master.parquet', index=False)