class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        res = set()
        d = defaultdict(list)
        
        for index1, t1 in enumerate(transactions):
            name, time1, amt1, city1 = t1.split(',')
            
            if int(amt1) > 1000:
                res.add((index1, t1))
            
            for index2, t2 in d[name]:
                name, time2, amt, city2 = t2.split(',')
                
                if abs(int(time1) - int(time2)) <= 60 and city1 != city2:
                    res.add((index1, t1))
                    res.add((index2, t2))

            d[name].append((index1, t1))
        
        return [x[1] for x in res]
                
            
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         d = defaultdict(list)
#         res = set()
#         for index1, t1 in enumerate(transactions):
#             name, time1, amt1, city1 = t1.split(',')
            
#             if int(amt1) > 1000:
#                 res.add((index, t1))
            
#             for index2, t2 in d[name]:
#                 name, time2, amt2, city2 = t2.split(',')
#                 if abs(int(time2)-int(time1)) <= 60 and city1 != city2:
#                     res.add((index2, t2))
#                     res.add((index1, t1))
                    
#             d[name].append((index1, t1))
            
#         return [x[1] for x in res]

                    
            
        
       
        
        
        
        
        
#         res = set()
#         d = defaultdict(list)
        
#         for index, transaction in enumerate(transactions):
#             name, time, amt, city = transaction.split(',')
            
#             if int(amt) > 1000:
#                 res.add((index, transaction))
            
            
#             for t in d[name]:
#                 name2, time2, amt2, city2 = t[1].split(',')
                
#                 if abs(int(time) - int(time2)) <= 60 and city != city2:
#                     res.add((t[0], t[1]))
#                     res.add((index, transaction))
            
#             d[name].append((index, transaction))
        
#         return [t[1] for t in res]

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = []
        
#         d = defaultdict(dict)
        
#         for transaction in transactions:
#             name, time, amt, city = transaction.split(',')
#             time = int(time)
            
#             if name not in d[time]:
#                 d[time][name] = set()
            
#             d[time][name].add(city)
            
        
#         for transaction in transactions:
#             name, time, amt, city = transaction.split(',')
#             time = int(time)
            
#             if int(amt) > 1000:
#                 res.append(transaction)
#                 continue 
            
#             for t in range(time-60, time+ 61):
#                 if t not in d:
#                     continue
#                 if name not in d[t]:
#                     continue 
                
#                 transaction_by_name_at_time = d[t][name]
                
#                 if city not in transaction_by_name_at_time or len(transaction_by_name_at_time) > 1:
#                     res.append(transaction)
#                     break
#         return res 
                
                
                
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
            