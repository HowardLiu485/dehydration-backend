from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

MODEL_PATH = "model/model.pkl"

# Try to load model. If not available, fallback to mock mode.
model = None
try:
    if os.path.exists(MODEL_PATH) and os.path.getsize(MODEL_PATH) > 0:
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
        print("Model loaded successfully!")
    else:
        print("model.pkl not found or empty — using mock mode.")
except Exception as e:
    print("Failed to load model. Using mock mode. Error:", e)
    model = None


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    hr = data.get("hr")
    temp = data.get("temp")
    activity = data.get("activity")

    # ----------- Mock prediction mode (currently used) -----------
    if model is None:
        if temp and temp > 37:
            risk = "HIGH"
            score = 90
        elif temp and temp > 36:
            risk = "MILD"
            score = 60
        else:
            risk = "NORMAL"
            score = 30

    # ----------- Real model mode (after Student 1 provides model.pkl) -----------
    else:
        features = [[hr, temp, activity]]
        risk = model.predict(features)[0]
        score = int(model.predict_proba(features).max() * 100)

    return jsonify({
        "risk": risk,
        "score": score
    })


if __name__ == "__main__":
    app.run(debug=True)