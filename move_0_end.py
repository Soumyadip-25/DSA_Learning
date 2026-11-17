# Move all zeros to the end

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

result = []

for num in arr:
    if num != 0:
        result.append(num)

zeros = arr.count(0)

for i in range(zeros):
    result.append(0)

print("Updated array:", result)