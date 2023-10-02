from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/hello/<name>")
def hello_world(name):
    return jsonify({"message": "Hello, {}!".format(name)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
