# 1. Two Sum

[LeetCode Link](https://leetcode.com/problems/two-sum/)  
Difficulty: Easy  
Topics: Array, Hash Table

---

## Problem Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

---

## Approach

This solution uses two loops to check all possible pairs in the array.

- Iterate through each element using index `i`
- For each `i`, iterate through the remaining elements using index `j`
- If `nums[i] + nums[j] == target`, return `[i, j]`

---

## Python Code

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
