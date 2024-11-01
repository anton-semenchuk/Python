class SuffixTrieConstruction:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = '*'
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insertSubstringStartingAt(i, string)

    # O(n^2) time | O(n^2) space
    def insertSubstringStartingAt(self, i, string):
        node = self.root
        for j in range(i, len(string)):
            letter = string[j]
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.endSymbol] = True

    # O(m) time | O(1) space - where m is the length of string
    def contains(self, string):
        node = self.root
        for letter in string:
            if letter not in node:
                return False
            node = node[letter]
        return self.endSymbol in node


trie = SuffixTrieConstruction("babc")
print(trie.contains('bc'))
