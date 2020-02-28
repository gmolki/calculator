import csv
import requests
import sys
import getopt


def sendRequest(operation):
    serverResponse = requests.post(
        url='http://127.0.0.1:5000/', json=operation)

    resJson = serverResponse.json()
    print 'Operation:\t', operation['value1'], ' ', operation['operator'], ' ', operation['value2']
    print 'Result:\t\t', resJson['solution'], '\n'


def readCsv(file):
    with open('sample.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        nReq = 0  # Counter of requests sent to the server
        for row in csv_reader:
            # Reads every row of the csv file and sends the data to the
            # server to get the operation result
            operation = {'value1': row[0],
                         'operator': row[1], 'value2': row[2]}

            nReq += 1
            # print 'Request no. ', nReq
            sendRequest(operation)


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
            readCsv(arg)


if __name__ == "__main__":
    main(sys.argv[1:])
