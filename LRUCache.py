from collections import defaultdict 
class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.abbr=defaultdict(set)
        for i in dictionary:
           self.abbr[self.to_abbr(i)].add(i)

    def to_abbr(self,word):
        if len(word)<=2:
            return word
        else:
            return '{}{}{}'.format(word[0],len(word)-2,word[-1])
        
    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        
        abbr =self.to_abbr(word)
        words = self.abbr[abbr]
        if len(words)==0:return True
        return len(words)==1 and word in words



v = ValidWordAbbr([ 'a'])
print v.isUnique('')










import collections
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return -1

    def set(self, key, value):
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value

