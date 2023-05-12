"""
You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from
question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi
points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to
make the decision on the next question.
"""

from test import *


def mostPoints(questions: List[List[int]]) -> int:
    n = len(questions)
    dp = [0] * n

    def dfs(i):
        if i >= n:
            return 0
        if dp[i]:
            return dp[i]
        points, skip = questions[i]

        dp[i] = max(dfs(i + 1), points + dfs(i + skip + 1))
        return dp[i]

    return dfs(0)


a = Solution()
a.mostPoints = mostPoints

check_result(a.mostPoints(
    [[21, 2], [1, 2], [12, 5], [7, 2], [35, 3], [32, 2], [80, 2], [91, 5], [92, 3], [27, 3], [19, 1], [37, 3], [85, 2],
     [33, 4], [25, 1], [91, 4], [44, 3], [93, 3], [65, 4], [82, 3], [85, 5], [81, 3], [29, 2], [25, 1], [74, 2],
     [58, 1], [85, 1], [84, 2], [27, 2], [47, 5], [48, 4], [3, 2], [44, 3], [60, 5], [19, 2], [9, 4], [29, 5], [15, 3],
     [1, 3], [60, 2], [63, 3], [79, 3], [19, 1], [7, 1], [35, 1], [55, 4], [1, 4], [41, 1], [58, 5]]), 781)
