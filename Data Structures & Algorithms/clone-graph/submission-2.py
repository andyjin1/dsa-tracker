"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visit = {}      

        def dfs(curr):
            if curr in visit:
                return visit[curr]
            
            copy = Node(curr.val)
            visit[curr] = copy        
            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy
            
        return dfs(node) if node else None