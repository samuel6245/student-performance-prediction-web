import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

data=pd.read_csv('dataset/student.csv')
print(data)
x=data[['Hours','Attendance']]
y=data['Result']
model=DecisionTreeClassifier()
model.fit(x,y)
joblib.dump(model,'model.pkl')
print('model trained successfully')