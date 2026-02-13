text = "Ravi went to school. He was late."

sentences = text.split(". ")
noun = sentences[0].split()[0]   # Ravi

resolved = text.replace("He", noun)
print("Resolved Text:", resolved)
