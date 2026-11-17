Remove duplicate elements from an array

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

new_arr = []

for num in arr:
    if num not in new_arr:
        new_arr.append(num)

print("Array after removing duplicates:", new_arr)