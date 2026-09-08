class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        for x in tokens:
            # 1. Handle operators
            if x in ("+", "-", "*", "/"):
                # Pop operands in reverse order
                op2 = stack.pop()
                op1 = stack.pop()
                
                if x == '+':
                    stack.append(op1 + op2)
                elif x == '-':
                    stack.append(op1 - op2)
                elif x == '*':
                    stack.append(op1 * op2)
                elif x == '/':
                    # Use int() on float division to correctly truncate toward zero
                    stack.append(int(float(op1) / op2))
            
            # 2. Handle numbers (positive and negative)
            else:
                stack.append(int(x))
                
        return stack[0]
