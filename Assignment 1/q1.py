import pandas as pd

# Creating the DataFrame
data = {
    'Roll number': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Total Marks': [85, 92, 78, 88],
    'Class': ['10th', '10th', '12th', '11th']
}
df = pd.DataFrame(data)

# Sorting by Name and Total Marks
df_sorted = df.sort_values(by=['Name', 'Total Marks'])
print(df_sorted)