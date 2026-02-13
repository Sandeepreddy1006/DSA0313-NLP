# pip install transformers

from transformers import pipeline

translator = pipeline("translation_en_to_fr")
result = translator("I love natural language processing")

print(result[0]['translation_text'])
