class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodf=1
        prodr=1
        resf=[]
        resrev=[]
        res=[]
    
        for i in range(len(nums)):
            resf.append(0)
            resrev.append(0)
            res.append(0)


        
        prev=1
        for i in range(len(nums)):
            if i == 0 :
                prev =nums[i]
                
                resf[i]=1
            else:
                prodf=prodf*prev
                resf[i]=prodf
                prev=nums[i]

        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                prev=nums[i] 
                
                resrev[i]=1
            else: 
                prodr= prodr*prev
                resrev[i]=prodr
                prev=nums[i]
 
        for i in range(len(nums)):

            res[i]=resf[i]*resrev[i]
        return(res)
         

