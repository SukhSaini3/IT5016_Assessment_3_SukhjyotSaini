"""
Week 2 Lab
Question 2

Author: Sukhjyot Singh
"""

a = 42
b = 3.14
c = "Hello, World!"
d = [1, 2, 3]
e = (1, 2, 3)
f = {"name": "Sukh","age":30}

#a. Types of each variable

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

#b. Converting the content of variable "b" to str

b_str = str(b)
print(b_str) #"3.14"

#c. Calculating exponential value of b

import math 
print("Exponential Value of 'b' is: ", math.exp(b)) #Calculates the exponential value of 'b'


#d. "a" modulus "b"

mod = a%b
print("a % b is:",mod)


#e. Apply Assighnment operators on "a"

a+=5  #Increases the value of 'a' by 5
print("a+=5 is:",a)
a-=10 #Decreases the value of 'a' by 10
print("a-=10 is:",a)
a*=2  #Multiplies the value of 'a' by 2
print("a*=2 is:",a)
a/=7  #Divides the value of 'a' by 7
print("a/=7 is:",a)

#f. Convert 'c' to uppercase

uppercase = c.upper()

print(" 'c' as uppercase:", uppercase)

#g. Convert 'a' and 'b' to str and then concanate them

a = "42"   #Converts 'a' into string variable type
b = "3.14" #Converts 'b' into string variable type

concanate = a+b
print("Concanated Value of 'a' abd 'b' is: ", concanate)

#h. Reverse the content of variable 'c'

reverse = c[::-1] #"::" will omit the start and stop point and will cover the entire string, -1 will read the string backwards
print("Reversed Value: ", reverse)
