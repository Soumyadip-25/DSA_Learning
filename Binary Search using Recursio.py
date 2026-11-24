# Implement Binary Search using Recursion

def binary_search(arr, low, high, target):

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return binary_search(arr, mid + 1, high, target)

    else:
        return binary_search(arr, low, mid - 1, target)


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element in sorted order: "))
    arr.append(num)

target = int(input("Enter element to search: "))

result = binary_search(arr, 0, n - 1, target)

if result == -1:
    print("Element not found")
else:
    print("Element found at index:", result)