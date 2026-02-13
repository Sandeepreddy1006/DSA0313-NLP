import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple opened a new office in Hyderabad.")

for ent in doc.ents:
    print(ent.text, ent.label_)
