class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operands = ['+', '-', '*', '/']
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            
            else:
                if token == '+':
                    a, b = stack.pop(), stack.pop()
                    stack.append(a + b)
                
                elif token == '-':
                    a, b = stack.pop(), stack.pop() 
                    stack.append(b - a )
                
                elif token == '/':
                    a, b = stack.pop(), stack.pop() 
                    stack.append(int(b / a))
                
                elif token == '*':
                    a, b = stack.pop(), stack.pop()
                    stack.append(a*b)
            
        return stack[-1]