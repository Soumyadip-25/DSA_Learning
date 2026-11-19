# Find the missing number in an array

n = int(input("Enter the value of N: "))

arr = []

for i in range(n - 1):
    num = int(input("Enter element: "))
    arr.append(num)

expected_sum = n * (n + 1) // 2

actual_sum = 0

for num in arr:
    actual_sum += num

missing = expected_sum - actual_sum

print("Missing number:", missing)