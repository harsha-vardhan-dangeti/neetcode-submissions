class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        hash_map = { ']': '[', ')': '(',  '}': '{' }
        stack = []
        for i in range(len(s)):
            if s[i] in hash_map.values():
                stack.append(s[i])
            else: 
                if len(stack) == 0:
                    return False
                tmp = stack.pop()
                if tmp != hash_map[s[i]]:
                    return False
        
        return (len(stack)==0)



        