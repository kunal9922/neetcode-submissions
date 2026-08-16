class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # string first 
        if len(s) != len(t):
            return False
        count = dict()
        for n in s:
            count[n] = count.get(n, 0) + 1
        
        for n in t:
            if n in count.keys():
                if count[n]:
                    count[n] -= 1
                else:
                    return False
            else:
                return False
        return True


        