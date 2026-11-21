# Find the intersection of two arrays

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

intersection = []

for num in arr1:
    if num in arr2 and num not in intersection:
        intersection.append(num)

print("Intersection:", intersection)