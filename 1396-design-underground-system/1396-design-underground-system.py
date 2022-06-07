class UndergroundSystem:

    def __init__(self):
        self.checkin_data = {}
        self.journey_data = defaultdict(lambda: [0,0])

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin_data[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.checkin_data[id]
        time = t - start_time
        avg_time, count = self.journey_data[(start_station, stationName)]
        avg_time = (avg_time * count + time)/(count + 1)
        self.journey_data[(start_station, stationName)] = [avg_time, count + 1]


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.journey_data[(startStation, endStation)][0]



# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)



# # store the average time in journey data instead of sum to avoid overflow

#     def __init__(self):
#         self.check_in_data = {}
#         self.journey_data = defaultdict(lambda: [0,0])

        

#     def checkIn(self, id: int, stationName: str, t: int) -> None:
#         self.check_in_data[id] = [stationName, t]

        

#     def checkOut(self, id: int, stationName: str, t: int) -> None:
#         start_station, start_time = self.check_in_data[id]
#         time = t - start_time
#         average, count = self.journey_data[(start_station, stationName)]
#         self.journey_data[(start_station, stationName)] = [(average * count + time)/(count + 1), count + 1]



#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         return self.journey_data[(startStation, endStation)][0]






# O(1)
# O(P + S^2): P is the number of passengers, S is the number os stations. O(P) for the check_in hashmap, one entry for each passenger. O(S^2) for journey hashmap. There're S station to start, each station can go to S stations (including itself, O(S^2 - S) = O(S^2) ). 



# class UndergroundSystem:

#     def __init__(self):
#         self.check_in_data = {}
        
#         # pass lambda as default_factory argument, the value will be returned by default if the key doesn't exist 
#         self.journey_data = defaultdict(lambda: [0,0])
        

#     def checkIn(self, id: int, stationName: str, t: int) -> None:
#         self.check_in_data[id] = [stationName, t]
        

#     def checkOut(self, id: int, stationName: str, t: int) -> None:
#         start_station, start_time = self.check_in_data[id]
     
#         self.journey_data[(start_station, stationName)][0] += (t - start_time)
#         self.journey_data[(start_station, stationName)][1] += 1


#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         time, count = self.journey_data[(startStation, endStation)]
#         return time/count
        