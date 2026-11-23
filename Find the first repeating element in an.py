# Find the first repeating element in an array
# Find the first element that appears more than once, based on its first occurrence in the array.

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

seen = set()
found = False

for num in arr:

    if num in seen:
        print("First repeating element:", num)
        found = True
        break

    seen.add(num)

if not found:
    print("No repeating element found")