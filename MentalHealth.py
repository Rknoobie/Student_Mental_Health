import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(rc={'figure.figsize': (15, 9)})

# Ensure the correct file path
df = pd.read_csv('c:/Users/Sebastan/OneDrive/Desktop/github test/mentalhealth_dataset.csv')

# Print the first few rows of the dataframe
print("First few rows of the dataframe:")
print(df.head())

# Display the shape of the dataframe (rows, columns)
print("\nShape of the dataframe:")
print(df.shape)

# Get summary statistics of the dataframe
print("\nSummary statistics of the dataframe:")
print(df.describe())

# Check for missing values in the dataframe
print("\nMissing values in the dataframe:")
print(df.isna().sum())

# Wow. We have 1000 entries. No missing values. Data looks promissing, it would be interesting to know what features correlate with anxiety and depresion and to check, 
# wheather anxiety and depression have negative effects on CGPA.

## `Timestamp`

g = sns.histplot(df, x='Timestamp', discrete=True)
g.set(title='Timestamp histogram')
xticks = g.get_xticks()
xticks_labels = g.get_xticklabels()
g.tick_params(axis='x', labelrotation=45);
plt.show()

# Hm. We observe strange peaks at certain dates. Probably these are days when dataset's owner published it somewhere.