"""
Week 7 Lab 2:
Question 1: Python program for Membership Registration System
Author: Sukhjyot Singh Saini
"""

class WhitecliffeStudent():
    def __init__(self):
        self.studentID = int(input("Enter Student ID: "))
        self.lname = input("Enter Student Last Name:  ")
        self.program = input("Enter the Program(Diploma or Bachelor):")
        self.studentlist = [] #creates a new list
        self.membership_counter = 1000
        self.withdrawl_counter = 400
        self.register_counter = 600
        self.bachelor_students = 500
        self.diploma_students = 500

    def membership(self):
        #Add new student
        self.studentlist.append((self.lname, self.studentID, self.program))
        self.membership_counter += 1
        print(f"Hello {self.lname}! your membership ID is {self.membership_counter}")

        #Increment the appropriate program count
        if self.program.lower() == "bachelor":
            self.bachelor_students += 1
        elif self.program.lower() == "diploma":
            self.diploma_students += 1
        else:
            print("Invalid program selection. Please select a valid option.")


    def withdrawal(self):
        #Checks if the student in the list, remove if found
        student = (self.lname, self.studentID, self.program)
        if student in self.studentlist:
            self.studentlist.remove(student)
            self.withdrawl_counter += 1
            self.register_counter += 1
            print(f"Student {self.lname} has withdrwan their membership")
        else:
            print("Error. Student not found.")

    #Update program count
        if self.program.lower() == "bachelor":
            self.bachelor_students += 1
        elif self.program.lower() == "diploma":
            self.diploma_students += 1

    #Display update counts
        print(f"Registered Students: {self.register_counter}")
        print(f"Withdrawn Students: {self.withdrawl_counter}")

    
    def statistics(self):
        print(f"Number of Registered Students: {self.register_counter}")
        print(f"Students in Diploma Program: {self.diploma_students}")
        print(f"Students in Bachelor Program: {self.bachelor_students}")
        print(f"Number of withdrawn Students: {self.withdrawl_counter}")

def main():
    system = WhitecliffeStudent()
    while True:
        choice = input("\n 1. New Membership\n 2. Withdraw Membership\n 3. Statistics\n 4.Exit\n Choose an option: ")

        if choice == "1":
            system.membership()
        elif choice == "2":
            system.withdrawal()
        elif choice == "3":
            system.statistics()
        elif choice == "4":
            print("Exiting the membership system...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()





