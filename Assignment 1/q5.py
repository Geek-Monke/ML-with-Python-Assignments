# Download the dataset
import numpy as np
import pandas as pd
phone_data = pd.read_csv(r'C:\Users\ghosh\Desktop\ML with Python\Assignment 1\phone_data.csv')

# a. Number of rows
num_rows = phone_data.shape[0]

# b. Longest phone call/data entry
longest_entry = phone_data['duration'].max()

# c. Total seconds of phone calls
total_phone_seconds = phone_data[phone_data['item'] == 'call']['duration'].sum()

# d. Number of non-null unique network entries
unique_networks = phone_data['network'].nunique()

# e. Number of entries for each month
phone_data['month'] = pd.to_datetime(phone_data['date']).dt.month
entries_per_month = phone_data['month'].value_counts()

# f. First entry for each month
first_entry_per_month = phone_data.groupby('month').first()

# g. Sum of durations per month
sum_duration_per_month = phone_data.groupby('month')['duration'].sum()

# h. Number of dates/entries in each month
num_entries_per_month = phone_data.groupby('month')['date'].nunique()

# i. Sum of durations for calls to each network
sum_duration_calls_per_network = phone_data[phone_data['item'] == 'call'].groupby('network')['duration'].sum()

# j. Number of calls, sms, and data entries in each month
calls_sms_data_per_month = phone_data.groupby(['month', 'item']).size().unstack(fill_value=0)

# k. Calls, texts, and data sent per month, split by network type
monthly_network_split = phone_data.groupby(['month', 'network', 'item']).size().unstack(fill_value=0)

print("Number of rows:", num_rows)
print("Longest entry duration:", longest_entry)
print("Total phone call seconds:", total_phone_seconds)
print("Unique networks:", unique_networks)
print("Entries per month:\n", entries_per_month)
print("First entry per month:\n", first_entry_per_month)
print("Sum of durations per month:\n", sum_duration_per_month)
print("Number of entries per month:\n", num_entries_per_month)
print("Sum of durations for calls per network:\n", sum_duration_calls_per_network)
print("Calls, SMS, Data entries per month:\n", calls_sms_data_per_month)
print("Monthly network split:\n", monthly_network_split)