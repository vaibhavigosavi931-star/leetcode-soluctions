class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :return type: int
        """
        # If needle is longer than haystack, it can't be a substring
        if len(needle) > len(haystack):
            return -1
        
        # Slide a window of the size of 'needle' across 'haystack'
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
                
        return -1