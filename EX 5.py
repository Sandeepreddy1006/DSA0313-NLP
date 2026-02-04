from nltk.stem import PorterStemmer

stemmer = PorterStemmer()
words = ["running", "flies", "happily", "cats"]

stems = [stemmer.stem(w) for w in words]
print("Stems:", stems)
