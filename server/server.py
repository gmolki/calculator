from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def index():
    userSent = request.get_json()
    print '\tClient sent:', userSent
    return jsonify({"received": userSent})


if __name__ == '__main__':
    app.run(debug=True)
