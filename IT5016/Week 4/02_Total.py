"""
Author: Sukhjyot Singh Saini
"""
def total_user_numbers():
    total = 0
    number = int(input("Enter a number (0 to end): "))
    while number != 0:
        total += number
        number = int(input("Enter a number (0 to end): "))
    print("Total: ", total)

def main():
    total_user_numbers()

main()