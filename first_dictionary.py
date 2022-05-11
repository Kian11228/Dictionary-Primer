# first_dictionary.py

from microbit import *

sleep(1000)

string = input("Enter your name: ")

text = input("Enter a recent game score: ")
value = int(text)

info = {   }

info['name'] = string
info['score'] = value

print("Dictionary")
print("info = ", info)

name_val = info['name']
text = info['score']
score_val = int(text)

print("Hello", name_val, "your score was", score_val)
