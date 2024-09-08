import numpy as np
import pandas as pd
# Creating a DataFrame with random values
df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])

# Row-wise sum using apply()
row_sum = df.apply(np.sum, axis=1)
print(row_sum)