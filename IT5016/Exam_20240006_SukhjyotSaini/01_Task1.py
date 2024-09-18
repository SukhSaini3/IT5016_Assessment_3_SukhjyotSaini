"""
Exam Task 1: Program to collect staff members information 
Author: Sukhjyot Singh Saini
"""
def staff_info(requisition_id):
    print("Enter Staff Information:")
    date = input("Enter Date: ") #Inputs the date from the staff member.
    staff_id = input("Enter Staff ID: ") #Inputs the staff member's staff ID.
    staff_name = input("Enter Staff Name: ") #Inputs the staff member's name

    unique_id = requisition_id + 1 #The variable 'unique_id' will increment the current requisition ID (i.e. 10000) by 1.
    requisition_id = unique_id #The variable 'requisition_id' will read the incremented value as its input from 'unique_id' variable.

    print(f"Printing Staff Information: ")
    print(f"Date: {date}") #Outputs the date entered by the staff member.
    print(f"Staff ID: {staff_id}") #Outputs the staff ID entered by the staff member.
    print(f"Staff Name: {staff_name}") #Outputs the staff name entered by the staff member.
    print(f"Requisition ID: {requisition_id}") #Outputs the generated and incremented value (i.e. 10001).

    return date, staff_id, staff_name, requisition_id 

def main():
    requisition_id = 10000 #States the current value for the requisition id (i.e. 10000).
    date, staff_id, staff_name, requisition_id = staff_info(requisition_id) #Calls the variables from the 'staff_info' function.

main()




