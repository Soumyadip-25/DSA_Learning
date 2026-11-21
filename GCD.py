# Find the GCD of two numbers
# GCD (Greatest Common Divisor) is the largest number that divides two numbers exactly.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    remainder = a % b
    a = b
    b = remainder

print("GCD:", abs(a))