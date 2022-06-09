class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        d = defaultdict(list)
        res = set()
        
        
        for i in range(len(transactions)):
            name, time, amt, city = transactions[i].split(',')
            
            if int(amt) > 1000:
                res.add((i, transactions[i]))
            
            if name in d:
                for t in d[name]:
                    name2, time2, price2, city2 = t[1].split(',')
                    index = t[0]
                    
                    if abs(int(time) - int(time2)) <= 60 and city2 != city:
                        res.add((index, t[1]))
                        res.add((i, transactions[i]))
            d[name].append((i, transactions[i]))
        
        return [t[1] for t in res]
            