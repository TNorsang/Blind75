# Heap

To sort numbers using heap sort it is fairly simple.

When you heapify a list of numbers, default is min heap, it bubbles up the
smallest number to the root and arranges nodes to nodes by making sure
the children nodes are smaller than it's parents. This is complete opposite for
max heap, where the largest value is at the root and the parents value have to be larger
than it's children.

## Min Heap (Default)

```
import heapq

numbers = [1,5,10,4,6,2,8]

sorted_numbers = []

heapq.heapify(numbers)

while numbers:
    min_num = heapq.heappop(numbers)
    sorted_numbers.append(min_num)

print(sorted_numbers)
```

## Max Heap

```
import heapq

numbers = [1,5,10,4,6,2,8]

negative_numbers = [-num for num in numbers]

sorted_numbers = []

while negative_numbers:
    max_num = -heapq.heappop(negative_numbers)
    sorted_numbers.append(max_num)

print(sorted_numbers)
```
