# Search for an element in an array (Linear Search)

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

search = int(input("Enter element to search: "))

found = False

for i in range(n):
    if arr[i] == search:
        print("Element found at index:", i)
        found = True
        break

if found == False:
    print("Element not found")