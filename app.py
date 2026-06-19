from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load trained model
with open("salary_model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return "Salary Prediction API Running"

@app.route("/predict/<int:experience>")
def predict(experience):
    salary = model.predict([[experience]])[0]

    return jsonify({
        "experience": experience,
        "predicted_salary": int(salary)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
