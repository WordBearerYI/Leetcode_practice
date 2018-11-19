'''
https://leetcode.com/problems/word-search/
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
'''

class TrieNode(object):
    def __init__(self, is_leaf = False):
        self.children = dict()
        self.is_leaf = is_leaf
        
    def add_s(self, s):
        curr = self
        for c in s:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_leaf = True

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        trie = TrieNode()
        trie.add_s(word)
        
        height = len(board)
        width = len(board[0])
        
        def check(i,j,node):
            if node.is_leaf:
                return True     
            if i < 0 or i >= height or j < 0 or j >= width:
                return 
            if board[i][j] in node.children:
                c = board[i][j]
                board[i][j] = '-'
                if check(i + 1, j, node.children[c]) or check(i - 1, j, node.children[c]) or check(i, j + 1, node.children[c]) or check(i, j - 1, node.children[c]):
                    return True
                board[i][j] = c
        return True if any([check(i,j,trie) for i in range(height) for j in range(width)]) else False
        


'''
#tle
class Solution(object):
    def findWords(self, board, words):
    
        row = len(board)
        col = len(board[0])
        if row<=0 or col<=0:
            print "FFF"
            if not word:
                return True
            return False
        
        def bfs(i,j,s,lst):
            if not s:
                return True
            if i>=row or i<0 or j>=col or j<0:
                return False
            print i,j,s
            
                
            if (i,j) not in lst and s[0] == board[i][j]:
                newlst = lst[:]
                newlst.append((i,j))
                return bfs(i+1,j,s[1:],newlst) or bfs(i-1,j,s[1:],newlst) or bfs(i,j+1,s[1:],newlst) or  bfs(i,j-1,s[1:],newlst)
            
        lst = []
        for i in range(row):
            for j in range(col):
                if bfs(i,j,word,lst):
                    return True
        return False
  '''
