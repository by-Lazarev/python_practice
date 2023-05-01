"""
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary.
Answers within 10-5 of the actual answer will be accepted.
"""
from typing import List


def fail_print(func_result, clue):
    print(f"Function returned:\t{func_result}\nExpected result:\t{clue}")


class Solution:
    def average(self, salary: List[int]) -> float:
        return sum(sorted(salary)[1:-1]) / (len(salary) - 2)


a = Solution()

test_1 = a.average([4000, 3000, 1000, 2000])
test_1_clue = 2500.00000
if test_1 != test_1_clue:
    fail_print(test_1, test_1_clue)
else:
    print("Test_1 done!")