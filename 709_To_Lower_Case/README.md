# 709. To Lower Case

LeetCode Link: https://leetcode.com/problems/to-lower-case/  
Difficulty: Easy  
Topics: String

## Problem Description

Given a string `s`, return the string after replacing every uppercase letter with the same lowercase letter.


## Approach

This problem is straight forward in Python because the language provides a built-in method `lower()` for strings.

The `lower()` method converts all uppercase characters to their corresponding lowercase characters and leaves other characters unchanged.

## Python Code

```python
class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.lower()
