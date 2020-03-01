from flask import Flask, jsonify, request
import calculator

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    logString = ''
    if request.method == 'POST':
        userSent = request.get_json()
        if userSent['action'] == 'calculate':

            result = calculator.calculate(float(userSent['value1']),
                                          userSent['operator'],
                                          float(userSent['value2']))

            return jsonify({"sent": userSent, 'solution': result})

    elif request.method == 'GET':
        return '<h1>Hello!<h1>'


if __name__ == '__main__':
    app.run(debug=False)
