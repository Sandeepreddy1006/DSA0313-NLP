sentence = "Can you help me?"

if "?" in sentence:
    print("Dialog Act: Question")
elif sentence.lower().startswith("please"):
    print("Dialog Act: Command")
else:
    print("Dialog Act: Statement")
