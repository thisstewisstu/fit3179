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

    # Print the column names to check for 'SchoolName'
    print("\nColumn names in schools DataFrame:")
    print(schools_df.columns)

    # Step 3: Clean up the 'SchoolName' column in schools_df for matching
    # Extract the part before and after the dash
    schools_df['MatchName'] = schools_df['SchoolName'].str.split(' - ').str[0].str.strip().str.lower()  # Part before dash for matching
    schools_df['ItemName'] = schools_df['SchoolName'].str.split(' - ').str[1].str.strip()  # Part after dash as ItemName
    
    # Clean up the SchoolName in locations_df for matching
    locations_df['SchoolName'] = locations_df['SchoolName'].str.strip().str.lower()  # this line was provided by ChatGPT

    # Step 4: Merge the DataFrames on the MatchName column
    merged_df = pd.merge(schools_df, locations_df, left_on='MatchName', right_on='SchoolName', how='left')  # Keep all from schools_df

    # Step 5: Save the merged DataFrame to a new CSV file
    merged_df.to_csv(os.path.join(directory, 'merged_schools_data.csv'), index=False)
    print("\nMerged DataFrame saved as 'merged_schools_data.csv'.")

except FileNotFoundError as e:
    print(f"Error: {e}")
except KeyError as e:
    print(f"Key error: {e}")
