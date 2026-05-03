"""
1. Write a Python program to read an entire text file.
"""

"""
with open("filex.txt","r") as f:
    data = f.read()
    print(data)
"""

"""
2. Write a Python program to read first n lines of a file.
"""
"""
def display_n_lines(n):
    with open("filex.txt","r") as f:
        data = f.readlines()
    for i in range(n + 1):
        print(data[i])

display_n_lines(1)
"""

### something is wrong

"""
3. Write a Python program to append text to a file and display the text.
"""
"""
with open("filex.txt","a") as f:
    f.write("\n we can do it")
"""
    

### don't know how to display append things

"""
4. Write a Python program to read last n lines of a file.
"""


def display_n_lines(n):
    with open("filex.txt","r") as f:
        data = f.readlines()
    for i in range(n + 1):
        print(data[-i])

display_n_lines(0)

"""
5. Write a Python program to read a file line by line and store it into a list.
"""
with open("filex.txt","r") as f:
        data = f.readlines()
        print(data)

"""
6. Write a Python program to read a file line by line store it into a variable.
"""
with open("filex.txt","r") as f:
        data = f.read()
        print(data)

"""
7. Write a python program to find the longest words.
"""
def longestword(file):
    with open(file,"r") as f:
        data = f.read()
        words = data.split()
        longest = max(words,key=len)
    return longest

print(longestword("filex.txt"))

"""
8. Write a Python program to count the number of lines in a text file.
"""
with open("filex.txt","r") as f:
        data = f.readlines()
        print(len(data))

"""
9. Write a Python program to count the frequency of words in a file.
"""
#for single words
with open("filex.txt","r") as f:
        data = f.read()
        print(data.count("can"))

#for each word that is there in the file : it prints out a dictinory inside counter()
from collections import Counter

with open("filex.txt", "r") as f:
    words = f.read().split()

freq = Counter(words)
print(freq)

"""
10. Write a Python program to get the file size of a plain file.
"""
import os

size = os.path.getsize("filex.txt")
print(size) 
        
"""
11. Write a Python program to write a list to a file.
"""

def listwritentofile(listobewritten):
    with open("filex.txt","a") as f:
        for i in listobewritten:
            f.write(f"\n {i}")
    return listobewritten

print(listwritentofile(["hello bro","what's going on","what the hell"]))

"""
12. Write a Python program to copy the contents of a file to another file .


def copyfile(file1,file2):
    with open(file1,"r") as f1:
        data = f1.read()
    with open(file2,"w") as f2:
        f2.write(data)
    return data

print(copyfile("filex.txt","filey.txt"))
"""

"""
13. Write a Python program to read a random line from a file.
"""
import random
def randomline(file):
    with open(file,"r") as f:
        data = f.readlines()
    return random.choice(data)

print(randomline("filex.txt"))

"""
14. Write a Python program to assess if a file is closed or not.
"""

with open("filex.txt","r") as f:
    print(f.closed)

"""
15.Write a Python program that takes a text file as input and returns the number of words of a given text file.
"""

with open("filex.txt","r") as f:
    data = f.read()
    words = data.split()
    print(len(words))





