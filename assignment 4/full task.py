import pandas as pd
import matplotlib.pyplot as plt

# Assuming the data is in a CSV file named 'company_sales_data.csv'
data = pd.read_csv('company_sales_data.csv')

# Task 1: Read Total profit of all months and show it using a line plot
plt.figure(figsize=(2,2))
plt.plot(data['month_number'], data['total_profit'], marker='o', linestyle='-', color='b')
plt.xlabel('Month Number')
plt.ylabel('Total profit')
plt.title('Profit of All Months')
plt.grid(True)
plt.show()


# Task 3: Read all product sales data and show it using a multiline plot
plt.figure(figsize=(3,6))
plt.plot(data['month_number'], data['facecream'], label='Face Cream', marker='o')
plt.plot(data['month_number'], data['facewash'], label='Face Wash', marker='o')
plt.plot(data['month_number'], data['toothpaste'], label='Toothpaste', marker='o')
plt.plot(data['month_number'], data['bathingsoap'], label='Bathing Soap', marker='o')
plt.plot(data['month_number'], data['shampoo'], label='Shampoo', marker='o')
plt.plot(data['month_number'], data['moisturizer'], label='Moisturizer', marker='o')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Sales Data of All Products')
plt.legend()
plt.grid(True)
plt.show()


# Task 3: Read all product sales data and show it using a multiline plot
plt.figure(figsize=(3,6))
plt.plot(data['month_number'], data['facecream'], label='Face Cream', marker='o')
plt.plot(data['month_number'], data['facewash'], label='Face Wash', marker='o')
plt.plot(data['month_number'], data['toothpaste'], label='Toothpaste', marker='o')
plt.plot(data['month_number'], data['bathingsoap'], label='Bathing Soap', marker='o')
plt.plot(data['month_number'], data['shampoo'], label='Shampoo', marker='o')
plt.plot(data['month_number'], data['moisturizer'], label='Moisturizer', marker='o')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Sales Data of All Products')
plt.legend()
plt.grid(True)
plt.show()


# Task 5: Read face cream and facewash product sales data and show it using the bar chart
plt.figure(figsize=(3,4))
bar_width = 0.4
plt.bar(data['month_number'] - bar_width/2, data['facecream'], width=bar_width, label='Face Cream', color='blue')
plt.bar(data['month_number'] + bar_width/2, data['facewash'], width=bar_width, label='Face Wash', color='orange')
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.title('Face Cream and Face Wash Sales Data')
plt.legend()
plt.grid(True)
plt.show()
