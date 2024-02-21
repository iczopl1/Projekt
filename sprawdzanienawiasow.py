class Solution:
    def isValid(self, s: str) -> bool:
        lens = len(s)
        x = 0
        znaki =['()','[]','{}']
        if lens % 2 != 0:
            return False
        lens = lens/2
        while x<lens:
            for znak in znaki:
                if(s.find(znak)!=-1):
                    s = s.replace(znak,'')
                    if s =='':
                        return True
            x = x+1
        return False




a = Solution()
strs = "[{()}]"
print(a.isValid(strs))
