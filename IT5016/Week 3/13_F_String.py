name = input("Enter your name: ")
age = input("Enter yout age: ")
print("Hello,",name,".You are",age,"years old", sep="")

#f string
print(f"Hello, {name} . You are {age} years old.")

pi = 3.141592653589793
print(pi)
formatted_pi = f"Value of pi to 2 decimel places: {pi: .3f}"
print(formatted_pi)

salary = float(input("Enter your weekly salary:"))
print(f"Your weekly salary is ${salary: .3f}")

a = 10
b = 5
result = f"The result of {a} multiplied by {b} is {a*b}"
print(result)

name = "Sukh"
age = 20
address = "136 Queen St."
info = f"""
Name: {name}
Age: {age}
Address: {address}
"""

print(info)