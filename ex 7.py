import nltk
from nltk import word_tokenize, pos_tag

sentence = "The dog is running"
tokens = word_tokenize(sentence)
tags = pos_tag(tokens)

print(tags)
