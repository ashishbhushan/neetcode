class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_end
            char = word[index]
            if char == ".":
                for child in node.children.values():
                    if dfs(child, index+1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], index+1)
        
        return dfs(self.root, 0)