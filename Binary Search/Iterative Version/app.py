def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) 

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


numbers = [1, 3, 5, 7, 9, 11, 13]
result = binary_search(numbers, 7)

print("Element found at index:", result)