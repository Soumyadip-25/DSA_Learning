# CHeck whether a given string is palindrome or not

s = input("Enter a string: ")

reverse = ""

for char in s:
    reverse = char + reverse

if s == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")