def binary_search(target,arr):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = right - left // 2
        if arr[mid] == target:
            return f"Target found at position {mid+1}"
        if arr[mid] > target:
            right = mid - 1
        if arr[mid] < target:
            left = mid + 1
    return "Target Not Found"

print(binary_search(0,[0,1,2,3,4,5,6]))