# Find the index of an element

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

search = int(input("Enter element to find: "))

index = -1

for i in range(n):
    if arr[i] == search:
        index = i
        break

if index != -1:
    print("Index:", index)
else:
    print("Element not found")