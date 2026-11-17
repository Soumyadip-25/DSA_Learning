# Check whether an array is sorted

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

sorted_array = True

for i in range(n - 1):
    if arr[i] > arr[i + 1]:
        sorted_array = False
        break

if sorted_array:
    print("Array is sorted")
else:
    print("Array is not sorted")