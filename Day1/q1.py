import pandas as pd

data = {
    "Name" : ["Tiru", "Arijeet"],
    "Roll" : [1, 2],
    "Age" : [20, 20],
    "Marks" : [100, 100]
}

df = pd.DataFrame(data)
sorted_df = df.sort_values(by=["Name", "Age"]) 
print(sorted_df)