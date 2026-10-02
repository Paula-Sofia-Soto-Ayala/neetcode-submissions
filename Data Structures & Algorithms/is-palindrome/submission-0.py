class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        s = s.replace(" ", "")
        s = "".join([char for char in s if char.isalnum()])

        begin = 0
        end = len(s)-1

        while(begin < end):
            if s[begin] != s[end]:
                return False
            else:
                begin += 1
                end -= 1
        return True
        