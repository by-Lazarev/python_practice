"""
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
"""

from test import *
from functools import lru_cache


def maxVowels(s: str, k: int) -> int:
    ltrs = set("aeiou")
    ans = sum([i in ltrs for i in s[: k]])

    for i in range(k, len(s)):
        if ans >= k:
            return k
        if s[i] in ltrs:
            ans += 1
        if s[i - k] in ltrs:
            ans -= 1
    return ans


a = Solution()
a.maxVowels = maxVowels

check_result(a.maxVowels("weallloveyou", 7), 4)
