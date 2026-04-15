class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        ptr = self.root
        for c in word:
            if c not in ptr.children:
                ptr.children[c] = TrieNode()
            ptr = ptr.children[c]
        ptr.word = True
        

    def search(self, word: str) -> bool:
        def searchChildren(start, root):
            ptr = root

            for i in range(start, len(word)):
                char = word[i]
                if char == '.':
                    for child in ptr.children.values():
                        if searchChildren(i + 1, child):
                            return True
                    return False
                else:
                    if char not in ptr.children:
                        return False
                    ptr = ptr.children[char]
            return ptr.word
        return searchChildren(0, self.root)
