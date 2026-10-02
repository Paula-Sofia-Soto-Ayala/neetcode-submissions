class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1 = {}
        dic2 = {}

        for i in s:
            if i in dic1:
                dic1[i] += 1
            else:
                dic1[i] = 1

        for i in t:
            if i in dic2:
                dic2[i] += 1
            else:
                dic2[i] = 1

        if len(dic1) != len(dic2):
            return False

        for i in dic1:
            if i not in dic2:
                return False
            elif dic1[i] != dic2[i]:
                return False
        return True

        

        
        