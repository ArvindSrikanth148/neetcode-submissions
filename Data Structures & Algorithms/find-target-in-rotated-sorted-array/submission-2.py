class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l=0
        r=len(nums)-1

        while l<r:

            mid=(l+r)//2
            if nums[mid]>nums[r]:
                l=mid+1
            else: 
                r=mid
        pivot=l


        def binsearch(left:int,right: int) -> int:

            while left<=right:

                m=(left+right)//2

                if nums[m]==target:
                    return m
                elif nums[m]>target:
                    right =m-1
                else:
                    left=m+1
            return -1 
        res= binsearch(0, pivot - 1)
        if res!=-1:
            return res
        else:
            return binsearch(pivot,len(nums)-1)


            