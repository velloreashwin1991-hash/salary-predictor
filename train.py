import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Load CSV file
df = pd.read_csv("salary_data.csv")

# Features and target
X = df[["experience"]]
y = df["salary"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
