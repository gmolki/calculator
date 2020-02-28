from flask import Flask, jsonify, request


def calculate(value1, operator, value2):
    if (operator == "+"):
        return value1 + value2
    elif (operator == "-"):
        return value1 - value2
    elif (operator == "*"):
        return value1 * value2
    elif (operator == "/"):
        return value1 / value2


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        userSent = request.get_json()
        print '\tClient sent:', userSent
        solution = calculate(
            int(userSent['value1']), userSent['operator'], int(userSent['value2']))
        return jsonify({"sent": userSent, 'solution': solution})
    elif request.method == 'GET':
        return '<h1>Hello<h1>'


if __name__ == '__main__':
    app.run(debug=True)
