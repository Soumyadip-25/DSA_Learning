# Find maximum and minimum using Divide and Conquer

def find_min_max(arr, low, high):

    if low == high:
        return arr[low], arr[low]

    if high == low + 1:

        if arr[low] < arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    mid = (low + high) // 2

    min1, max1 = find_min_max(arr, low, mid)

    min2, max2 = find_min_max(arr, mid + 1, high)

    minimum = min(min1, min2)
    maximum = max(max1, max2)

    return minimum, maximum


n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

if n == 0:
    print("Array is empty")
else:
    minimum, maximum = find_min_max(arr, 0, n - 1)

    print("Minimum element:", minimum)
    print("Maximum element:", maximum)