"""
Folosind re.findall(), găsiți toate cuvintele care încep cu litera "p" sau "P" în următorul text:
text = "Programare în Python este foarte populară și interesantă!"
"""
import re

text = "Programare în Python este foarte populară și interesantă!"
results = re.findall(r"\b[pP]\w*", text)
print(results)
