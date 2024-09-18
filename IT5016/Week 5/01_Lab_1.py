"""
Week 5 Lab Q1: Program for collecting user information
Author: Sukhjyot Singh Saini
"""

def collect_user_data(id_counter):
    print("Enter User Information:")
    username = input("Name: ")
    user_age = input("Age: ")
    user_email = input("Email Address: ")

    unique_id = id_counter + 1
    id_counter = unique_id

    print("User Information: ")
    print(f"Name: {username} ")
    print(f"Age: {user_age}")
    print(f"Email: {user_email}")
    print(f"Unique ID: {id_counter}")

    return username, user_age, user_email, id_counter

def main():
    id_counter = 5000
    id_counter, username, user_age, user_email = collect_user_data(id_counter)


main()
