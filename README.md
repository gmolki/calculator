# HTTP Flask Server Calculator

HTTP Server written in python using the Flask library that can act as a simple calculator.

## Server

Inside the **server** folder

### Run the server

`python server.py`

### Files

- server.py > Receives clients requests and operates depending the request type and the action specified by the 'action' flag in the json
- calculator.py > Contains methods to make simple operations between two values

## Client

Inside the **client** folder

### Run the client

To send the operations written in a csv file (i.e. 'sample.csv'):
`python client.py -i sample.csv`

### Test the server

To test the methods used by the client in the server side:
`python unit_tests.py`

### Files

- client.py > Checks the flags written in CLI when executed and operates depending in this flags
- serverConnection.py > Sends request to the server and receives its responses
- unit_test.py > Tests the methods executed in the server side used by the client with unit tests
- sample.csv > Csv example file with values and operators
