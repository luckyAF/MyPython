def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    ones,twos=0,0
    for ele in nums:
        ones = ones^ele & ~twos
        twos = twos^ele & ~ones
    return ones
        

Nums =[3,2,3,3]
singleNumber(Nums)