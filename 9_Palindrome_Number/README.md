# 9. Palindrome Number (Python Solution)

[LeetCode Link](https://leetcode.com/problems/palindrome-number/)  
Difficulty: Easy  
Topics: Math

---

## Problem Description

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

A palindrome is a number that reads the same **backward as forward**.


---

## Approach

String Conversion:
   - Convert the integer to a string.
   - Check if it reads the same forward and backward.

---

## Python Code

```python
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        return s == s[::-1]
