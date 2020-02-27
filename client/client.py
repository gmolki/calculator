import csv
import requests

with open('sample.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    nReq = 0
    for row in csv_reader:
        serverResponse = requests.get(
            url='http://127.0.0.1:5000/', json={"operation": row})
        nReq += 1
        print 'Request no. ', nReq
        print '\tSending:\t', row
        print '\tResponse:\t', serverResponse.json()
