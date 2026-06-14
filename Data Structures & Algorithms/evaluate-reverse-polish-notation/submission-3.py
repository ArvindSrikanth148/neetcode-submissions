class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        
        while len(tokens)>0:
            c=tokens.pop(0)
            print("token:", c)
            print("stack:", stack)
            if c == "+" or c == "-" or c == "/" or c=="*":
                e1=stack.pop()
                e2=stack.pop()
                if c=="+":
                  stack.append(e1+e2)
                elif c== "-":
                    stack.append(e2-e1)
                elif c=="/":
                    stack.append(int(e2/e1))
                else:
                    stack.append(e1*e2)
                  
                
            else:
                num=int(c)
                stack.append(num)

        return stack[0]