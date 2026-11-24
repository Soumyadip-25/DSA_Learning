# Find the second smallest element in an array

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

smallest = float('inf')
second = float('inf')

for num in arr:

    if num < smallest:
        second = smallest
        smallest = num

    elif num < second and num != smallest:
        second = num

if second == float('inf'):
    print("Second smallest element does not exist")
else:
    print("Second smallest element:", second)