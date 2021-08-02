'''A: Bulls & Cows
Tvým úkolem bude vytvořit program, který by simuloval hru Bulls and Cows. Hra funguje následovně:

Počítač vygeneruje tajné 4místné číslo. Každá číslice tohoto čísla musí být jiná.
Počítač vždy vyzve uživatele, aby hádal toto číslo.
Počítač vyhodnotí tip uživatele a vrátí počty shod.
Pokud uživatel uhádne správné číslo i správnou pozici, jedná se o "bulls". Pokud je pozice jiná, ale číslice je správná, jedná se o "cows".
Příklad hry s číslem 2017
Hi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
Enter a number
>>> 1234
0 bulls, 2 cows
>>> 6147
1 bull, 1 cow
>>> 2417
3 bulls, 0 cows
>>> 2017
Correct, you've guessed the right number in 4 guesses!
That's {amazing, average, not so good, ...}
Program toho může umět víc. Můžeš přidat například:

vrácení času, tedy jako dlouho uživateli trvalo číslo uhodnout,uchovávání statistik počtu odhadů jednotlivých her.'''

import random

# generate number to be guessed
number = []
separator = '= ' * 50

while len(number) < 4:
  a = random.randint(0,9)
  if a not in number:
    number.append(a)
  secret_no = ['_'] * len(number)

print (separator)
print ('''\nHi there!
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.\n''')
print (separator)

# correct input format compare with generated number and print result
def main():
  guess = (guess_No())
  count = 0

  while ([str(n) for n in guess]) != ([str(n) for n in number]):
    bulls = 0
    cows = 0
    for i in range (len(number)):
        if (guess)[i] == str(number[i]):
          bulls += 1
        else:
          if int (guess[i]) in number:
            cows += 1
    count += 1
    print (f'{cows} cows, {bulls} bulls')
    guess = (guess_No())

  # marking result as: amazing!, average or not so good :(
  if count < 10:
    result = 'are amazing!'
  elif count < 20:
    result = 'are average.'
  elif count < 30:
    result = 'are not so good :('
  else:
    result = 'SUCK !!!!'
  
  print (separator)
  print (f"\nCorrect, you've guessed the right number in {count} guesses!")
  print (f'That indicates you {result}\n')
  print (separator)

# input from user and check for correct input format (4 different digits)
def guess_No():
  guess = (input ('Enter a number:\t'))
  passing = 0

  while passing == 0:
    if guess.isdigit() and\
      (len([str(n) for n in guess])) == 4:
      passing = 1
      if any([(guess.count(g) != 1) for g in guess]):
          passing = 0
          guess = (input ('\nEnter a 4 (different) digit number: '))
    else:
      guess = (input ('\nEnter a 4 digit number:\t'))
  return guess


(main())

