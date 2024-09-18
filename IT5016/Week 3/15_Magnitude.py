"""
Week 3 Lab 
Question 1. The program reads the magnitude from the user and displays a meaningful message.
Author: Sukhjyot Singh
"""

def magnitude():
    magnitude= float(input("Please enter the magnitude of the earthquake: "))

    if(magnitude<2.0):
        print("The earthquake is Micro")

    elif(magnitude>2.0 and magnitude<3.0):
        print("The earthquake is Very Minor")

    elif(magnitude>3.0 and magnitude<4.0):
        print("The earthquake is Minor")
    
    elif(magnitude>4.0 and magnitude<5.0):
        print("The earthquake is Light")

    elif(magnitude>5.0 and magnitude<6.0):
        print("The earthquake is Moderate")

    elif(magnitude>6.0 and magnitude<7.0):
        print("The earthquake is Strong")
    
    elif(magnitude>7.0 and magnitude<8.0):
        print("The earthquake is Major")
    
    elif(magnitude>8.0 and magnitude<10.0):
        print("The earthquake is Great")

    else:
        print("The earthquake is Meteoric")

magnitude()



