import sys

from spell_checker import spell_check
from get_filenames import get_filenames

def main(argv):
    inputfile, outputfile = get_filenames(argv)
    spell_check(inputfile, outputfile)
    return

if __name__ == "__main__":
    main(sys.argv[1:])