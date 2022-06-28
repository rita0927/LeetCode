class Solution:
    def numberToWords(self, num: int) -> str:
        d = {
            1000000000: 'Billion',
            1000000: 'Million',
            1000: 'Thousand',
            100: 'Hundred',
            90: 'Ninety',
            80: 'Eighty',
            70: 'Seventy',
            60: 'Sixty',
            50: 'Fifty',
            40: 'Forty',
            30: 'Thirty',
            20: 'Twenty',
            19: 'Nineteen',
            18: 'Eighteen',
            17: 'Seventeen',
            16: 'Sixteen',
            15: 'Fifteen',
            14: 'Fourteen',
            13: 'Thirteen',
            12: 'Twelve',
            11: 'Eleven',
            10: 'Ten',
            9: 'Nine',
            8: 'Eight',
            7: 'Seven',
            6: 'Six',
            5: 'Five',
            4: 'Four',
            3: 'Three',
            2: 'Two',
            1: 'One',
            0: 'Zero'      
        }

        if num == 0:
            return 'Zero'
        
        def helper(n):
            if n <= 20:
                return d[n]
            elif n < 100:
                return d[n//10*10] + ' ' + d[n%10] if n%10 else d[n//10*10] 
            elif n < 1000:
                return d[n//100] + ' Hundred ' + helper(n%100) if n%100 else d[n//100] + ' Hundred'
            
        res = []
        if num >= 1000000000:
            c, num = divmod(num, 1000000000)
            res.append(d[c])
            res.append(d[1000000000])
        
        if num >= 1000000:
            c, num = divmod(num, 1000000)
            res.append(helper(c))
            res.append(d[1000000])
            
        if num >= 1000:
            c, num = divmod(num, 1000)
            res.append(helper(c))
            res.append(d[1000])
        
        if num > 0:
            res.append(helper(num))
            
        
        return ' '.join(res)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# class Solution:
#     def numberToWords(self, num: int) -> str:
#         if num == 0:
#             return 'Zero'
        
#         res = []
#         d = {
#             1000000000: "Billion",
#             1000000: "Million",
#             1000: "Thousand",
#             100: "Hundred",
#             90: "Ninety",
#             80: "Eighty",
#             70: "Seventy",
#             60: "Sixty",
#             50: "Fifty",
#             40: "Forty",
#             30: "Thirty",
#             20: "Twenty",
#             19: "Nineteen",
#             18: "Eighteen",
#             17: "Seventeen",
#             16: "Sixteen",
#             15: "Fifteen",
#             14: "Fourteen",
#             13: "Thirteen",
#             12: "Twelve",
#             11: "Eleven",
#             10: "Ten",
#             9: "Nine",
#             8: "Eight",
#             7: "Seven",
#             6: "Six",
#             5: "Five",
#             4: "Four",
#             3: "Three",
#             2: "Two",
#             1: "One",
#             0: "Zero",
#         }
        
#         def helper(n):
#             if n <= 20:
#                 return d[n]
#             elif n <100:
#                 return d[n//10*10] + ' ' + d[n%10] if n%10 else d[n//10*10]
#             elif n < 1000:
#                 return d[n//100] + ' Hundred ' + helper(n%100) if n%100 else d[n//100] + ' Hundred'
            
        
#         if num >= 1000000000:
#             c,num = divmod(num, 1000000000)
#             res.append(d[c])
#             res.append(d[1000000000])
        
#         if num >= 1000000:
#             c, num = divmod(num, 1000000)
#             res.append(helper(c))
#             res.append(d[1000000])
            
#         if num >= 1000:
#             c, num = divmod(num, 1000)
#             res.append(helper(c))
#             res.append(d[1000])
        
#         if num > 0:
#             res.append(helper(num))
            
#         return ' '.join(res)