class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n= len(haystack)
        m= len(needle)

        if m==0:
            return 0
        
        for i in range(n-m+1):
            for j in range(m):
                if haystack[i+j]!=needle[j]:
                    break
                if j==m-1:
                    return i
        return -1
