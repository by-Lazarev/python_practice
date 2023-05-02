"""
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
"""

from typing import List
from functools import reduce

def fail_print(func_result, clue):
    print(f"Function returned:\t{func_result}\nExpected result:\t{clue}")


class Solution:
    """
    best result
    """
    def arraySign(self, nums: List[int]) -> int:
        n_sign = 1
        for i in nums:
            if i == 0:
                return 0
            if i < 0:
                n_sign *= -1
        return n_sign
    """
    better result
    """
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        return 1 if reduce(int.__mul__, nums) > 0 else -1
    """
    unoptimized
    """
    def arraySign(self, nums: List[int]) -> int:
        result = reduce(int.__mul__, nums)
        if result == 0:
            return result
        return 1 if result > 0 else -1


a = Solution()

test_1 = a.arraySign([-1,-2,-3,-4,3,2,1])
test_1_clue = 1
print("test_1:")
if test_1 != test_1_clue:
    fail_print(test_1, test_1_clue)
else:
    print("\tdone!")
