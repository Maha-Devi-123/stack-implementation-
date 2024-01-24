class Solution:
    def isValid(self, s: str) -> bool: 
        k=[]
        h={')':'(',']':'[','}':'{'}
        for i in s:
            if i in h:
                if k and  k[-1] == h[i] :
                    k.pop()
                else:
                    return False
                
            else:
                k.append(i)
        
        return True if not k else False 