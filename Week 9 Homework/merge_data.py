import pandas as pd
import os

# Define the path to your CSV files
directory = r'C:\Users\jasse\Desktop\fit3179\Week 9 Homework\fit3179\Week 9 Homework'

# Step 1: List all files in the specified directory
print("Files in the specified directory:")
print(os.listdir(directory))

# Step 2: Load the CSV files
try:
    schools_df = pd.read_csv(os.path.join(directory, 'heritageitem_2020.csv'))  # contains school names and ItemName
    locations_df = pd.read_csv(os.path.join(directory, 'nsw_schools_data.csv'))  # contains latitude and longitude

    # Check the first few rows of each DataFrame to verify column names
    print("\nSchools DataFrame:")
    print(schools_df.head())
    
    print("\nLocations DataFrame:")
    print(locations_df.head())

    # Step 4: Merge the DataFrames on the common key 'ItemName'
    merged_df = pd.merge(schools_df, locations_df, on='ItemName', how='left')  # Use 'how='left'' to keep all rows from schools_df

    # Step 5: Save the merged DataFrame to a new CSV file
    merged_df.to_csv(os.path.join(directory, 'merged_schools.csv'), index=False)
    print("\nMerged DataFrame saved as 'merged_schools.csv'.")
    
except FileNotFoundError as e:
    print(f"Error: {e}")
