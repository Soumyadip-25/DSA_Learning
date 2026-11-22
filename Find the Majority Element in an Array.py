# Find the Majority Element in an Array
# Find the element that appears more than n/2 times.

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

count = 0
candidate = None

for num in arr:

    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1

frequency = 0

for num in arr:
    if num == candidate:
        frequency += 1

if frequency > n // 2:
    print("Majority element:", candidate)
else:
    print("No majority element exists")