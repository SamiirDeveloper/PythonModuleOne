import random
#Foundations of Python
#Create a program that takes your name, age and favorite color as an input and prints them out.

name = input("Whats your name ")
age = int(input("Whats your age: "))
color = input("What's your favorite color: ")

print(f"Your name is: {name}.")
print(f"You're {age} year's old ")
print(f"your favorite color is {color} ") 

#Build a program that asks the user to input their exam score then prints a message.

score = int(input("What's your score? "))

if score > 90:
   print("Excellent")
elif score > 70 and score < 90:
   print("Good ")
else:
   print("Needs improvement")

#Create a string with a sentence of your choice

sentence = "  Samir is a Software Developer.  "

print(sentence.upper())
print(sentence.strip())
print(sentence.replace("Developer", "Engineer"))
print(sentence.split())

#Build a text-based name generator that comvines random first and last names using string manipulation.

first_names = ["Samir", "Sam", "Sammy"]
last_names = ["Lander", "World", "Supremacy"]

import random

f_name = random.choice(first_names)
l_name = random.choice(last_names)
print(f"{f_name} {l_name}")