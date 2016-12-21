'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
Note:
You may assume that all words are consist of lowercase letters a-z.
'''



class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.d = {}
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        l = self.d
        for c in word:
            if c not in l:
                l[c] = {}
            l = l[c]
        l['#']=True
        
        return self.d
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def Recu(word,di,pos):
            if len(word)==pos:
                if '#' in di:
                    return True
                return False  
        
            if word[pos] in di:
                return Recu(word,di[word[pos]],pos+1)
            if word[pos] == '.':
                for key in di:
                    if key!='#':
                        if Recu(word,di[key],pos+1):
                            return True
        
            return False

        return Recu(word,self.d,0) 
