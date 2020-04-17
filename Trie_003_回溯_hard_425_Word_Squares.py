"""
给定一个单词集合 （没有重复），找出其中所有的 单词方块 。

一个单词序列形成了一个有效的单词方块的意思是指从第 k 行和第 k 列 (0 ≤ k < max(行数, 列数)) 来看都是相同的字符串。

例如，单词序列 ["ball","area","lead","lady"] 形成了一个单词方块，因为每个单词从水平方向看和从竖直方向看都是相同的。

b a l l
a r e a
l e a d
l a d y
注意：

单词个数大于等于 1 且不超过 500。
所有的单词长度都相同。
单词长度大于等于 1 且不超过 5。
每个单词只包含小写英文字母 a-z。
 

示例 1：

输入：
["area","lead","wall","lady","ball"]

输出：
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

解释：
输出包含两个单词方块，输出的顺序不重要，只需要保证每个单词方块内的单词顺序正确即可。 

"""

# ----------------------------------------------------------------------
# class Solution:
#     def wordSquares(self, words: List[str]) -> List[List[str]]:

#         self.words = words
#         self.N = len(words[0])

#         results = []
#         word_squares = []
#         for word in words:
#             # try with every word as the starting word
#             word_squares = [word]
#             self.backtracking(1, word_squares, results)
#         return results

#     def backtracking(self, step, word_squares, results):

#         if step == self.N:
#             results.append(word_squares[:])
#             return

#         prefix = ''.join([word[step] for word in word_squares])
        
#         # find out all words that start with the given prefix        
#         for candidate in self.getWordsWithPrefix(prefix):
#             # iterate row by row
#             word_squares.append(candidate)
#             self.backtracking(step+1, word_squares, results)
#             word_squares.pop()

#     def getWordsWithPrefix(self, prefix):
#         for word in self.words:
#             if word.startswith(prefix):
#                 yield word

# ----------------------------------------------------------------------




# class Solution:

#     def wordSquares(self, words: List[str]) -> List[List[str]]:

#         self.words = words
#         self.N = len(words[0])
#         self.buildPrefixHashTable(self.words)
#         print(self.prefixHashTable)

#         results = []
#         word_squares = []
#         for word in words:
#             word_squares = [word]
#             self.backtracking(1, word_squares, results)
#         return results

#     def backtracking(self, step, word_squares, results):
#         if step == self.N:
#             results.append(word_squares[:])
#             return

#         prefix = ''.join([word[step] for word in word_squares])
#         print(word_squares, prefix)
#         for candidate in self.getWordsWithPrefix(prefix):
#             word_squares.append(candidate)
#             self.backtracking(step+1, word_squares, results)
#             word_squares.pop()

#     def buildPrefixHashTable(self, words):
#         self.prefixHashTable = {}
#         for word in words:
#             for prefix in (word[:i] for i in range(1, len(word))):
#                 self.prefixHashTable.setdefault(prefix, set()).add(word)

#     def getWordsWithPrefix(self, prefix):
#         if prefix in self.prefixHashTable:
#             return self.prefixHashTable[prefix]
#         else:
#             return set([])


# Trie
class Solution:

    # def wordSquares(self, words: List[str]) -> List[List[str]]:
    def wordSquares(self, words):

        self.words = words
        self.N = len(words[0])
        self.buildTrie(self.words)
        print(self.trie)

        results = []
        word_squares = []
        for word in words:
            word_squares = [word]
            self.backtracking(1, word_squares, results)
        return results

    def buildTrie(self, words):
        self.trie = {}

        for wordIndex, word in enumerate(words):
            node = self.trie
            for char in word:
                if char in node:
                    node = node[char]
                else:
                    newNode = {}
                    newNode['#'] = []
                    node[char] = newNode
                    node = newNode
                node['#'].append(wordIndex)

    def backtracking(self, step, word_squares, results):
        if step == self.N:
            results.append(word_squares[:])
            return

        prefix = ''.join([word[step] for word in word_squares])
        print(word_squares, prefix, self.getWordsWithPrefix(prefix))
        for candidate in self.getWordsWithPrefix(prefix):
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()

    def getWordsWithPrefix(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return []
            node = node[char]
        return [self.words[wordIndex] for wordIndex in node['#']]
