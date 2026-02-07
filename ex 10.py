sentence = ["can", "fish"]
tags = ["NN", "NN"]

if sentence[0] == "can":
    tags[0] = "MD"

print(list(zip(sentence, tags)))
