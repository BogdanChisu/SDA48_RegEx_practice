"""
Folosind re.match(), verificați dacă următorul text începe cu "Python":
text = "Python este un limbaj de programare."
"""
import re
text = "Python este un limbaj de programare."
result = re.match("^Python", text)
if result:
    print("Yes. The string starts with Python!")
else:
    print("No, the string does not start with Python!")