import sys
import getopt
import serverConnection as s


def main(argv):

    server = s.ServerConnection('http://127.0.0.1:5000/')
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
            server.calculateCsv(arg)


if __name__ == "__main__":
    main(sys.argv[1:])
