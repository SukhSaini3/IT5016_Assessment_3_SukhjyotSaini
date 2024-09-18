"""
Week 3 Lab 
Question 5. The program generates a username for the student based on the input.
Author: Sukhjyot Singh
"""

def username():
    student_id = (input("Enter your Student ID: "))
    first_name = (input("Enter you First Name: "))
    last_name = (input("Enter you Last Name: "))
    university = (input("Which university do you attend?"))

    if(university == "whitecliffe college"):
        print(f"Welcome to Whitecliffe College! Your username is {student_id}{last_name[3:]}")

    else:
        print("Please have your university generate your name")

username()
