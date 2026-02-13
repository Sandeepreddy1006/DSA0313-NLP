expression = "Loves(John,Mary)"

predicate = expression.split("(")[0]
arguments = expression.split("(")[1].replace(")", "")

print("Predicate:", predicate)
print("Arguments:", arguments)
