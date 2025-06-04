import os
from flask import Flask, request, jsonify
from prediction import predict

app = Flask(__name__)

@app.route("/")
def home():
    return "Prophet Game Forecast API with regressors is running."

@app.route("/predict", methods=["POST"])
def predict_endpoint():
    data = request.get_json()
    game = data.get("game")
    months = int(data.get("months", 3))
    patch_count = data.get("Patch_Count")
    google_trend = data.get("Google_Trends_Index")

    try:
        result = predict(game, months, patch_count, google_trend)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001)) 
    app.run(host="0.0.0.0", port=port)
