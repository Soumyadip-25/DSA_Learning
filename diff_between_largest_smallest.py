# Find the difference between the largest and smallest elements

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

largest = arr[0]
smallest = arr[0]

for num in arr:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

difference = largest - smallest

print("Difference:", difference)