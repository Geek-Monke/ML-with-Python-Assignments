import pandas as pd

# Load the dataset
data = pd.read_csv(r'C:\Users\user\Desktop\python ML lab\sample\bacteria_list_200.csv')

# Display the first few rows of the dataset to understand its structure
print(data.head())

# Function to display bacteria information based on where they are found
def display_bacteria_info(location):
    filtered_data = data[data['Where Found'] == location]
    if filtered_data.empty:
        print(f"No bacteria found in location: {location}")
    else:
        for index, row in filtered_data.iterrows():
            print(f"Name: {row['Name']}, Family: {row['Family']}, Harmful for Humans: {row['Harmful to Humans']}")

# User input for location
location_input = input("Enter the location where the bacteria are found: ")

# Display the bacteria information based on user input
display_bacteria_info(location_input)

