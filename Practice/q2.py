import pandas as pd

data ={
    'Name' : ["Ari", "Tiru"],
    'Age' : [20, 20],
    'Rating' : [5.5, 10.0]
}

df = pd.DataFrame(data) #Coloumn

col_sum = df.sum() #1 Coloumn Sum

avg_age = df['Age'].mean() #2 Average Age & Rating
avg_rating = df['Rating'].mean()

std_deviation = df.std() #3 Standard Deviation

description = df.describe() #4 Describe

print(col_sum, avg_age, avg_rating, std_deviation, description)