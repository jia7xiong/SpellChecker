import re
import sys

from eng_dict import DICT
from correction import correct

def tokenizer(l, num_l):  
    no_error = True
    tokens = re.split(r'\W', l)
    not_alpha = 0

    correct_line = []

    for num_c, tok in enumerate(tokens):
        tok = tok.lower()
        if tok.isalpha():
            if tok not in DICT:
                no_error = False
                best , candidates = correct(tok)
                print("SpellError(Line#" + str(num_l+1) + ", Word#" + str(num_c+1-not_alpha) + "): \'" + str(tok) + "\'")
                print("You may choose a correct alternative from the set", candidates)
                print("Do you mean the word? \'" + best + "\'\n\n")
                correct_line.append(best)
            else:
                correct_line.append(tok)
        else:
            not_alpha += 1
            correct_line.append(tok)

    if no_error:
        return l, no_error
    else:
        return " ".join(correct_line), no_error

def spell_check(inputfile, outputfile):
    no_error = True

    if inputfile == "":
        l = input("Please type in your sentence: ")
        print("---------------------------------------------------------\n")
        print("-----------------Spell Checking Complete-----------------\n")
        blah, no_error = tokenizer(l, 0)

    else:
        if outputfile:
            try:
                f2 = open(outputfile, 'w')
            except:
                outputfile = "../output/correct.txt"
                
                if inputfile == outputfile:
                    print("SameI/OFileError: Output file should not be the same as the input file, please check the name of files and retry.")
                    sys.exit(1)

                f2 = open(outputfile, 'w')
        
        try:
            with open(inputfile, 'r') as f1:
                line = f1.readlines()
                print("---------------------------------------------------------\n")
                print("-----------------Spell Checking Complete-----------------\n")
                if outputfile:
                    print("Check spell-error-free file there: " + outputfile)
                    print("---------------------------------------------------------\n")
                for num_l, l in enumerate(line):
                    correct_line, line_no_error = tokenizer(l, num_l)
                    if outputfile:
                        f2.write(correct_line)
                        f2.write("\n")
                    if not line_no_error:
                        no_error = False

        except FileNotFoundError:
            print("FileNotFoundError: Input file does not exist, please check the name of file and retry.")
            sys.exit(1)

        if outputfile:
            f2.close()
        
    if no_error:
        print("This is a perfect spell-error-free text!")