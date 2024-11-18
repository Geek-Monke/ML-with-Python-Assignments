import pandas as pd

#Load the data
data = pd.read_csv(r'C:\Users\ghosh\Desktop\ML with Python\Assignment 7\Heart.csv')

#1. Print the Shape of the Data
print("Shape of the Data:",data.shape)

#2. Find Missing Values
print("Missing Values:", data.isnull().sum())

#3. Find Data
selected_columns= ['Age','Sex','ChestPain','RestBP', 'Chol']
x = data[selected_columns]
y = data['AHD'].apply(lambda x: 1 if x == 'Yes' else 0)
X = pd.get_dummies(x, columns=['ChestPain'], drop_first=True)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=.35, random_state=42)
print('Training Set Shape:', x_train.shape)
print('Test Set Shape:', x_test.shape)

#4. Logistic Regression
from sklearn.linear_model import LogisticRegression
log_model = LogisticRegression()
log_model.fit(x_train,y_train)
y_log_pred = log_model.predict(x_test)

#5. KNN Algorithm
from sklearn.neighbors import KNeighborsClassifier
knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(x_train,y_train)
y_knn_pred = knn_model.predict(x_test)

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
#6. Confusion Matrix for Both
print('Confusion Matrix for Logistic Regression Model:', confusion_matrix(y_test,y_log_pred))
print('Confusion Matrix for KNN Model:', confusion_matrix(y_test,y_knn_pred))

#7. Accuracy Score for Both
print('Acuuracy Score for Logistic Regression Model:', accuracy_score(y_test,y_log_pred))
print('Acuuracy Score for KNN Model:', accuracy_score(y_test,y_knn_pred))

#8. Classification Report for Both
print('Classification Model for Logistic Regression Model:', classification_report(y_test,y_knn_pred))
print('Classification Model for KNN Model:', classification_report(y_test,y_knn_pred))

#9. Histogram
log_accuracy = accuracy_score(y_test,y_log_pred)
knn_accuracy = accuracy_score(y_test,y_knn_pred)

import matplotlib.pyplot as plt
models = ['Logistic Regression', 'KNN Model']
accuracies = [log_accuracy,knn_accuracy]
plt.bar(models,accuracies, color = [ 'Blue', 'Green'])
plt.ylabel['Accuracy']
plt.title['Accuracy comparision of two Models']
plt.show()