# word-break
# https://leetcode.com/problems/word-break/description/
'''
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

'''

class TrieNode:
    def __init__(self):
        self.childNodes = [None for _ in range(26)]
        self.wordCount = 0
class Trie:

    def __init__(self):
        self.root = TrieNode()
        self.memo = {}
        

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
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordTrie = Trie()
        n = len(s)
        for word in wordDict:
            wordTrie.insert(word)
        root = wordTrie.root
        # set every instance to False to start
        dp = [False] * (n + 1)
		# intialize the last instance to True
        dp[-1] = True
        
		# Go backwards to save time repeating 
        for l in reversed(range(n)):
            
			# intialize curr to a new trie every time we move our left pointer
            curr = wordTrie.root
            
			# check every right pointer between l and n, if it isn't a child it breaks, otherwise it keeps going until r hits the range limit or
			# until curr is now a word and the next step in the sentence can also be a word, where that left pointer will be set to true 
            for r in range(l, n):
                
                if curr.childNodes[ord(s[r])-97] == None:
                    break
                curr = curr.childNodes[ord(s[r])-97]
                if curr.wordCount and dp[r + 1]:
                    dp[l] = True
                    break
                    
        return dp[0]

        

        