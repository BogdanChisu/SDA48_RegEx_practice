"""
Folosind re.split(), împărțiți următorul text în propoziții (delimitate de semne de punctuatie .!?:
text = "Bună ziua! Cum vă numiți? Eu sunt un student la SDA."
"""
import re

text = "Bună ziua! Cum vă numiți? Eu sunt un student la SDA."
sentences = re.split('[?!.]', text)
print(sentences)