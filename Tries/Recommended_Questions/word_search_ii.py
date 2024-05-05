# word-search-ii
# https://leetcode.com/problems/word-search-ii/
'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

'''

class TrieNode:
    def __init__(self):
        self.childNodes = [None for _ in range(26)]
        self.wordCount = 0
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for value in word:
            childNodes = node.childNodes
            pos = ord(value)-97
            if childNodes[pos] == None:
                childNodes[pos] = TrieNode()
            node = childNodes[pos]
        node.wordCount+=1


    def search(self, word: str) -> bool:
        node = self.root
        for value in word:
            childNodes = node.childNodes
            pos = ord(value)-97
            if childNodes[pos] == None:
                return False
            node = childNodes[pos]
        if(node.wordCount > 0):
            return True
        return False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordTrie = Trie()
        root = wordTrie.root
        res = set([])
        m = len(board)
        n = len(board[0])
        for word in words:
            wordTrie.insert(word)
        
        def searchWord(row,col,trie,s):
            if trie.wordCount>0:
                res.add(s)
            if row>=m or row<0 or col>=n or col<0 or board[row][col] == '':
                return
            if trie.childNodes[ord(board[row][col])-97]:
                trie = trie.childNodes[ord(board[row][col])-97]
                s += board[row][col]
                temp = board[row][col]
                board[row][col] = ''
                searchWord(row+1,col,trie,s)
                searchWord(row-1,col,trie,s)
                searchWord(row,col+1,trie,s)
                searchWord(row,col-1,trie,s)
                board[row][col] = temp
        
        for i in range(m):
            for j in range(n):
                searchWord(i,j,root,'')
        return list(res)


        