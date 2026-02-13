import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'she' [1.0]
VP -> 'eats' [1.0]
""")

parser = ViterbiParser(grammar)
sentence = "she eats".split()

for tree in parser.parse(sentence):
    print(tree)
