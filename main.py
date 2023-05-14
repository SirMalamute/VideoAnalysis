from flask import Flask, request, jsonify
from runner import main
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    print(request.args.get("id"))
    s, h, n, p = main([request.args.get("id")])
    return jsonify(
        sentiment= s,
        not_hate= h,
        sfw= n,
        profanity= p
    )

if __name__ == '__main__':
    app.run()