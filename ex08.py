"""
Găsiți suma tuturor numerelor întregi din următorul text folosind re.findall():
text = "Acest text conține numerele 12, 7, 20 și 33." (edited)
"""

import re

text = "Acest text conține numerele 12, 7, 20 și 33."
results = re.findall("\d+", text)
numbers = [int(i) for i in results]
print(sum(numbers))