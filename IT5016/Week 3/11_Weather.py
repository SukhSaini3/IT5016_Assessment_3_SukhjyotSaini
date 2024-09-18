def what_to_wear(temperature):
    if temperature > 25:
        print("Wear shorts.")
    else:
        print("Not hot today!")
        print("Wear long pants.")
    print("Enjoy yourself!")

def main():
    what_to_wear(20)
    print()
    what_to_wear(30)

main()
