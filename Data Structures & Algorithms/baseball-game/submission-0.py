class Solution:
    def calPoints(self, operations: List[str]) -> int:


        counter = 0

        new_stack = []

        for x in operations:
            match x:
                case "+":
                    counter += (new_stack[-1]+ new_stack[-2])
                    new_stack.append(new_stack[-1]+ new_stack[-2])
                case "D": 
                    counter += (new_stack[-1] * 2)
                    new_stack.append(new_stack[-1] * 2 )
                case "C":  
                    counter -= new_stack.pop()
                case _: 
                    counter += int(x)
                    new_stack.append(int(x))
                    
        return counter


                

        