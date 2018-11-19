
'''
https://leetcode.com/problems/word-search-ii/

Word-Search-II
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent"
cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.

Input: 
words = ["oath","pea","eat","rain"] and board =
[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Output: ["eat","oath"]
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
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        
        trie_root = TrieNode()
        for w in words:
            trie_root.add_s(w)
            
        result = set()

        height = len(board)
        width = len(board[0])
        
        def go(i, j, node, word):
            
            if node.is_leaf:
                result.add(word)
                
            if i < 0 or i >= height or j < 0 or j >= width:
                return 
            
            if board[i][j] in node.children:
                c = board[i][j]
                board[i][j] = '-'
                go(i + 1, j, node.children[c], word + c)
                go(i - 1, j, node.children[c], word + c)
                go(i, j + 1, node.children[c], word + c)
                go(i, j - 1, node.children[c], word + c)
                board[i][j] = c
            
            if word == '':
                go(i, j + 1, node, word) if j + 1 < width else go(i + 1, 0, node, word)
            
        go(0, 0, trie_root, '')    
        
        return list(result)
