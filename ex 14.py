import nltk

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'dogs'
VP -> 'run'
""")

parser = nltk.ChartParser(grammar)
sentence = "dogs run".split()

try:
    list(parser.parse(sentence))
    print("Sentence is grammatically correct")
except:
    print("Sentence is incorrect")
