# 28. Find the Index of the First Occurrence in a String

LeetCode Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/  
Difficulty: Easy  
Topics: String, Two Pointers, String Matching

## Problem Description

Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.
 

## Approach

This solution uses a basic brute-force method to find the first matching position of `needle` in `haystack` without using any built-in functions like `find()`.

1. Calculate the lengths of `haystack` (n) and `needle` (m).
2. If `needle` is empty, return 0.
3. Loop through each possible starting index `i` in `haystack` (up to `n - m`)
4. For each index `i`, check character by character whether `needle` matches
5. If all characters match, return the starting index `i`
6. If no match is found after all iterations, return -1

## Python Code

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)

        if m == 0:
            return 0
        
        for i in range(n - m + 1):
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    break
                if j == m - 1:
                    return i
        return -1
