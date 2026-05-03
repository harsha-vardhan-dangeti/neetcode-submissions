class Solution:
    def isValid(self, s: str) -> bool:

        hash_map = { '}' : '{' , ']' : '[', ')' : '(' }

        stack = []

        for x in s :
            if x in hash_map:
                if len(stack) != 0 and stack[-1] == hash_map[x] :
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)

        return len(stack) == 0            
        