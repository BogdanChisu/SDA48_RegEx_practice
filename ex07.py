"""
Folosind re.search(), verificați dacă textul conține numere telefonice în formatul "07xx-xxx-xxx":
text = "Numarul de telefon pentru contact este 0777-555-234 iar cel de la recepție +407789-44445-58."
"""
import re
text = "Numarul de telefon pentru contact este 0777-555-234 iar cel de la recepție +407789-44445-58."

result = re.search("\d\d\d\d-\d\d\d\-\d\d\d", text)
if result:
    print("The text contains a phone number in the correct format.")
else:
    print("The text does not contain a phone number in the correct format")