import random
import time
from afinn import Afinn

# Prompt of Name
name = input("Hello, What is your name? \n")
time.sleep(2)

print("Hello "+name)

# Prompt of Feeling
feeling = input("How are you today? \n")
time.sleep(2)

afinn = Afinn()
affinScore = afinn.score(feeling)

if affinScore > 0:
   print("I am feeling good too!!")
else:
   print("I am sorry to hear that!!")

time.sleep(2)

# Prompt of Color
favcolour = input("What is your favourite color? \n")

colors = ["Red","Green","Blue"]
time.sleep(2)

print("My favourite color is "+ random.choice(colors))