"""
Week 5 Lab Q4 : Program to provide a detailed report
Author: Sukhjyot Singh Saini
"""

#Program 1
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

#Program 2
def calculate_total_amount():
    items = []
    total_amount = 0.0

    print("Enter Item Details (Type 'finish' to end):")
    while True:
        item_input = input("Item Name and Price (e.g., Cables $200): ")
        if item_input.lower() == 'finish':
            break
        try: 
            item_name, price_str = item_input.rsplit(' ', 1)
            item_price = float(price_str.strip('$')) #Remove the '$' and convert to float
            items.append((item_name, item_price))
            total_amount += item_price

        except ValueError:
            print("Invalid price format. Please enter the price in the correct format.")
    
    
    return total_amount, items

#Program 3
def categorize_request(total_amount):
    
    if total_amount < 150:
        category = "Low"
        recommendation = "Proceed with standard processing"

    else:
        category = "High"
        recommendation = "Review for potential discounts"
        

    return category, recommendation

#Program 4
def create_detailed_report(id_counter, username, user_age, user_email, total_amount, category, recommendation):
     print("Detailed Report ")
     print(f"Unique ID: {id_counter}")
     print(f"Username: {username} ")
     print(f"Age: {user_age}")
     print(f"Email: {user_email}")
     print(f"Total Amount: ${total_amount: .2f}")
     print(f"Category: {category}")
     print(f"Recommendation: {recommendation}")

  

def main():
    id_counter = 5000
    id_counter,username,user_age, user_email= collect_user_data(id_counter)
    total_amount, items = calculate_total_amount()
    category, recommendation = categorize_request(total_amount)
    create_detailed_report(id_counter,username, user_age, user_email, total_amount, category, recommendation)

main()