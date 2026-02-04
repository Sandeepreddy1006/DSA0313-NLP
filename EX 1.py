import re

text = "The rain in Spain falls mainly in the plain."
pattern = r"\bin\b"   # match word 'in'

matches = re.findall(pattern, text)
print("Matches:", matches)

search = re.search(r"Spain", text)
if search:
    print("Found:", search.group())
