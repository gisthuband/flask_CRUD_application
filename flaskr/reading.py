import pandas as pd

## this is a test to see if I am accessing the database correctly

read_df = pd.read_csv('flaskr/data.csv')

print (read_df.head())