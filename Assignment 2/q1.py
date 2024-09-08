import pandas as pd
import numpy as np
pl=pd.read_csv(r'C:\Users\ghosh\Desktop\ML with Python\Assignment 2\dataset.csv')
arr=np.array(pl)
print("Array values:\n", arr)
print("Shape of the array:", arr.shape)
