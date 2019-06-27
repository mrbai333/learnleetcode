# Date : 06/27/19
# 使用字典树Trie进行处理
# 1.首先将root初始化位python自带的字典collections.defaultdict()
# 2.其次，插入操作使用python自带字典的setdefault操作，在单词的最后插入结束符号end_with_char
# 3.查询和检查前缀都是从root开始检查字符是否包含在字典中，查询要多检查一次结束符号是否包含在节点中。
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = collections.defaultdict()
        self.end_with_char = "#"

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            node = node.setdefault(ch,collections.defaultdict())
        node[self.end_with_char] = self.end_with_char
        return

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            if ch not in node:
                return False
            node = node[ch]
        return self.end_with_char in node

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node = node[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)