import pandas as pd

# Load the datasets
customers_df = pd.read_csv('Customers.csv', encoding='latin1')
# exchange_rates_df = pd.read_csv('C:\Users\DhinU\Desktop\Dataspark-EDA PowerBI Project/Exchange_Rates.csv', encoding='latin1')
# products_df = pd.read_csv('C:\Users\DhinU\Desktop\Dataspark-EDA PowerBI Project/Products.csv', encoding='latin1')
# stores_df = pd.read_csv('C:\Users\DhinU\Desktop\Dataspark-EDA PowerBI Project/Stores.csv', encoding='latin1')
# sales_df = pd.read_csv('C:\Users\DhinU\Desktop\Dataspark-EDA PowerBI Project/Sales.csv', encoding='latin1')

# Inspect the datasets
print("Customers Dataset Columns:\n", customers_df.columns, "\n")
# print("Exchange Rates Dataset Columns:\n", exchange_rates_df.columns, "\n")
# print("Products Dataset Columns:\n", products_df.columns, "\n")
# print("Stores Dataset Columns:\n", stores_df.columns, "\n")
# print("Sales Dataset Columns:\n", sales_df.columns, "\n")

# Display the first few rows of each dataset
print("First few rows of Customers Dataset:\n", customers_df.head(), "\n")
# print("First few rows of Exchange Rates Dataset:\n", exchange_rates_df.head(), "\n")
# print("First few rows of Products Dataset:\n", products_df.head(), "\n")
# print("First few rows of Stores Dataset:\n", stores_df.head(), "\n")
# print("First few rows of Sales Dataset:\n", sales_df.head(), "\n")
