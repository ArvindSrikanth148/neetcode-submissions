class TimeMap:

    def __init__(self):
        self.dict={}
        self.matrix={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.dict.keys():
            self.dict[key][timestamp]=value
        else:
            self.dict[key]={timestamp:value}
        if key in self.matrix.keys():
            self.matrix[key].append(timestamp)
        else:
            self.matrix[key]=[timestamp]
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.matrix.keys():
         list=self.matrix[key]

        else:
            return ""
        l=0
        r=len(list)-1
        if list[0]>timestamp:
            print(timestamp,list[0])
            return "" 

        while l<=r:
            mid=(l+r)//2
            if list[mid]==timestamp:
                return self.dict[key][list[mid]]

            elif list[mid]<timestamp:
                l=mid+1
            else:
                r=mid-1
        if l!=0:
         return self.dict[key][list[l-1]]
        else :
          return self.dict[key][list[0]]




        
