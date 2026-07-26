class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:



        preMap={i:[] for i in range(numCourses)}
        for a, b in prerequisites:
            preMap[a].append(b)
        
        visiting=set()
        
        def dfs(c): 

            if c in visiting: 
                return False
            if preMap[c]==[]: 
                return True
            visiting.add(c)
            for pre in preMap[c]: 
                if not dfs(pre):
                    return False
            visiting.remove(c)

            preMap[c]=[]

            return True 


        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
        