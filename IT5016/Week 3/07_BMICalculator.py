def function1(weight,height):
    bmi = weight / (height*0.01) ** 2
    return bmi

weight = float(input("Enter Weight(kg): "))
height = float(input("Enter Height (cm): "))

print(function1(weight,height))

