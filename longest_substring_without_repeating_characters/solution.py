class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_str = ''
        max = 0
        for i in s:
            while i in sub_str:
                sub_str = sub_str[1:]

            sub_str += i
            if len(sub_str) > max:
                    max = len(sub_str)

        return max if len(sub_str) < max else len(sub_str)
