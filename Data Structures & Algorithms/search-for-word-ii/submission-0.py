class TrieNode:
    def __init__(self):
        self.children = {}
        self.whole_word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.root = TrieNode()
        for word in words:
            cur = self.root
            for letter in word:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]
            cur.whole_word = word

        rows, cols = len(board), len(board[0])
        result = []
        
        def dfs(r, c, node):
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c] not in node.children:
                return

            letter = board[r][c]
            new_node = node.children[letter]
            
            if new_node.whole_word:
                result.append(new_node.whole_word)
                new_node.whole_word = None

            board[r][c] = "#"

            dfs(r+1,c,new_node)
            dfs(r-1,c,new_node)
            dfs(r,c+1,new_node)
            dfs(r,c-1,new_node)

            board[r][c] = letter

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,self.root)
            
        return result
