import random

text = "I love natural language processing"
words = text.split()

bigrams = {}
for i in range(len(words) - 1):
    key = words[i]
    value = words[i + 1]
    bigrams.setdefault(key, []).append(value)

word = "I"
for i in range(5):
    print(word, end=" ")
    word = random.choice(bigrams.get(word, words))
