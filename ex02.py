"""
Folosind re.sub(), înlocuiți toate cuvintele care conțin cifre cu "abcx" în următorul text:
text = "Acesta este exercițiul nr2, care are 3 exemple."
"""
import re

text = "Acesta este exercițiul nr2, care are 3 exemple."
pattern = f"\w*\d+"
to_substitute = "abcx"
subs_rez = re.subn(pattern, to_substitute, text)
print(subs_rez)