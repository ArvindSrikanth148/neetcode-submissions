class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result=[0]*len(temperatures)
        stack=[]
        istack=[]
        index=0
        for i in range(len(temperatures)):

            
            if len(stack)!=0:
                while stack[0]< temperatures[i] :
                
                    a=stack.pop(0)
                    b=istack.pop(0)
                    
                    result[b]=i-b
                    if len(stack)==0:
                        break
            stack.insert(0,temperatures[i])
            
            istack.insert(0,i)
            
        return result   


            





