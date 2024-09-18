def function1(inches):
    inches_to_cm = inches * 2.54
    return inches_to_cm

def function2(cm):
    cm_to_inches = cm/2.54
    return cm_to_inches

inches = float(input("Enter inches: "))
cm = float(input("Enter CM: "))

print("Inches to CM: ",function1(inches))
print("CM to inches: ",function2(cm))

