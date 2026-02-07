import re

rules = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*s$', 'NNS'),
    (r'.*', 'NN')
]

sentence = "Dogs are running"
words = sentence.split()

for word in words:
    for pattern, tag in rules:
        if re.match(pattern, word.lower()):
            print(word, tag)
            break
