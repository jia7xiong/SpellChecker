from corpus_trainer import NWORDS
from eng_dict import DICT

# All edits that are one edit away from `word`
def edits1(word):
    n = len(word)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    return set([word[0:i]+word[i+1:] for i in range(n)] +                     # deletion
               [word[0:i]+word[i+1]+word[i]+word[i+2:] for i in range(n-1)] + # transposition
               [word[0:i]+c+word[i+1:] for i in range(n) for c in alphabet] + # alteration
               [word[0:i]+c+word[i:] for i in range(n+1) for c in alphabet])  # insertion

#  All edits that are two edits away from `word`
def edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1))

# The subset of `words` that appear in the dictionary of NWORDS
def known(words): return set(w for w in words if w in NWORDS)

def correct(word):
    # Generate possible spelling corrections for word
    candidates = known([word]) or known(edits1(word)) or known(edits2(word)) or [word]

    can = set()

    for c in candidates:
        if c in DICT:
            can.add(c)

    # Most probable spelling correction for word
    return max(candidates, key=lambda w: NWORDS[w]), candidates
