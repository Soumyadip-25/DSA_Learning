# Binary Search

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

search = int(input("Enter element to search: "))

low = 0
high = n - 1

found = False

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == search:
        print("Element found at index:", mid)
        found = True
        break

    elif arr[mid] < search:
        low = mid + 1

    else:
        high = mid - 1

if not found:
    print("Element not found")