"""
一. 定义
在计算机科学中，trie，又称前缀树或字典树，是一种有序树，用于保存关联数组，其中的键通常是字符串。
与二叉查找树不同，键不是直接保存在节点中，而是由节点在树中的位置决定。一个节点的所有子孙都有相同的前缀，
也就是这个节点对应的字符串，而根节点对应空字符串。一般情况下，不是所有的节点都有对应的值，
只有叶子节点和部分内部节点所对应的键才有相关的值。

trie中的键通常是字符串，但也可以是其它的结构。trie的算法可以很容易地修改为处理其它结构的有序序列，
比如一串数字或者形状的排列。比如，bitwise trie中的键是一串位元，可以用于表示整数或者内存地址。

二. 性质

- 根节点不包含字符，除根节点外每一个节点都只包含一个字符。
- 从根节点到某一节点，路径上经过的字符连接起来，为该节点对应的字符串。
- 每个节点的所有子节点包含的字符都不相同。

三. 应用场景及其优缺点

1. 典型应用是用于统计和排序大量的字符串（但不仅限于字符串），所以经常被搜索引擎系统用于文本词频统计。
它的优点是：最大限度地减少无谓的字符串比较，查询效率比哈希表高。

2. Trie的核心思想是空间换时间。利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的。
3. Trie树也有它的缺点,Trie树的内存消耗非常大.当然,或许用左儿子右兄弟的方法建树的话,可能会好点.


LeetCode - Trie 集 （14题）

【208】Implement Trie (Prefix Tree) （2018年11月27日）

【211】Add and Search Word - Data structure design (2018年11月27日)

【212】Word Search II 

【336】Palindrome Pairs 

【421】Maximum XOR of Two Numbers in an Array 

【425】Word Squares 

【472】Concatenated Words 

【642】Design Search Autocomplete System 

【648】Replace Words 

【676】Implement Magic Dictionary 

【677】Map Sum Pairs

【692】Top K Frequent Words 

【720】Longest Word in Dictionary （2019年2月14日，谷歌tag）

【745】Prefix and Suffix Search 
"""