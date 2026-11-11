class PrefixTree:
    def __init__(self):
        self.root = {} 

    def insert(self, word: str) -> None:
        node=self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node=node[c]
        node['*']=True 

    def search(self, word: str) -> bool:
        if not self.root:
            return False
        node=self.root
        for c in word:
            if c not in node:
                return False 
            node=node[c]
        if '*' not in node:
            return False 
        return True 
        
    def startsWith(self, prefix: str) -> bool:
        if not self.root:
            return False 
        node=self.root
        for c in prefix:
            if c not in node:
                return False 
            node=node[c]
        return True 

        
        