# Kth Largest Element in an Array

At first to find the Kth largest element in an array without sorting using heap works.
However to find the Kth largest, it invovles using max heap approach, which is simply negative the elements in nums and grabbing the values by iterating K times.

```
if not nums:
    return None
if len(nums) == 1 and k == 1:
    return nums[0]

negative_array = [element * -1 for element in nums]

heapq.heapify(negative_array)
largest_k = 0

for _ in range(k):
    largest_k = heappop(negative_array)
return largest_k * -1
```

Then I found a faster approach by storing the first K elements from nums, heapify it, then iterate through the array form k to end of array and compare each element with the smallest element in the Kth element array. If smaller ignore and iterate to the next value in nums, if larger replace it by using heapreplace(arr, num) this will replace the value and re-heapify the arr.

```
min_heap = nums[:k]
heapq.heapify(min_heap)

for num in nums[k:]:
    if num > min_heap[0]:
        heapq.heapreplace(min_heap, num)
return min_heap[0]
```
