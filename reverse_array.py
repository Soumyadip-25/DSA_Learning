# Reverse an array

n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

# Reverse the array
reversed_arr = []

for i in range(n - 1, -1, -1):
    reversed_arr.append(arr[i])

print("Original Array:", arr)
print("Reversed Array:", reversed_arr)