'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
'''

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        wordList.add(endWord)
        candidates,visited,result = [beginWord],set([beginWord]),0
        while candidates:
            newcandidates=[]
            for candidate in candidates:
                if candidate == endWord:
                    return result+1
                else:
                    for i in xrange(len(beginWord)):
                        for w in 'abcdefghijklmnopqrstuvwxyz':
                            new_word = candidate[:i]+w+candidate[i+1:]
                            if new_word in wordList and new_word not in visited:
                                newcandidates.append(new_word)
                                visited.add(new_word) 
            candidates = newcandidates
            result+=1
        return 0
