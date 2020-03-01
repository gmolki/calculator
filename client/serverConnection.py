import csv
import requests
import logging


class ServerConnection:
    def __init__(self, url):
        self.url = url
        logging.basicConfig(filename='./client_log.txt',
                            filemode='w',
                            format='%(asctime)s - %(message)s',
                            datefmt='%d-%b-%y %H:%M:%S',
                            level=logging.INFO)

    def log(self, data):
        logging.info(data)

    def sendRequest(self, operation):
        # Sends request to the server and returns the json of the response
        serverResponse = requests.post(
            url=self.url, json=operation)
        return serverResponse.json()

    def calculateCsv(self, file):
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
                self.log(logString)
                nReq += 1

                result = self.sendRequest(operation)

                logString = 'Result:\t' + str(result['solution'])
                print(logString)
                self.log(logString)
