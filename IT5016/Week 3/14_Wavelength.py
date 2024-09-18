"""
Week 3 Lab 
Question 2. The program calculates if the value is between the wavelength of the visible range and reports the color.
Author: Sukhjyot Singh
"""

def light_wavelength():
    wavelength = int(input("Enter Wavelength Value: "))

    if (wavelength>=380 and wavelength<450):
        print(f"Thank you, the wavelength that you entered in nanometers is {wavelength}. The color for this wavelength is Violet")

    elif(wavelength>=450 and wavelength<495):
        print(f"Thank you, the wavelength that you entered in nanometers is {wavelength}. The color for this wavelength is Blue")
    
    elif(wavelength>=495 and wavelength<570):
        print(f"Thank you, the wavelength that you entered in nanometers is {wavelength}. The color for this wavelength is Green")
    
    elif(wavelength>=570 and wavelength<590):
        print(f"Thank you, the wavelength that you entered in nanometers is {wavelength}. The color for this wavelength is Yellow")

    elif(wavelength>=590 and wavelength<620):
        print(f"Thank you, the wavelength that you entered in nanometers is {wavelength}. The color for this wavelength is Orange")
    
    elif(wavelength>=620 and wavelength==750):
        print(f"Thank you, the wavelength that you entered in nanometers is {wavelength}. The color for this wavelength is Red")

    else:
        print("The wavelength is out of range")

light_wavelength()

