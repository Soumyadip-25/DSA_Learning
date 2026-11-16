# Find the largest element in an array

n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest element:", largest)