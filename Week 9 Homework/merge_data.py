import pandas as pd
import os

# define path to CSV files
directory = r'C:\Users\jasse\Desktop\fit3179\Week 9 Homework\fit3179\Week 9 Homework\data'

# list all files in the directory
print("Files in the specified directory:")
print(os.listdir(directory))

# step 2: Load the CSV files
try:
    schools_df = pd.read_csv(os.path.join(directory, 'heritageitem_2020.csv'))  # contains school names and ItemName
    locations_df = pd.read_csv(os.path.join(directory, 'nsw_schools_data.csv'))  # contains latitude and longitude

    # print the column names to check for 'SchoolName'
    print("\nColumn names in schools DataFrame:")
    print(schools_df.columns)

    # extract the part before and after the dash in SchoolName for school name
    # this line was provided by ChatGPT
    schools_df['MatchName'] = schools_df['SchoolName'].str.split(' - ').str[0].str.strip().str.lower()  # part before dash for matching
    # this line was provided by ChatGPT
    schools_df['ItemName'] = schools_df['SchoolName'].str.split(' - ').str[1].str.strip()  # part after dash as ItemName
    
    # clean up the SchoolName in locations_df for matching
    # this line was provided by ChatGPT
    locations_df['SchoolName'] = locations_df['SchoolName'].str.strip().str.lower() 

    # merge the DataFrames on the MatchName column
    merged_df = pd.merge(schools_df, locations_df, left_on='MatchName', right_on='SchoolName', how='left')  # Keep all from schools_df

    # save the merged DataFrame to a new CSV file
    merged_df.to_csv(os.path.join(directory, 'merged_schools_data.csv'), index=False)
    print("\nMerged DataFrame saved as 'merged_schools_data.csv'.")

except FileNotFoundError as e:
    print(f"Error: {e}")
except KeyError as e:
    print(f"Key error: {e}")