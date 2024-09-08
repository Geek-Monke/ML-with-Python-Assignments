import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(data={
    'a': np.random.randint(0, 100, 30),
    'b': np.random.randint(0, 100, 30),
    'c': np.random.randint(0, 100, 30)
})

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))

ax1.bar(df.index, df['a'], color='green', label='a')
ax1.set_title('Bar Graph')
ax1.set_xlabel('Index')
ax1.set_ylabel('Value')
ax1.legend()

ax2.bar(df.index, df['b'], color='orange', label='b')
ax2.set_title('Bar Graph')
ax2.set_xlabel('Index')
ax2.set_ylabel('Value')
ax2.legend()

ax3.bar(df.index, df['a'], color='green', label='a')
ax3.bar(df.index, df['b'], bottom=df['a'], color='orange', label='b')
ax3.set_title('Stacked Bar Graph')
ax3.set_xlabel('Index')
ax3.set_ylabel('Value')
ax3.legend()

plt.tight_layout()
plt.show()

fig, ax = plt.subplots(figsize=(8, 10))

total = df[['a', 'b']].sum()
ax.pie(total, labels=total.index, autopct='%1.1f%%', colors=['#66b3ff', '#ff9999'])

ax.set_title('Pie Chart')

plt.show()
