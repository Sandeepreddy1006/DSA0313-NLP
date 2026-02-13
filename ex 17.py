from nltk.corpus import wordnet as wn

synsets = wn.synsets("bank")

for s in synsets[:2]:
    print(s.name(), "-", s.definition())
