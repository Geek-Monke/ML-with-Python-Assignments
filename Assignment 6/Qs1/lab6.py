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

