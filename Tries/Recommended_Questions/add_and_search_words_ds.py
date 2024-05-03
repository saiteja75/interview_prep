# design-add-and-search-words-data-structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/description/
'''
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

'''
class TrieNode:
    def __init__(self):
        self.childNodes = [None for _ in range(26)]
        self.wordCount = 0
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
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
        index = 0
        def searchNode(node,currindex):
            if currindex == len(word):
                return node.wordCount
            if word[currindex] == ".":
                for curr in node.childNodes:
                    if curr!=None:
                        if(searchNode(curr,currindex+1)):
                            return True
            elif node.childNodes[ord(word[currindex])-97]:
                return searchNode(node.childNodes[ord(word[currindex])-97],currindex+1)

            return False

        return searchNode(node,index)


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)