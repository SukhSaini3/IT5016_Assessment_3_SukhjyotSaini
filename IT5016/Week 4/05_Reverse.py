"""
Author: Sukhjyot Singh Saini
"""
def reverse_string(s):
    reversed_str = " "
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

def main():
    original_string = input("Enter a string: ")
    reversed = reverse_string(original_string)
    print(f"Original String: {original_string}")
    print(f"Reversed String: {reversed}")

main()

