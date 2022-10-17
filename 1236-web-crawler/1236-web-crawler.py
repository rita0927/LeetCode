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
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        hostname='http://'+startUrl.split('/',3)[2]
        res=set([startUrl])
        stack=[startUrl]
        while stack:
            url=stack.pop()
            for sub_url in htmlParser.getUrls(url):
                if hostname in sub_url and sub_url not in res:
                    res.add(sub_url)
                    stack.append(sub_url)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # hostname='http://'+startUrl.split('/',3)[2]
        # res=set([startUrl])
        # # use the stack to iterate all related urls with the same hostname
        # stack=[startUrl]
        # while stack:
        #     url=stack.pop()
        #     # find all sub_url related to url
        #     for sub_url in htmlParser.getUrls(url):
        #         # if the related url contains the same hostname
        #         if hostname in sub_url and sub_url not in res:
        #             res.add(sub_url)
        #             stack.append(sub_url)
        # return res 
        
        