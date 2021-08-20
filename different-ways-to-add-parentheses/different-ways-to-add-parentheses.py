class Solution:
    def diffWaysToCompute(self, exp: str) -> List[int]:
        
        def calc(left, right, op):
            res = []
            for l in left:
                for r in right:
                    res.append(eval(str(l)+op+str(r)))
            return res
        if exp.isdigit():
            return [int(exp)]
        res = []        
        for i,v in enumerate(exp):
            if v in '-+*':
                l = self.diffWaysToCompute(exp[:i])
                r = self.diffWaysToCompute(exp[i + 1:])
                res.extend(calc(l,r,v))
                
        return res