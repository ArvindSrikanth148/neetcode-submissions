class Node: 
    def __init__(self,key,val) -> None:
       self.key=key
       self.val=val
       self.prev=None 
       self.next=None


class LRUCache:

    def __init__(self, capacity: int):
        self.dict={}
        self.c=capacity
        self.left=Node(0,0)
        self.right=Node(0,0)
        self.left.next, self.right.prev = self.right, self.left
        

    def insert(self,node):

        previous = self.right.prev

        previous.next = node
        node.prev = previous

        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        prev,nxt=node.prev,node.next
        prev.next=nxt
        nxt.prev=prev

    def get(self, key: int) -> int:

        if key in self.dict.keys():
            self.remove(self.dict[key])
            self.insert(self.dict[key])
            return self.dict[key].val
        return -1 

    def put(self, key: int, value: int) -> None:

        if key in self.dict.keys():
            self.remove(self.dict[key])
            
        self.dict[key]=Node(key,value)
        self.insert(self.dict[key])

        if len(self.dict)>self.c:
            lru = self.left.next
            self.remove(lru)
            del self.dict[lru.key]

            


                
        
