#combine, then remove duplicates, then sort based on saleDate

import pandas as pd

# Read the CSV files into pandas DataFrames
axie_sales_df = pd.read_csv("axie_sales.csv")
big_dataset_df = pd.read_csv("big_dataset.csv")
huge_dataset_df = pd.read_csv("huge_dataset.csv")

# Concatenate the DataFrames for axie_sales and huge_dataset
combined_df = pd.concat([axie_sales_df, huge_dataset_df], ignore_index=True)

# Concatenate the deduplicated combined DataFrame with big_dataset
final_combined_df = pd.concat([combined_df, big_dataset_df], ignore_index=True)

# Deduplicate the final combined DataFrame based on 'axieId' and 'priceEth'
final_combined_df = final_combined_df.drop_duplicates(subset=['axieId', 'priceEth'], keep='first')

# Sort the data by the 'saleDate' column in ascending order
final_combined_df = final_combined_df.sort_values(by='saleDate', ascending=True)

# Save the final combined DataFrame to a new CSV file
final_combined_df.to_csv("combined_data_corrected_sorted.csv", index=False)

# Check the first few rows of the combined DataFrame
print(final_combined_df.head())
