import collections
class MagicDictionary(object):
    def __init__(self):
        self.buckets = collections.defaultdict(list)

    def buildDict(self, words):
        for word in words:
            self.buckets[len(word)].append(word)

    def search(self, word):
        return any(sum(a!=b for a,b in zip(word, candidate)) == 1
                   for candidate in self.buckets[len(word)])
val=MagicDictionary()
words=list(map(str,input().split()))
search_word=input()
(val.buildDict(words))
print(val.search(search_word))
