    
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.root
        for a in word:
            if a not in root:
                root[a] = {}
            root = root[a]
        root['#'] = '#'
                
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        for a in word:
            if a not in root:
                return False
            root = root[a]
        if '#' in root:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        for a in prefix:
            if a not in root:
                return False
            root = root[a]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)