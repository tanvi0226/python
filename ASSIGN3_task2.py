#Task 2: Using the Math Module for Calculations.
import math 
num=float(input(" Enter a number:"))

if (num>0):
    print(f"Square root of {num} is:", num*num)
    print(f"Natural logarithm (log base e) of {num}is:", math.log(num))

else:
    print(f"square root of {num} is not defined")
    print(f"Natural logarithm (log base e) of {num} is not defined")

print(f"sin value of {num} is:", math.sin(num))