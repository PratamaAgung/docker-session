from flask import Flask, request, jsonify, abort
from datetime import date

app = Flask(__name__)
@app.route("/")
def hello():
    today = date.today()
    return jsonify({
        "response": "Hello from my API",
        "time": "Today is {}".format(today.strftime("%d-%m-%Y"))
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
