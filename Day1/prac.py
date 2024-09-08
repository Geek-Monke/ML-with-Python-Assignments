import pandas as pd

data2 = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [20, 21, 19],
    'Rating': [4.5, 3.8, 4.2]
}

df2 = pd.DataFrame(data2)

# Sum of columns
column_sum = df2.sum()

# Average age and rating
average_age = df2['Age'].mean()
average_rating = df2['Rating'].mean()

# Standard deviation
std_deviation = df2.std()

# Describe the DataFrame
description = df2.describe()

print(column_sum, average_age, average_rating, std_deviation, description)