import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, f1_score, recall_score, classification_report
import matplotlib.pyplot as plt

#Load the data
data = pd.read_csv(r'C:\Users\ghosh\Desktop\ML with Python\Assignment 7\Heart.csv')

#1. Print the Shape of the Data
print("Shape of the Data:",data.shape)

#2. Find Missing Values
print("Missing Values:", data.isnull().sum())