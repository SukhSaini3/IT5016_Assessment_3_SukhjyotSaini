#item1 = 10
#item2 = 20
#item3 = 30

item1 = float(input("Enter the price for item1: "))
item2 = float(input("Enter the price for item2: "))
item3 = float(input("Enter the price for item3: "))

SubTotal = item1+item2+item3

SalesTax = SubTotal*0.15

Total = SubTotal+SalesTax



print("Subtotal: $", SubTotal, sep="")
print("SalesTax: $", SalesTax, sep="")
print("Total: $", Total, sep="")

