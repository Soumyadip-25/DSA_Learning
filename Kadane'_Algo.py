# Find the maximum subarray sum (Kadane's Algorithm)
# Find the maximum possible sum of a continuous subarray.

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

if n == 0:
    print("Array is empty")
else:
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1, n):

        current_sum = max(arr[i], current_sum + arr[i])

        max_sum = max(max_sum, current_sum)

    print("Maximum subarray sum:", max_sum)