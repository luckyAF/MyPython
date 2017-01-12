def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    knums = {}
    rnums = []
    for i in num:
        if i in knums:
            knums[i] = knums[i] + 1
        else :
            knums[i] = 0
    index = 0
    for i in range(k):
        max = -1
        for (k,m) in knums.items():
            if m > max:
                index = k
                max = m
        rnums.insert(index)
        knums[index] = -1
    return rnums
