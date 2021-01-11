import numpy as np
from sklearn.datasets import load_iris 
iris=load_iris()

x=iris.data 
y=iris.target
print(x[:5],y[:5]) 

from sklearn.model_selection import train_test_split 

# random_state=1 ,0 or any integer s
#every time when you run your program you will get same output because of splitting between train and test varies within.
#For multiple times of execution of our model, random state make sure that data values will be same for training and testing data sets. 
#It fixes the order of data for train_test_split

xtrain,xtest,ytrain,ytest =train_test_split(x,y,test_size=0.4,random_state=1)

print(iris.data.shape) 

print(len(xtrain)) 

print(len(ytest))

from sklearn.neighbors import KNeighborsClassifier 

knn=KNeighborsClassifier(n_neighbors=1) 

knn.fit(xtrain,ytrain)

pred=knn.predict(xtest)

from sklearn import metrics 
print("Accuracy",metrics.accuracy_score(ytest,pred))

print(iris.target_names[2]) 
ytestn=[iris.target_names[i] for i in ytest]
predn=[iris.target_names[i] for i in pred]

print("  predicted     Actual")
for i in range(len(pred)):
    print(i,"   ",predn[i],"   ",ytestn[i]) 
