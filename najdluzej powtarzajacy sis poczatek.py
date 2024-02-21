class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        x = sorted(strs)
        x2 = x[-1]
        x = x[0]
        i = 1
        wynik = ''
        while i<=len(x):
            if x[i-1]!=x2[i-1]:
                return wynik
            else:
                wynik =wynik+ x[i-1]
                i =i+1
        return wynik

a = Solution()
strs = ["flower","flow","flight"]
print(a.longestCommonPrefix(strs))