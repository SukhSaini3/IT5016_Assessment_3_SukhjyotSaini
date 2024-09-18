"""
Week 3 Lab 
Question 3. The program asks the user input two values and select a function for the values.
Author: Sukhjyot Singh
"""

def arithmetic():
    value1 = float(input("Enter First Value: "))
    value2 = float(input("Enter Second Value: "))

    print(f"""
          Select a function to apply on the values:
          a. Addition
          b. Subtraction
          c. Division
          d. Multiplication
          """)
    
    select = (input("Enter the function you want to select: "))

    if(select == "a"):
        print(f"{value1} + {value2} = ", value1+value2)
    
    elif(select == "b"):
        print(f"{value1} - {value2} = ", value1-value2)

    elif(select == "c"):
        print(f"{value1} / {value2} = ", value1 / value2)

    elif(select == "d"):
        print(f"{value1} * {value2} = ", value1 * value2)

    else:
        print("Incorrect Selection")

arithmetic()

