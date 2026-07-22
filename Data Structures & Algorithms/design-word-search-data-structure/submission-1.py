class Trie():
    def __init__(self): 
        self.children={}
        self.EOW= False
class WordDictionary:

    def __init__(self):
        self.root=Trie()

    def addWord(self, word: str) -> None:
        cur=self.root

        for c in word: 
            if c not in cur.children:
                cur.children[c]=Trie()
            cur=cur.children[c]
        cur.EOW= True

    def search(self, word: str) -> bool:


        cur=self.root
        
        def dfs(node, i):
            if i == len(word):
                return node.EOW

            if word[i] != ".":
                if word[i] not in node.children:
                    return False
                return dfs(node.children[word[i]], i + 1)

            for child in node.children.values():
                if dfs(child, i + 1):
                    return True
            return False

    
            
        
        return dfs(cur,0)

            
            

        
    


        
        
