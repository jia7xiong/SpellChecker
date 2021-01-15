[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)

# Spell Checker
This command line program allows you to either spell check a sentence or a .txt file. It will provide list of misspelled words with correct alternatives for each, and can generate a most probable correct version of text based on a [large English corpus](./data/big.txt).

## Background
With the help of a complete vocabulary, it is trivial to check if there are misspelled words. This project mainly focus on how to automatically suggest potential correct candidates and choose the optimum through [maximum likelihood estimation](https://en.wikipedia.org/wiki/Maximum_likelihood_estimation) and [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance) metric. To make it simple, instead of computing [N-gram](https://en.wikipedia.org/wiki/N-gram)(N>1), here, I estimate the probability of a word, by counting the number of times each word appears in a plain text file of about a million words, which is a concatenation of public domain book excerpts from Project Gutenberg and lists of most frequent words from Wiktionary and the British National Corpus. 

## Usage
Run the unix executable file
```sh
$ ./bin/spell_checker 
```
```
spell_checker [-h][-i <inputfile> [-o <outputfile>]]
Options:
	 -h 	 print this help message and exit (also --help)
	 -i 	 input the file to be checked (also --ifile)
	 -o 	 output the correct version of inputfile (also --ofile)
```
or
### 
```sh
$ python3 ./src/main.py
```
You may carry your own [corpus](./data/big.txt) and [vocabulary](./data/words_alpha.txt) to improve accuracy. I personally recommend [PyInstaller](https://www.pyinstaller.org) for quickly creating an executable.

## Related Efforts
- [English Words](https://github.com/dwyl/english-words) - 📝 A text file containing 479k English words for all your dictionary/word-based projects
- [Pytudes](https://github.com/norvig/pytudes) - Python programs, usually short, of considerable difficulty, to perfect particular skills.

## Maintainers
[@jia7xiong](https://github.com/jia7xiong)
