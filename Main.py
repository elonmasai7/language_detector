import langid
def detect_language(text):
    return langid.classify(text)[0]
text = input ("Enter in any language :")
print(detect_language(text))
