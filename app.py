from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def home():
    return "Salary Prediction API Running"

@app.route("/predict")
def predict():
    exp = int(request.args.get("experience"))

    prediction = model.predict([[exp]])

    return jsonify({
        "experience": exp,
        "predicted_salary": int(prediction[0])
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
