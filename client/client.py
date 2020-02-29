import csv
import requests
import sys
import getopt
import logging

logging.basicConfig(filename='./client_log.txt',
                    filemode='w',
                    format='%(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)


def log(data):
    logging.info(data)


def sendRequest(operation):
    # Sends request to the server and returns the json of the response
    serverResponse = requests.post(
        url='http://127.0.0.1:5000/', json=operation)
    return serverResponse.json()


def calculateCsv(file):
    # Reads .csv file and sends a request for each operation to the
    # server to calculate them
    logString = ''
    with open('sample.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        nReq = 0  # Counter of requests sent to the server
        for row in csv_reader:
            # Reads every row of the csv file and sends the data to the
            # server to get the operation result
            operation = {'value1': row[0],
                         'operator': row[1], 'value2': row[2]}
            logString = 'Operation:\t' + \
                operation['value1'] + ' ' + \
                operation['operator'] + ' ' + operation['value2']
            print(logString)
            log(logString)
            nReq += 1

            result = sendRequest(operation)

            logString = 'Result:\t' + str(result['solution'])
            print(logString)
            log(logString)


def main(argv):

    try:
        # Specify what options and arguments are accepted by the program
        unixOptions = "hi:"
        gnuOptions = ["help", "input="]
        opts, args = getopt.getopt(argv, unixOptions, gnuOptions)
    except getopt.error as err:
        # Print error information and exit
        print(str(err))
        sys.exit(2)

    for opt, arg in opts:
        # Define operations for each option
        if opt in ("-h", "--help"):
            # Help option
            print "\nUsage:\npython client.py [option] [arg]\n\nOptions and arguments:\n-h\t: print this help message and exit (also --help)\n-i\t: csv input file to read the operations and calculate them,\n\t  needed to specify the extension (also --input)\n"
            sys.exit(0)
        elif opt in ("-i", "--input"):
            # Input option
            print "input file\t: ", arg
            calculateCsv(arg)


if __name__ == "__main__":
    main(sys.argv[1:])
