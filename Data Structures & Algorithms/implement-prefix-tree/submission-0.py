class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                ptr.children[c] = TrieNode()
            ptr = ptr.children[c]
        ptr.word = True


    def search(self, word: str) -> bool:
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return ptr.word
        

    def startsWith(self, prefix: str) -> bool:
        ptr = self.root
        for c in prefix:
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return True
        