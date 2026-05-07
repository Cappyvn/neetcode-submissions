class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        stringS = {}
        stringT = {}

        for c in s:
            if c not in stringS:
                stringS[c] = 1
            else:
                a = stringS[c]
                stringS[c] = a + 1
        
        for c in t:
            if c not in stringT:
                stringT[c] = 1
            else:
                a = stringT[c]
                stringT[c] = a + 1
            
        return stringT == stringS