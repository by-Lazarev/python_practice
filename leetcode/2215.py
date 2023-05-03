'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
'''

from test import *
from itertools import zip_longest


def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    # best results
    result1, result2 = set(nums1), set(nums2)
    return list(map(list, [result1.difference(result2), result2.difference(result1)]))
    # unoptimized
    result = [set(), set()]
    for first, second in zip_longest(nums1, nums2):
        if first is not None and first not in nums2:
            result[0].add(first)
        if second is not None and second not in nums1:
            result[1].add(second)
    return [list(result[0]), list(result[1])]


a = Solution()
a.findDifference = findDifference

check_result(a.findDifference([1, 2, 3], [2, 4, 6]), [[1, 3], [4, 6]])
