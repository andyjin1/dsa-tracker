class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = '+', '-', '*', '/'
        stack = []
        for c in tokens: 
            if c not in operands:
                stack.append(int(c))
            
            else:
                num1, num2 = stack.pop(), stack.pop()
                if c == '+':
                    stack.append(num1 + num2)
                
                elif c == '-':
                    stack.append(num2 - num1)
                
                elif c == '/':
                    stack.append(int(num2 / num1))
                
                else:
                    stack.append(num1 * num2)
        
        return stack[-1]