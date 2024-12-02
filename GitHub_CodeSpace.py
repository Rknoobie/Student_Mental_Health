import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt

# Set figure size for seaborn plots
sns.set(rc={'figure.figsize': (15, 9)})

# Load the dataset
df = pd.read_csv('/workspaces/Student_Mental_Health/mentalhealth_dataset.csv')

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

# Plot the Timestamp histogram
g = sns.histplot(df, x='Timestamp', discrete=True)
g.set(title='Timestamp histogram')
xticks = g.get_xticks()
xticks_labels = g.get_xticklabels()
g.tick_params(axis='x', labelrotation=45)

# Show the plot
plt.show()

# Gender ratio plot
sns.countplot(df, x='Gender').set(title='Gender ratio')
plt.show()

# Age distribution plot
sns.countplot(df, x='Age').set(title='Students of different ages in data')
plt.show()

# Age and Gender distribution plot
sns.countplot(df, x='Age', hue='Gender').set(title='Students of different ages and genders in data')
plt.show()

# Course distribution (visualize popular ones)
sns.countplot(df[df.Course.apply(lambda x: df.Course.value_counts()[x] > 16)], x='Course').set(title='Most popular courses in data')
plt.show()


# Hm. We observe strange peaks at certain dates. Probably these are days when dataset's owner published it somewhere.

## `Gender`

sns.countplot(df, x='Gender').set(title='Gender ratio');
plt.show()

# Wow. Many women took part in the survey, significantly more than men. That's interesting. We will check later the same ratios for different courses.

## `Age`

sns.countplot(df, x='Age').set(title='Students of different ages in data');

# Nice. Dataset is slightly unballanced, but we have enough samples for ages from 18 to 25 years old. Let's check wheather gender ratio varies significantly for any age group.

sns.countplot(df, x='Age', hue='Gender').set(title='Students of different ages and genders in data');

# We observe no suspicious gender disbalance for any age group.

## `Course`

df.Course.value_counts()

# Okay, we have lot's of different courses here. Let's visualise only the most popular ones.

sns.countplot(df[df.Course.apply(lambda x: df.Course.value_counts()[x] > 16)], x='Course').set(title='Most popular courses in data');
plt.show()