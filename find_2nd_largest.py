# Find the second largest element in an array

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

largest = second = float('-inf')

for num in arr:
    if num > largest:
        second = largest
        largest = num

    elif num > second and num != largest:
        second = num

if second == float('-inf'):
    print("Second largest element does not exist")
else:
    print("Second largest element:", second)