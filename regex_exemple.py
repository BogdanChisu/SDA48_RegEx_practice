import re
#  libraria de expresii built-in

# exemplul 1 - cautam toate aparitiile unui substring-pattern in altul
# findall

# strx = 'In clasa SDA sunt 15 studenti si cursul dureaza 3 ore 29 minute'
# pattern = r'\d+' # returns a match where the string contains digits
# numbers_found = re.findall(pattern, strx)
# print(f"Nr found in string = {numbers_found}")

# ex 2 - inlocuiesc toate aparitiile unui substring-pattern

# pattern = r'^Salutare'
#^ inseamna ca incepe cu
# fara ^ inlocuia toate aparitiile cuvantului, nu doar prima aparitie in string
# text1 = 'Salutare Andrei, stiai ca salutare este informal?'
# match_1 = re.match(pattern, text1)
# print(bool(match_1))
# text_inlocuit = re.sub(pattern, "Hello", text1)
# print(text_inlocuit)

# extract strings baza tpe o regula, folosim \W
# returns a match where the string doesn;t contain any word characters
#
# pattern = r"\W+"
# strx = 'In clasa SDA sunt 15 studenti si cursul dureaza 3 ore 29 minute'
# tokens = re.split(pattern, strx)
# print(tokens)

#ex4 - prima aparitie a unui substring-pattern in text
# pattern = f'\d+'
strx = 'In clasa de SDA sunt 15 studenti si cursul dureaza 3 ore 29 minute'
# search_result = re.search(pattern, strx)
# print(search_result.group())
#returneaza primul obiect gasit care respecta pattern-ul definit
pattern2 = r"\s[a-z]{2}\s"
search_result2 = re.search(pattern2,strx)
print(f"Primul match {pattern2} = {search_result2.group()}")

# exemplul 5
# finditer - returns iterator
# pattern = f'\d+'
# strx = 'In clasa SDA sunt 15 studenti si cursul dureaza 3 ore 29 minute'
# results_iter = re.finditer(pattern, strx)
# results_as_list = [el.group() for el in results_iter]
# print(results_as_list)
# for el in results_iter:
#     print(el.group())

# pattern = f'\d+'
# strx = 'In clasa SDA sunt 15 studenti si cursul dureaza 3 ore 29 minute'
# to_substitute = "xyz"
# subs_rez = re.subn(pattern, to_substitute, strx)
# print(subs_rez)
# print(f"Substituted string is: \n{subs_rez[0]} there were {subs_rez[1]} substitutions.")