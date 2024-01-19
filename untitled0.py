# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w0ZZSmlx9W36U8tUwOeUrwRnFBUoPfpd
"""

# method to print full name by combining firstname and lastname
def full__Name(fName, lName):
    Full_name = first__Name + " " + last__Name
    print("Your full name is ", Full_name)

# method to print alternative characters of a string
def string_alternative(str):
    print("Alternative characters are " + str[::2])

if __name__ == "__main__":
    first__Name = input("Enter your first Name: ")
    last__Name = input("Enter your last Name: ")
    full__Name(first__Name, last__Name)
    str = input("Enter a string to print alternate characters: ")
    string_alternative(str)

f = open("testinput.txt","w")
f.write("Python Course\n")
f.write("Deep learning Course\n")
f.close()
f= open("testinput.txt","r")
print(f.read())
from collections import Counter

# Reading input from input.txt
with open('testinput.txt', 'r') as file:
    lines = file.readlines()

# Processing each line and count words
wordcountperline = []

for line in lines:
    words = line.strip().split()
    wordcountperline.append(Counter(words))

# Printing the lines
for line in lines:
    print(line.strip())

# Printing word counts for each word
print("Word_Count:")
for word, count in Counter(word for wc in wordcountperline for word in wc).items():
    print(f"{word}: {count}")

# Storing the output in output.txt
with open('testoutput.txt', 'w') as output_file:
    for line in lines:
        output_file.write(line)
    output_file.write("Word_Count:\n")
    for word, count in Counter(word for wc in wordcountperline for word in wc).items():
        output_file.write(f"{word}: {count}\n")

# below code snippet is the conversion of heights from inches to cms
# using Nested Interactive loop & List comprehensions
heights_List = []
elements = int(input("Enter size of list: "))
for e in range(elements):
    heights_List.append(float(input()))
tempHeights_List = [2.54 * item for item in heights_List]
print(tempHeights_List)