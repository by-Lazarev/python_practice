"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that
are not part of the primary diagonal.
"""

from test import *


def diagonalSum(mat: List[List[int]]) -> int:
    answer, n = 0, len(mat)

    for i in range(n//2):
        answer += sum([mat[i][i], mat[i][-1-i], mat[-1-i][i], mat[-1-i][-1-i]])
    return answer + (n % 2) * mat[n//2][n//2]
    # unoptimized
    n = len(mat)
    d1 = sum([mat[i][n - i - 1] for i in range(n)])
    d2 = sum([mat[i][i] for i in range(n)])
    result = d1 + d2 - mat[n//2][n//2] * (n % 2)
    return result


a = Solution()
a.diagonalSum = diagonalSum

check_result(a.diagonalSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 25)
