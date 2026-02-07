import nltk
from nltk.parse.earleychart import EarleyChartParser
from nltk import CFG

grammar = CFG.fromstring("""
S -> NP VP
NP -> 'the' 'dog'
VP -> 'barks'
""")

parser = EarleyChartParser(grammar)
sentence = "the dog barks".split()

for tree in parser.parse(sentence):
    print(tree)
