# Creating the DataFrame
import numpy as np
import pandas as pd
data = {
    'A': [1.0, 4.0, 7.0, np.nan],
    'B': [2, 5, 8, np.nan],
    'C': [3.0, 6.0, 9.0, np.nan]
}
df = pd.DataFrame(data)

# a. Display first 10 rows
print(df[:10])

# b. Apply aggregate functions row-wise
row_aggregate = df.aggregate(['sum', 'min', 'max'], axis=1)

# c. Apply aggregate functions column-wise
col_aggregate = df.aggregate(['sum', 'min', 'max'], axis=0)

print("Row-wise aggregate:\n", row_aggregate)
print("Column-wise aggregate:\n", col_aggregate)