# Download the dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
asiangames_data = pd.read_csv(r'C:\Users\user\Desktop\python ML lab\Assignment 1\asiangamestop10.csv')

# a. Total Number of Records
total_records = asiangames_data.shape[0]

# b. Top n Records
top_n_records = asiangames_data.head(n=10)

# c. Rename 'NOC' to 'Country'
asiangames_data.rename(columns={'NOC': 'Country'}, inplace=True)

# d. Top 15 Year Wise Medals Count Using BarGraph
top15_year_medals = asiangames_data.groupby('Year')['Total'].sum().nlargest(15)
top15_year_medals.plot(kind='bar')

# e. Top 15 Country Wise Medals Count Using BarGraph
top15_country_medals = asiangames_data.groupby('Country')['Total'].sum().nlargest(15)
top15_country_medals.plot(kind='bar')

# f. Max, Min and Mean for Total Medals
max_medals = asiangames_data['Total'].max()
min_medals = asiangames_data['Total'].min()
mean_medals = asiangames_data['Total'].mean()

print("Total Number of Records:", total_records)
print("Top 10 Records:\n", top_n_records)
print("Max Medals:", max_medals)
print("Min Medals:", min_medals)
print("Mean Medals:", mean_medals)