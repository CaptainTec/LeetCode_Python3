# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    # def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
    def crawl(self, startUrl: str, htmlParser):
        res = set([startUrl])
        queue = [startUrl]
        while queue:
            top = queue.pop(0)
            for one in htmlParser.getUrls(top):
                if startUrl[7:].split('/')[0] == one[7:].split('/')[0] and one not in res:
                    queue.append(one)
                    res.add(one)
        return res