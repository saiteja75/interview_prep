# trie-prefix-tree
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
''' 
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

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

        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for value in prefix:
            childNodes = node.childNodes
            pos = ord(value)-97
            if childNodes[pos] == None:
                return False
            node = childNodes[pos]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)