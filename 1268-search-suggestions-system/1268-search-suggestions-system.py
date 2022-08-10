class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        res = []
        products.sort()
        
        for i, ch in enumerate(searchWord):
            temp = []
            for p in products:
                if i < len(p) and p[i] == ch:
                    temp.append(p)
            products = temp
            res.append(temp[:3])
        
        return res 
        
        
        
        
        