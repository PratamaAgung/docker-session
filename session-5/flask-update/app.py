import os
import pmdarima as pm
import joblib
from flask import Flask, request, jsonify, abort

model_path = os.environ.get("MODEL_PATH", "model.pickle")
app = Flask(__name__)

@app.route("/update", methods=['GET'])
def get_prediction():
    try:
        height = int(request.args.get('height'))
        model = joblib.load(model_path)
        model.update([height])
        joblib.dump(model, model_path)
        return jsonify({
            "status": "Success",
            "message": "Model updated!"
        })
    except Exception as e:
        return jsonify({
            "status": "Error",
            "message": "{}".format(e)
        })