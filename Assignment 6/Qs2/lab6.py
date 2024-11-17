#Question-1

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, cohen_kappa_score

#Load the Dataset and create a Dataframe
iris = load_iris()
x = iris.data
y = iris.target

#Train and Tst Split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=.2, random_state=42)

#KNN Classifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)
y_pred = knn.predict(x_test)

#Accuracy Score
accuracy=accuracy_score(y_test, y_pred)
print("Accuracy:",accuracy)

#Confusion Matrix
conf_matrix=confusion_matrix(y_test, y_pred)
print("Confusion Matrix:",conf_matrix)

#Classification Report
print("Classification Report:\n", classification_report(y_test, y_pred))

#Question-2
import matplotlib.pyplot as plt

def knn_accuracy(x,y,test_size):
    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=test_size, random_state=42)
    knn = KNeighborsClassifier(n_neighbors=3)
    knn.fit(x_train,y_train)
    y_pred = knn.predict(x_test)
    return accuracy_score(y_test, y_pred)

#70-30 & 65-35 Splits
accuracy_80_20 = accuracy
accuracy_70_30 = knn_accuracy(x,y,test_size=.3)
accuracy_65_35 = knn_accuracy(x,y,test_size=.35)

# Display the accuracies
print("80-20 Accuracy:", accuracy_80_20)
print("70-30 Accuracy:", accuracy_70_30)
print("65-35 Accuracy:", accuracy_65_35)

#Bar Graph for the accuracies
splits = ['80-20', '70-30', '65-35']
accuracies = [accuracy_80_20, accuracy_70_30, accuracy_65_35]

plt.bar(splits, accuracies, color = ['green', 'blue', 'red'])
plt.xlabel("Train Test Splits")
plt.ylabel("Accuracy")
plt.title("KNN Accuracy for Different Splits")
plt.show()