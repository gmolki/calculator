import logging

logging.basicConfig(filename='./server_log.txt',
                    filemode='w',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)


def log(data):
    logging.info(data)


def operate(value1, operator, value2):
    # Returns the operation between to values
    if (operator == "+"):
        return value1 + value2
    elif (operator == "-"):
        return value1 - value2
    elif (operator == "*"):
        return value1 * value2
    elif (operator == "/"):
        return value1 / value2


def calculate(value1, operator, value2):
    # Writes operation and solution in the log file and returns
    # the solution of it.
    logString = 'Operation:\t ' + \
                str(value1) + ' ' + \
                operator + ' ' + \
                str(value2)
    log(logString)

    solution = operate(value1, operator, value2)

    logString = 'Solution:\t ' + str(solution)
    log(logString)

    return solution
