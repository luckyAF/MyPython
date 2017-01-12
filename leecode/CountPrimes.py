import math
def countPrimes(n):
    """
    求素数
    """
    if n <= 2:
        return 0

    nums = [ i for i in range(2,n)]
    i = 0
    j = 0
    keyNum = 0
    while i < len(nums) and keyNum <= math.sqrt(n):
        keyNum = nums[i]
        j = i + 1
        while j < len(nums):
            if nums[j] % keyNum == 0:
                nums.pop(j)
            else:
                j = j + 1
        i = i + 1
    print(n)
    print(len(nums)) 
def countPrimes2(n):
    if n <= 2:
        return 0
    sum = 0 
    nums = [None] * (n + 1)
    for i in range(2,int(math.sqrt(n))+1):
        for j in range(i+1,n +1):
            if j % i == 0:
                nums[j] = -1
    for i in range(2,n):
        if nums[i] == None:
            sum += 1
    print(n)       
    print(sum)


for i in range(1,10):
    countPrimes2(i)