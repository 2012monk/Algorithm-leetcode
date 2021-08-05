class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pad = {
            '2' : ['a', 'b', 'c'],
            '3' : ['d', 'e', 'f'],
            '4' : ['g', 'h', 'i'],
            '5' : ['j', 'k', 'l'],
            '6' : ['m', 'n', 'o'],
            '7' : ['p', 'q', 'r', 's'],
            '8' : ['t', 'u', 'v'],
            '9' : ['w', 'x', 'y', 'z']
        }
        
        v = []
        def dfs(idx, res):
            
            if len(digits) == len(res):
                v.append(res)
                return
            
            for i in range(idx, len(digits)):
                for a in pad[digits[i]]:
                    dfs(i + 1, res + a)
        if not digits:
            return []
        dfs(0, '')
        return v
                
            