# Rotate an array by K positions

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

k = int(input("Enter rotation value: "))

if n > 0:
    k = k % n

    rotated = arr[-k:] + arr[:-k]

    print("Rotated array:", rotated)
else:
    print("Array is empty")