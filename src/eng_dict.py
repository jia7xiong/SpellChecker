from resource_path import resource_path

filename = resource_path('data/words_alpha.txt')

with open(filename, 'r') as f:
    DICT = [d.split()[0] for d in f]
