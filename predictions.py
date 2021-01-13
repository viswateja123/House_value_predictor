
import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

data=pd.read_csv('Realestate.csv')
data.head()
x=data.drop(['No','X1 transaction date','Y house price of unit area'],axis=1)


print(x)

import seaborn as sb
sb.pairplot(data,height=4)

corrmat=data.corr()
sb.heatmap(corrmat, annot=True)

from sklearn.linear_model import LinearRegression
target=data['Y house price of unit area']
input=data.drop(['Y house price of unit area'],axis=1)
input=input.drop("No",axis=1)
input.head()


model=LinearRegression()
model.fit(input,target)

from sklearn.metrics import accuracy_score

temparray=list()

b=32.1
c=84.3
d=5
e=24.98298
f=121.54026
temparray+=[b,c,d,e,f]
X=np.array([temparray])
y=model.predict(X)
#accuracy_score(target[0],y)
print(y)

import pickle
filename = 'abc.pkl'
pickle.dump(model, open(filename, 'wb'))