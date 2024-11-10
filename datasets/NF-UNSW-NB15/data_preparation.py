import pandas as pd
from sklearn.model_selection import train_test_split

# Step 1: Load the CSV file into a pandas DataFrame
df = pd.read_csv('NF-UNSW-NB15_0.csv')

# Step 2: Split the DataFrame into training and testing sets (80% train, 20% test)
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

# Step 3: Save the split DataFrames into separate CSV files
train_df.to_csv('train.csv', index=False)
test_df.to_csv('test.csv', index=False)

print(f"Number of entries in the test set: {len(train_df)}")