class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for i in range(len(tokens)):
            match tokens[i]:
                case "+":
                    x, y = stack.pop(), stack.pop()
                    stack.append(x + y)
                case "-":
                    x, y = stack.pop(), stack.pop()
                    stack.append(y - x)
                case "*": 
                    x, y = stack.pop(), stack.pop()
                    stack.append(x * y)
                case "/" :
                    x, y = stack.pop(), stack.pop()
                    stack.append(int(y / x))
                case _:
                    stack.append(int(tokens[i]))
            print(stack)
        return stack[-1]

        