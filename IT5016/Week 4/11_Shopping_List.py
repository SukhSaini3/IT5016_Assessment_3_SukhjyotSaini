"""
Author: Sukhjyot Singh Saini
"""
def shopping():

    shopping_list = []
    total_price = 0 #Initial value to show that the data is empty
    while True: 
        item = input("Enter the name of the item(or type 'done' to finish)")
        if item.lower() == "done":
            break
        try:
            price = float(input(f"Enter the price of {item}: "))
            shopping_list.append((item,price))
            total_price += price

        except ValueError:
            print("Invalid input. Please enter a numeric value for the price")

    return shopping_list, total_price

def main():
    print("Welcome to the Shopping List Program!")
    shopping_list, total_price = shopping()

    if not shopping_list:
        print("No items were entered.")

    else:
        print("\n Shopping List:")
        for item,price in shopping_list:
            print(f"{item}: ${price: .2f}")
        print(f"\n Total Price: ${total_price: .2f}")



main()
