"""
Folosind re.sub(), înlăturați toate caracterele speciale din următorul text:
text = "Python!-+(){}{} este,. :=? un `%!@ limbaj $%&*=."
"""

import re

text = "Python!-+(){}{} este,. :=? un `%!@ limbaj $%&*=."
result = re.sub("\W+", "", text)
print(result)