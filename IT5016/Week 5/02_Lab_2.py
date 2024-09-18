"""
Week 5 Lab Q2: Program for summing up prices
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

calculate_total_amount()
