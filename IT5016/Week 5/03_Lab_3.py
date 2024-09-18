"""
Week 5 Lab Q3: Program to categorize and provide a recomnmendation based on the total amount.
Author: Sukhjyot Singh Saini
"""

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
    
    print(f"Total Amount: ${total_amount: .2f}")
    return total_amount, items

def categorize_request(total_amount):
    
    if total_amount < 150:
        category = "Low"
        recommendation = "Proceed with standard processing"

    else:
        category = "High"
        recommendation = "Review for potential discounts"
        

    return category, recommendation

def main():
    
    total_amount, items = calculate_total_amount()
    category, recommendation = categorize_request(total_amount)

    #Display results

    print("Request Summary:")
    print(f"Total Amount ${total_amount:.2f}")
    print(f"Category: {category}")
    print(f"Recommendation: {recommendation}")

main()