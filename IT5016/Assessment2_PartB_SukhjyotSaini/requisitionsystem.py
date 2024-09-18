"""
Assessment 2 Part B
Question: Create a python program for the Requisition system prototype.
Author: Sukhjyot Singh Saini
"""
class RequisitionSystem:
    def __init__(self):
        print("Enter Staff Information: ")
        self.date = input("Enter Date: ") #Inputs the date from the staff member
        self.staff_id = input("Enter Staff ID: ") #Inputs the staff member's ID
        self.name = input("Enter Staff Name: ") #Inputs the staff member's name
        self.unique_id = 10000 #Sets the unique ID counter to 10000
        self.total_requests = 30 #Sets the current number of total requests to 30
        self.approved_requests = 20 #Sets the current number of approved requests to 20
        self.pending_requests = 7 #Sets the current number of pending requests to 7
        self.not_approved_requests = 3 #Sets the current number of not approved requests to 3
        

    def staff_info(self):
        
        self.unique_id += 1 #Increments the ID counter by 1. (i.e. 10001,10002)
        self.requisition_id = str(self.unique_id) #Converts the unique ID counter to string

    def requisition_details(self):
        self.items = [] #Creates a new list 'self.items
        self.total_value = 0.0 #Sets the initial total value to 0.0

        print("Requisition Items Request (enter 'end' to calculate total value)")

        while True:
            input_items = input("Enter the requisition item with the price(e.g. ItemName $360): ") #Inputs items and price from staff
            if input_items.lower() == "end": #Converts the input into lowercase
                break #Breaks the function if the user types "end"
            try:
                self.item_name, self.price = input_items.rsplit(' ',1) #The rsplit() function splits and removes the item name written in the left side of the space(i.e. ' ').
                self.item_price = float(self.price.strip('$')) #The strip() function removes the '$' sign from the price value entered by the staff member.
                self.items.append((self.item_name, self.item_price)) #The append() function of the list will add the item name and the item price into the list 'items'
                self.total_value += self.item_price #Calculates the total value (i.e. total_value = total_value + item_price)

            except ValueError:
                print("Invalid input format. Please try again!") #Outputs error message if invalid price format is entered by the staff member.

        print(f"Total Value: ${self.total_value: .2f}") #Prints the total calculated value. '.2f' will only print two digits after the decimal.

    
    def requisition_approval(self):
        self.status = "Pending" #The current default status is set to 'Pending'
    
        if self.total_value < 500:
            self.status = "Approved" #Displays the status as 'Approved' if the requisition value is under $500.
            self.approved_requests += 1 #Increments the number of approved requests by 1.
            self.total_requests += 1 #Increments the number of total requests by 1.

        else:
            self.status = "Pending" #Displays the status as 'Pending' if the requisition value is $500 or higher.
            self.pending_requests += 1 #Increments the number of pending requests by 1.
            self.total_requests += 1 #Increments the number of total requests by 1.


    def respond_requisition(self):
        #If the currently pending requisition has a total value of more than $2000, then the manager can set the status of the requisiton as 'non approved'
        if self.total_value > 500 and self.total_value < 2000:
            self.status = "Pending"
            self.pending_requests += 1 #Increments the number of pending requests by 1.
            self.not_approved_requests -=1 #Decrements the number of not approved requests by 1.

        elif self.total_value > 2000:
            self.status = "Not Approved"
            self.not_approved_requests += 1 #Increments the number of not approved requests by 1.
            self.pending_requests -= 1 #Decrements the number of pending requests by 1.

    def display_requisitions(self):
        print("Printing Requisitions:")
        print(f"Date: {self.date}")
        print(f"Requisition ID: {self.unique_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.name}")
        print(f"Total: {self.total_value}")
        print(f"Status: {self.status}")
        if self.status == "Approved":
            print(f"Approval Reference Number: {self.staff_id}{self.requisition_id[2:]}")
        elif self.status == "Pending":
            print(f"Approval Reference Number: Not Available")
        elif self.status == "Not Approved":
            print(f"Approval Reference Number: Not Available")
        else:
            print("Error! Invalid value.")

    def requisition_statistic(self):
        print("Displaying the Requisition Statistics:")
        print(f"The total number of requisitions submitted: {self.total_requests}")
        print(f"The total number of approved requisitions: {self.approved_requests}")
        print(f"The total number of pending requisitions: {self.pending_requests}")
        print(f"The total number of not approved requisitions: {self.not_approved_requests}")

def menu():
    print("Staff Requisitions System:")
    print("1. New Requisition")
    print("2. Display Requisitions")
    print("3. Display Statistics")
    print("4. Exit System")

def main():
    system = RequisitionSystem() 

    while True:
        menu()
        choice = input("Enter Your Choice: ").strip()
        
        if choice == "1":
            system.staff_info()
            system.requisition_details()
            system.requisition_approval()
            system.respond_requisition()

        elif choice == "2":
            system.display_requisitions()
        
        elif choice == "3":
            system.requisition_statistic()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()






