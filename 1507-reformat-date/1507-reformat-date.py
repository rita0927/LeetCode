class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan": '01', 
                 "Feb": '02', 
                 "Mar": '03', 
                 "Apr": '04', 
                 "May": '05', 
                 "Jun": '06', 
                 "Jul": '07', 
                 "Aug": '08', 
                 "Sep": '09', 
                 "Oct": '10', 
                 "Nov": '11', 
                 "Dec": '12'}
        
        d,m,y = date.split()
        d = d[:-2]
        d = '0'+ d if len(d) == 1 else d
        m = month[m]
        return f'{y}-{m}-{d}'
        
        