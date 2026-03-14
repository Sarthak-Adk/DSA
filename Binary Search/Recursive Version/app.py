def binary_search_recursive(arr, target, left, right):

    if left > right:
        return -1 

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


numbers = [2, 4, 6, 8, 10, 12, 14]

result = binary_search_recursive(numbers, 10, 0, len(numbers)-1)

print("Element found at index:", result)