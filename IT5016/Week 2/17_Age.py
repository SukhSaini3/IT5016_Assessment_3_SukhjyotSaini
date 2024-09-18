"""
Week 2 Lab
Question 1
Program to calculate the age of a person based on their year of birth
"""


name = str(input("Enter your Name: "))
year = int(input("Enter your Year of Birth: "))
current_year = int(input("Enter the Current Year: "))
age = current_year - year

print ("Hello",name, ", you are now",age, "years old. Wow!!!")
