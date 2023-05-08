"""
Folosind re.search(), gasiti primele 2 cuvinte ce incep cu "ac" dintr-un text
(dati voi textul, dar sa fie compatibil) (edited)
"""
import re

strx = "Acea zi a fost acel odata ca niciodata accelerat, ca joac daca n-a fi fost, SDA48 nu ar fi existat in 2023, acum."
results = re.finditer(r"\bac\w*.", strx)
results_list = [res.group() for res in results]
print(results_list[0])
print(results_list[1])