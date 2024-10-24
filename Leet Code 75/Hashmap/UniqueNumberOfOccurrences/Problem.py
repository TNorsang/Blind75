from collections import Counter
def uniqueOccurrences(arr):
    if len(arr) == 1:
        return True
    if len(arr) == 2 and arr[0] != arr[1]:
        return False
    elif len(arr) == 2 and arr[0] == arr[1]:
        return True
    counter = Counter(arr)

    freq_set = set()

    for key, value in counter.items():
        if value in freq_set:
            return False
        elif value not in freq_set:
            freq_set.add(value)
    return True