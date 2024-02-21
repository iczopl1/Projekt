class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
	    def dfs(left, right, s):
		    if len(s) == n * 2:
			    res.append(s)
			    return

		    if left < n:
			    dfs(left + 1, right, s + '(')

		    if right < left:
			    dfs(left, right + 1, s + ')')

	    res = []
	    dfs(0, 0, '')
	    return res





a = Solution()
n = 3
print(a.generateParenthesis(n))