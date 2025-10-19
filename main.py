import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_csv('egypt_real_estate_listings.csv')

print(df.head())
print(df.info())

# Calculate % of Data Missing
columns = df.columns.to_list()

missing_percentage = []
for col in columns:
    missing_percentage.append(1 - (df[col].count()/len(df)))

for percent, col in enumerate(columns):
    print(f'{col}: {missing_percentage[percent]}')

