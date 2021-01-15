import os
import sys
import getopt

from helper import usage

def get_filenames(argv):
    inputfile = ""
    outputfile = ""

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile=","help"]) 
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    if args:
        print("unrecognized command")
        usage()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if not inputfile and outputfile:
        print("option -o should be a subcommand of option -i")
        usage()
        sys.exit(2)
    
    if os.path.isdir(inputfile):
        print("IsADirectoryError: \"" + str(inputfile) + "\" is a directory, please check the name of file and retry.")
        sys.exit(1)
    
    if os.path.isdir(outputfile):
        if outputfile[-1] != '/':
            outputfile = outputfile + "/"
        outputfile = outputfile + "correct.txt"

    if inputfile and inputfile == outputfile:
        print("SameI/OFileError: Output file should not be the same as the input file, please check the name of files and retry.")
        sys.exit(1)

    return inputfile, outputfile
