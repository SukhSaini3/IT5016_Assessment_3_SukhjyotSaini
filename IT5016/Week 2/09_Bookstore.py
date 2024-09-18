"""
Program to calculate the total wholesale cost of book copies
Author: Sukhjyot Singh
"""

cover_price = float(input("Enter Cover Price: ")) #Enter the cover price
discount = float(input("Enter Bookstore Discount: ")) #Enter discount Value
total_copies = int(input("Enter Total Number of Copies: ")) #Enter total number of copies

bookstore_discount = cover_price - (cover_price * discount/100) #40% discount for bookstores
shipping_cost = 3 + (total_copies - 1) * 0.75 #Shipping cost on first copy is $3 and for following is 75 cents

wholesale_price = (bookstore_discount*total_copies) + shipping_cost #Total wholsesale price
print ("Total Wholesale Cost: $", wholesale_price, sep="")


