from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

logging.basicConfig(filename='./server_log.txt',
                    filemode='w',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)


def log(data):
    logging.info(data)


def calculate(value1, operator, value2):
    if (operator == "+"):
        return value1 + value2
    elif (operator == "-"):
        return value1 - value2
    elif (operator == "*"):
        return value1 * value2
    elif (operator == "/"):
        return value1 / value2


@app.route('/', methods=['GET', 'POST'])
def index():
    logString = ''
    if request.method == 'POST':
        userSent = request.get_json()
        logString = 'Operation:\t ' + \
            userSent['value1'] + ' ' + userSent['operator'] + ' ' + \
            userSent['value2']
        log(logString)
        solution = calculate(
            float(userSent['value1']), userSent['operator'], float(userSent['value2']))

        logString = 'Solution:\t ' + str(solution)
        log(logString)
        return jsonify({"sent": userSent, 'solution': solution})
    elif request.method == 'GET':
        return '<h1>Hello!<h1>'


if __name__ == '__main__':
    app.run(debug=True)
