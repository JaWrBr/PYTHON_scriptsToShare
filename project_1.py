'''Tvým cílem bude vytvořit Textový analyzátor - program, který se bude umět prokousat libovolně dlouhým textem a zjistit o něm různé informace. Ještě než začneš, doporučíme ti použít námi předpřipravené texty. Kód se ti pak bude lépe kontrolovat. Tyto texty jsou dostupné zde.

Pojď se podívat, co všechno by tvůj program měl umět:

1. Na začátku přivítá uživatele.
2. Vyžádá si od uživatele přihlašovací jméno a heslo.
3. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.

4. Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS.

5. Pro vybraný text spočítá následující statistiky:
- počet slov,
- počet slov začínajících velkým písmenem,
- počet slov psaných velkými písmeny,
- počet slov psaných malými písmeny,
- počet čísel (ne cifer!).

6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:

 1 * 1
 2 *********** 11
 3 *************** 15
 4 ********* 9
 5 ********** 10
V textu, ze kterého byl vytvořen tento graf, je tedy pouze 1 jednopísmené slovo, 11 slov složených ze dvou písmen, a tak dále.

7. Program spočítá součet všech čísel (ne cifer!) v textu. '''


separator1 = '-'*50

TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

#1. Na začátku přivítá uživatele.
print (separator1)
print ('Welcome to the app. Please log in:')

#2. Vyžádá si od uživatele přihlašovací jméno a heslo.
user = input ('USERNAME: ')
password = input ('PASSWORD: ')
print (separator1)

#3. Zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů.

registered = {'USER':'PASSWORD', 'bob':'123' ,'ann':'pass123','mike':'password123','liz':'pass123' }
while registered.get(user)!=password:
  print ('\nWrong username or password.\nPlease try again:\n')
  user = input ('USERNAME: ')
  password = input ('PASSWORD: ')
  print (separator1)


#4. Program nechá uživatele vybrat mezi třemi texty, uloženými v proměnné TEXTS.
print ('We have 3 texts to be analyzed.')
text_select_index = int(input('Enter a number btw. 1 and 3 to select: '))
print (separator1)

text_select = TEXTS[text_select_index-1]
text_select = text_select.split()

#5.1 Pro vybraný text spočítá následující statistiky: - počet slov,
print (f'There are {len(text_select)} words in the selected text.')

#5.2 - počet slov začínajících velkým písmenem,
titlecaseWordsCount = 0
#5.3- počet slov psaných velkými písmeny,
uppercaseWordsCount = 0
#5.4- počet slov psaných malými písmeny,
lowercaseWordsCount = 0
#5.5- počet čísel (ne cifer!)
numericCount = 0
numericSum = 0

pocetPismen = {}

while text_select:
  word = text_select.pop()
  word = word.strip(" ., ")
  pocetPismen[len(word)] = pocetPismen.get(len(word),0)+1
  if word.isupper():
    uppercaseWordsCount += 1
  elif word.istitle():
    titlecaseWordsCount +=1
  elif word.islower():
    lowercaseWordsCount += 1
  elif word.isdigit():
    numericCount += 1
    numericSum = int(word) + numericSum

print (f'There are {titlecaseWordsCount} titlecase words')
print (f'There are {uppercaseWordsCount} uppercase words')
print (f'There are {lowercaseWordsCount} lowercase words')
print (f'There are {numericCount} numeric strings')

print (separator1)

#6. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. 
pocetPismen = dict(sorted(pocetPismen.items(), reverse = True))

while pocetPismen:
  item = pocetPismen.popitem()
  print (f'{str(item[0])} {"*"*int(item[1])} {str(item[1])}')

#7. Program spočítá součet všech čísel (ne cifer!) v textu. 
print (separator1)
print (f'If we summed all the numbers in this text we would get: {numericSum}')
print (separator1)

