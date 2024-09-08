import pandas as pd
import numpy as np

# Create the DataFrame
df = pd.DataFrame(data={
    'a': np.random.randint(0, 100, 30),
    'b': np.random.randint(0, 100, 30),
    'c': np.random.randint(0, 100, 30)
})
import matplotlib.pyplot as plt

# Create a figure of size 15x8
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,10))

# Plot lines in the top subplot
ax1.plot(df['a'], color='green', label='Green')
ax1.plot(df['b'], color='orange', label='Orange')

# Add legend to the top subplot in the top-middle
ax1.legend(loc='upper center')

# Plot points in the bottom subplot
ax2.scatter(df.index, df['a'], color='green', marker='x', label='a')
ax2.scatter(df.index, df['b'], color='red', marker='*', label='b')
ax2.scatter(df.index, df['c'], color='purple', marker='s', label='c')

# Add legend to the bottom subplot
ax2.legend(loc='upper right')

# Display the plots
plt.tight_layout()
plt.show()
# Create a new figure with bar graphs
fig, ax = plt.subplots(figsize=(8,10))

# Bar graph
df.plot(kind='bar', ax=ax)

# Display the bar plot
plt.show()