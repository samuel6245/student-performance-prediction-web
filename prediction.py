import joblib

model1=joblib.load('model.pkl')
hours=2
attendance=12
result=model1.predict([[hours, attendance]])
print('prediction:',result[0])