class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True 
    
class Solution:       
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        dirs = (0,1), (1,0), (-1,0), (0,-1)
        for word in words:
            root.add_word(word)
        m, n = len(board), len(board[0])
        res, visit = set(), set()
        def dfs(i, j, node, word):
            if i < 0 or j < 0 or i == m or j == n or (i,j) in visit or board[i][j] not in node.children:
                return 
            
            visit.add((i, j))
            word += board[i][j]
            node = node.children[board[i][j]]
            if node.is_end:
                res.add(word)

            for dx, dy in dirs:
                dfs(i + dx, j + dy, node, word)
            
            visit.remove((i,j))


        for i in range(m):
            for j in range(n):
                dfs(i, j, root, "")
        
        return list(res)
           


        
        