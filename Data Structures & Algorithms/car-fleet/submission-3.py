class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []

        result_stack = []

        

        for i in range(len(position)):
            stack.append((position[i], speed[i]))
        
        stack.sort(reverse=True)

    
        for i in range(len(stack)):
            result_stack.append((target - stack[i][0])/stack[i][1])
            while len(result_stack) >=2 and result_stack[-1] <= result_stack[-2]:
                result_stack.pop()
        
        return len(result_stack)