import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 22, 23, 25],
    'Rating': [4.5, 4.0, 4.7, 4.8]
}
df = pd.DataFrame(data)

# a. Sum of columns
sum_cols = df.sum(numeric_only=True)

# b. Average age and rating
avg_age = df['Age'].mean()
avg_rating = df['Rating'].mean()

# c. Standard deviation
std_dev = df.std(numeric_only=True)

# d. Describe the DataFrame
description = df.describe()

print("Sum of columns:\n", sum_cols)
print("Average Age:", avg_age)
print("Average Rating:", avg_rating)
print("Standard Deviation:\n", std_dev)
print("Description:\n", description)