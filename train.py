import pickle
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1],[2],[3],[4],[5],[6],[7],[8]])
y = np.array([25000,30000,35000,45000,55000,65000,72000,80000])

model = LinearRegression()
model.fit(X,y)

with open("model.pkl","wb") as f:
    pickle.dump(model,f)

print("Model trained and saved")
