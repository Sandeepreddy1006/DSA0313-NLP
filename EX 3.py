import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')

text = "Natural Language Processing is interesting."

tokens = word_tokenize(text)
tags = pos_tag(tokens)

print(tokens)
print(tags)
