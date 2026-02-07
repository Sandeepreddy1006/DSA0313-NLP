import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V
Det -> 'the'
N -> 'cat'
V -> 'slept'
""")

parser = nltk.ChartParser(grammar)
sentence = "the cat slept".split()

for tree in parser.parse(sentence):
    print(tree)
