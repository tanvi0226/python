# Task 1: Calculate Factorial Using a Function 

num= int(input("enter a number: "))
factorial= 1
for num in range (1, num +1):
    factorial *= num

print(f"Factorial of {num} is:", factorial)