text = "NLP is interesting. NLP is a part of AI."
sentences = text.split(". ")

words1 = set(sentences[0].split())
words2 = set(sentences[1].split())

score = len(words1 & words2) / len(words1 | words2)

print("Coherence Score:", round(score,2))
