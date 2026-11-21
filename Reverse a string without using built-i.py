# Reverse a string without using built-in functions

s = input("Enter a string: ")

reverse = ""

for char in s:
    reverse = char + reverse

print("Reversed string:", reverse)