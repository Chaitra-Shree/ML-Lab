import pandas as pd
col =['Age','Gender','FamilyHist','Diet','LifeStyle','Cholesterol','HeartDisease']
data = pd.read_csv('lab7.csv',names =col )
print(data)

#encoding 
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
for i in range(len(col)):
    data.iloc[:,i] = encoder.fit_transform(data.iloc[:,i])

#spliting data
X = data.iloc[:,0:6]
y = data.iloc[:,-1]
from sklearn.model_selection import train_test_split

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#prediction
from sklearn.naive_bayes import GaussianNB
#Create naive bayes classifier
clf = GaussianNB()
#Fit the dataset on classifier
clf.fit(X_train,y_train)

#Perform prediction
y_pred = clf.predict(X_test)

#confusion mtx output
import numpy as np
from sklearn.metrics import confusion_matrix

labels = np.unique(y_test)
a = confusion_matrix(y_test, y_pred, labels=labels)

print('Confusion matrix')
cm =pd.DataFrame(a, index=labels, columns=labels)
 
print(cm)









