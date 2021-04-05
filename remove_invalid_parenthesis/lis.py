def lengthOfLIS(nums):

    tails = [0] * len(nums)
    size = 0

    for x in nums:
        i, j = 0, size
        while i <j:
            m = (i + j) / 2
            if tails[m] < x:
                i = m + 1
            else:
                j = m
        tails[i] = x
        size = max(i + 1, size)
        print(tails)
    return size

nums = [10,9,2,5,3,7,101,18]
results = lengthOfLIS(nums)
print(results)

nums = [0,1,0,3,2,3]
results = lengthOfLIS(nums)
print(results)