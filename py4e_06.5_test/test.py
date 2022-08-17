text = "X-DSPAM-Confidence:    0.8475"

_lookup = text.find(":")
print(float(text[_lookup + 1:].strip()))
