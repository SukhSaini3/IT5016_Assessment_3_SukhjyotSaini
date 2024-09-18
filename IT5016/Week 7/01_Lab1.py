"""
Week 7 Lab 1
Question 2: Examine the code and assess where the software design principles are lacking
"""
class UnstructuredCode:
    def xyzzy(self,a,b):
        result = a+b
        print(f"Result: {result}")

class Calculator:
    def add(self,a,b):
        result = a+b
        print(f"Addition Result: {result}")

    def multiply(self,a,b):
        result = a*b
        print(f"Multiplication Result: {result}")

#class legacy_function(x,y): #first letter of class name should be capital. x and y cannot in such a way as 'legacy_function' is a class not a function.
    #r = x+y
    #print(f"Result: {r}")

class Legacy_function:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def sum(self):
        r = self.x + self.y
        print(f"Result: {r}")

class InflexibleShape:
    def calculate_area(self):
        pass

class Circle(InflexibleShape):
    def calculate_area(self):
        pass

class Square(InflexibleShape):
    def calculate_area(self):
        pass

#Main code
if __name__ == "__main__":
    obj = UnstructuredCode()
    #obj.xyz(5,10) # 'xyz' method does not exist. the correct method is 'xyzzy'
    obj.xyzzy(5,10) 

    calc = Calculator()
    calc.add(5,10)
    calc.multiply(5,10)

    #legacy_function(5,10) #legacy_function cannot be called without creating an instance
    legacy_function = Legacy_function(5,10)
    legacy_function.sum()

    circle = Circle()
    square = Square()

