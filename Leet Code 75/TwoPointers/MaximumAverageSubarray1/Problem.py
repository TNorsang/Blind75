def findMaxAverage(nums,k):
    if not nums:
        return 0
    if k == 0:
        return 0
    if len(nums) == 1 and k == 1:
        return nums[0]
    elif len(nums) == 1 and k > 1:
        return 0
    total_sum = 0
    for i in range(k):
        total_sum += nums[i]  

    max_avg = total_sum / k

    for i in range(k,len(nums)):
        total_sum += nums[i]
        total_sum -= nums[i-k]
        current_avg = total_sum / k
        max_avg = max(max_avg,current_avg)

    return max_avg

print(findMaxAverage([5],1))