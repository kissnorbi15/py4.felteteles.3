'''
3. Feladat
Készíts egy programot! A gép "gondol" egy számra 1 és 5 között, vagyis egy változóban tárolj egy ilyen számot! Azután a program bekér egy számot a felhasználótól, majd kiírja, hogy ez a szám egyenlő-e a gép által "gondolt" számmal, vagy annál kisebb, illetve nagyobb.
'''
print('A gép gondol egy számra...')
import random
randomszam = random.randint(1,5)
szam = int(input('Kérek egy számot:'))
if szam == randomszam: 
 print('Eltaláltad, ügyes vagy!')
elif szam != randomszam and szam > randomszam:
  print('Sajnos balszerencsés vagy, a szám kisebb volt')
else:
  print('Sajnos balszerencsés vagy, a szám nagyobb volt')
