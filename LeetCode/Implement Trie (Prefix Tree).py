'''
Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
'''

class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.flag = False
        self.leaves = {}
        

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        #raise Exception(word)
        print word
        temp = self.root
        for c in word:
            if c not in temp.leaves:
                temp.leaves[c] = TrieNode()
            temp = temp.leaves[c]
        temp.flag = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        print '-',word
        temp = self.root
        for c in word:
            if c in temp.leaves:
                temp = temp.leaves[c]
            else:
                return False
        return temp.flag

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        print '--',prefix
        temp = self.root
        for c in prefix:
            if c in temp.leaves:
                temp = temp.leaves[c]
            else:
                return False
        if temp.leaves or temp.flag:
            return True
        

