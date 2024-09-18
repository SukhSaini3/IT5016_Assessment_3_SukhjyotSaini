"""
Exam Task 2: Program to collect staff members information and ask the staff to input requisition items and then print the total amount.
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

def requisitions_total():
    items = [] #Creates a new empty list for the variable 'items'.
    total_value = 0.0 #Defines the current total value.

    print("Requisition Items Request (enter 'end' to calculate total value): ")

    while True:
        input_items = input("Enter the requisition item with the price (e.g. ItemName $300): ") #Inputs the item name and price from the staff member.
        if input_items.lower() == "end": #Converts the user input 'end' to lowercase from any written format.
            break #Will break the code if the user inputs 'end'
        try:
            item_name, price = input_items.rsplit(' ',1) #The rsplit() function splits and removes the item name written in the left side of the space(i.e. ' ').
            item_price = float(price.strip('$')) #The strip() function removes the '$' sign from the price value entered by the staff member.
            items.append((item_name, item_price)) #The append() function of the list will add the item name and the item price into the list 'items'
            total_value += item_price #Calculates the total value (i.e. total_value = total_value + item_price)

        except ValueError:
            print("Invalid input format. Please try again!") #Outputs error message if invalid price format is entered by the staff member.

    print(f"Total Value:${total_value: .2f}") #Prints the total calculated value. '.2f' will only print two digits after the decimal.
    return total_value, items

def main():
    requisition_id = 10000
    date, staff_id, staff_name, requisition_id = staff_info(requisition_id)
    total_value, items = requisitions_total()

main()


