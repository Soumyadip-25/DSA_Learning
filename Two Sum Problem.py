# Two Sum Problem

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

target = int(input("Enter target: "))

found = False

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == target:
            print("Indices:", i, j)
            found = True
            break

    if found:
        break

if not found:
    print("No pair found")