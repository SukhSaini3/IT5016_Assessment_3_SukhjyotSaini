def function3(name):
    first = name[0]
    last = name[len(name)-1]
    combined = last+first
    return combined.upper()

name = input("Enter Name: ")
print(function3(name))
