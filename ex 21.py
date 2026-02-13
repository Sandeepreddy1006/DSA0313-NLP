import nltk
from nltk import word_tokenize, pos_tag, RegexpParser

sentence = "The big dog chased a cat"
tokens = word_tokenize(sentence)
tags = pos_tag(tokens)

grammar = "NP: {<DT>?<JJ>*<NN>}"
cp = RegexpParser(grammar)
tree = cp.parse(tags)

for subtree in tree.subtrees():
    if subtree.label() == "NP":
        print("Noun Phrase:", subtree)
