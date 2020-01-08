import os
import pmdarima as pm
import joblib
from flask import Flask, request, jsonify, abort

model_path = os.environ.get("MODEL_PATH", "model.pickle")
app = Flask(__name__)

@app.route("/predict", methods=['GET'])
def get_prediction():
    n_days = int(request.args.get('n'))
    model = joblib.load(model_path)
    prediction = model.predict(n_periods=n_days)

    result = {}
    for idx, pred in enumerate(prediction):
        result['next_{}_day'.format(idx + 1)] = pred

    return jsonify(result)

