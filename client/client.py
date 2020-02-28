import csv
import requests

with open('sample.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    nReq = 0
    for row in csv_reader:
        operation = {'value1': row[0], 'operator': row[1], 'value2': row[2]}
        print 'Request no. ', nReq
        print '\tSending:\t', operation
        serverResponse = requests.post(
            url='http://127.0.0.1:5000/', json=operation)
        resJson = serverResponse.json()
        nReq += 1
        print '\tResponse:\t', serverResponse.json()
