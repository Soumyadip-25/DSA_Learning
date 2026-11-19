# Find the common elements in two arrays

n1 = int(input("Enter size of first array: "))

arr1 = []

for i in range(n1):
    num = int(input("Enter element: "))
    arr1.append(num)

n2 = int(input("Enter size of second array: "))

arr2 = []

for i in range(n2):
    num = int(input("Enter element: "))
    arr2.append(num)

common = []

for num in arr1:
    if num in arr2 and num not in common:
        common.append(num)

print("Common elements:", common)