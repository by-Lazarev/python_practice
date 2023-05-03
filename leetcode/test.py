from typing import List


class Solution:
    pass


def fail_print(func_result, clue):
    print(f"Function returned:\t{func_result}\nExpected result:\t{clue}")


def check_result(given, clue):
    if given != clue:
        fail_print(given, clue)
    else:
        print("Test_1 done!")
