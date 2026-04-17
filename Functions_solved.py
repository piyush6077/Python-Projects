"""
1. Write a Python function to find the maximum of three numbers.
"""

def maxNum(a,b,c):
    return max(a,b,c)

print(maxNum(5,4,6))

"""
2. Write a Python function to sum all the numbers in a list.

	Sample List : (8, 2, 3, 0, 7)
	Expected Output : 20
"""

def sumOflist(newList):
    a = 0
    for i in newList:
        a = a + i
    return a 

print(sumOflist([8, 2, 3, 0, 7]))


"""
3. Write a Python function to multiply all the numbers in a list.

	Sample List : (8, 2, 3, -1, 7)
	Expected Output : -336
"""

def multiOflist(newList):
    a = 1
    for i in newList:
        a = a * i
    return a 

print(multiOflist([8, 2, 3, -1, 7]))


"""
4. Write a Python function to reverse a string. 

	Sample String : "1234abcd"
	Expected Output : "dcba4321"
"""

def reverseString(string):
    return string[::-1]

print(reverseString("1234abcd"))


"""
5. Write a Python function to check whether a number falls within a given range.
"""

def checkTheRange(a,b,n):
    if n in range(a,b):
        return True
    else:
        return False
    
print(checkTheRange(1,10,4))


"""
6. Write a Python function that accepts a string and counts the number of upper and lower case letters.
	Sample String : 'The quick Brow Fox'
	Expected Output :
	No. of Upper case characters : 3
	No. of Lower case Characters : 12
"""

def checkUpLowerLetter(newString):
    l = 0
    u = 0
    for i in newString:
        if i.islower():
            l = l + 1
        elif i.isupper(): 
            u = u + 1
    
    print(f"No. of Upper case characters : {u}")
    print(f"No. of Lower case Characters : {l}")

checkUpLowerLetter('The quick Brow Fox')


"""
7. Write a Python function that takes a list and returns a new list with distinct elements from the first list.

	Sample List : [1,2,3,3,3,3,4,5]
	Unique List : [1, 2, 3, 4, 5]
"""

def uniqueList(newlist):
    return list(set(newlist))

print(uniqueList([1,2,3,3,3,3,4,5]))

"""
8. Write a Python function that checks whether a passed string is a palindrome or not.

	Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
"""

def isPalindrome(str):
    return str == str[::-1]

print(isPalindrome("abba"))
print(isPalindrome("madam"))
print(isPalindrome("nurse"))


"""
9. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

	Sample Items : green-red-yellow-black-white
	Expected Result : black-green-red-white-yellow
"""

def alpaCheck(newString):
    l = newString.split("-")
    l.sort()
    return '-'.join(l)

print(alpaCheck("green-red-yellow-black-white"))

"""
10. Write a Python program to detect the number of local variables declared in a function.
"""

def localVar():
    a = 1
    b = 2
    c = 3
    return len(locals())

print(localVar())


"""
11. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

	Sample Output:
	25
	48
"""

a = lambda x:x + 15
b = lambda x,y:x + y

print(a(10),b(10,28))

"""
12. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.

	Sample Output:
	Double the number of 15 = 30
	Triple the number of 15 = 45
	Quadruple the number of 15 = 60
	Quintuple the number 15 = 75
"""
def multiNum(n):
    print(f"Double the number of {n} = {n*2}")
    print(f"Triple the number of {n} = {n*3}")
    print(f"Quadruple the number of {n} = {n*4}")
    print(f"Quintuple the number of {n} = {n*5}")

multiNum(15)

"""
13. Write a Python program to sort a list of tuples using Lambda.

	Original list of tuples:
	[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
	Sorting the List of Tuples:
	[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
"""

l = lambda x: x.sort()
givenlist = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print(givenlist)


"""
14. Write a Python program to sort a list of dictionaries using Lambda.

	Original list of dictionaries :
	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
	Sorting the List of dictionaries :
	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
"""
givenDictlist = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

givenDictlist.sort(key = lambda x:x['color'] )
print(givenDictlist)

"""
15. Write a Python program to filter a list of integers using Lambda.

	Original list of integers:
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	Even numbers from the said list:
	[2, 4, 6, 8, 10]
	Odd numbers from the said list:
	[1, 3, 5, 7, 9]	
"""

oglist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evenList = filter(lambda x: x%2 == 0,oglist)
oddList = filter(lambda x: x%2 != 0,oglist)
print(list(evenList))
print(list(oddList))

"""
16. Write a Python program to square and cube every number in a given list of integers using Lambda.

	Original list of integers:
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	Square every number of the said list:
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	Cube every number of the said list:
	[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
"""

oglist2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squareLi = map(lambda x: x**2 , oglist2)
cubeLi = map(lambda y: y**3 , oglist2)

print(list(squareLi))
print(list(cubeLi))

"""
18. Write a Python program to find if a given string starts with a given character using Lambda.
"""	

givenString = "Hello World"
givenChar = "H"

checkString = lambda x: True if givenString.startswith(givenChar) else False
print(checkString(givenString))

"""
19. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.

	Original arrays:
	[-1, 2, -3, 5, 7, 8, 9, -10]
	Rearrange positive and negative numbers of the said array:
	[2, 5, 7, 8, 9, -10, -3, -1]
"""

givenArray = [-1, 2, -3, 5, 7, 8, 9, -10]
givenArray.sort(key = lambda x: (x < 0, x))
print(givenArray)


"""
20. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.

	Original arrays:
	[1, 2, 3, 5, 7, 8, 9, 10]
	Number of even numbers in the above array: 3
	Number of odd numbers in the above array: 5
"""
oglist3 = [1, 2, 3, 5, 7, 8, 9, 10]
evenList = len(list(filter(lambda x: x%2 == 0,oglist3)))
oddList = len(list(filter(lambda x: x%2 != 0,oglist3)))
print(f"Number of even numbers in the above array: {evenList}") 
print(f"Number of odd numbers in the above array: {oddList}")

"""
21. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.

	Orginal list:
	[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
	Numbers of the above list divisible by nineteen or thirteen:
	[19, 65, 57, 39, 152, 190]
"""
oglist4 = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
result5 = filter(lambda x: x%19 == 0 or x%13 == 0 , oglist4)
print(list(result5))

"""
22. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda.
"""
givenString2 = "Hisdjfnsykjsf1245"
checkStringType = lambda x: True if any(i.isupper() for i in givenString2) and any(j.islower() for j in givenString2) and any(k.isdigit() for k in givenString2) and len(givenString2) >= 8 else False
print(checkStringType(givenString2))
