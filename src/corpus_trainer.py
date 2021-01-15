import re
import collections

from resource_path import resource_path

def words(text): return re.findall('[a-z]+', text.lower()) 

def train(features):
    model = collections.defaultdict(lambda: 0)

    for f in features:
        model[f] += 1
    return model

filename = resource_path('data/big.txt')

f = open(filename, 'r')

NWORDS = train(words(f.read()))

f.close()