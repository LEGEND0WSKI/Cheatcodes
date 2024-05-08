class Solution:
    def generateParenthesis(n:int) -> list[str]:
        sol = []
        ans = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                ans.append("".join(sol))
                return
            
            if openN < n:
                sol.append("(")
                backtrack(openN+1, closeN)
                sol.pop()

            if closeN < openN:
                sol.append(")")
                backtrack(openN, closeN+1)
                sol.pop()

        backtrack(0, 0)
        return ans
    
print(Solution.generateParenthesis(6))