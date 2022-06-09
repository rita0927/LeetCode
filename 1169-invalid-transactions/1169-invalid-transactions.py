class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        res = []
        
        d = defaultdict(dict)
        
        for transaction in transactions:
            name, time, amt, city = transaction.split(',')
            time = int(time)
            
            if name not in d[time]:
                d[time][name] = set()
            
            d[time][name].add(city)
            
        
        for transaction in transactions:
            name, time, amt, city = transaction.split(',')
            time = int(time)
            
            if int(amt) > 1000:
                res.append(transaction)
                continue 
            
            for t in range(time-60, time+ 61):
                if t not in d:
                    continue
                if name not in d[t]:
                    continue 
                
                transaction_by_name_at_time = d[t][name]
                
                if city not in transaction_by_name_at_time or len(transaction_by_name_at_time) > 1:
                    res.append(transaction)
                    break
        return res 
                
                
                
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d = defaultdict(list)
#         res = set()
        
        
#         for i in range(len(transactions)):
#             name, time, amt, city = transactions[i].split(',')
            
#             if int(amt) > 1000:
#                 res.add((i, transactions[i]))
            
#             if name in d:
#                 for t in d[name]:
#                     name2, time2, price2, city2 = t[1].split(',')
#                     index = t[0]
                    
#                     if abs(int(time) - int(time2)) <= 60 and city2 != city:
#                         res.add((index, t[1]))
#                         res.add((i, transactions[i]))
#             d[name].append((i, transactions[i]))
        
#         return [t[1] for t in res]
            