class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        

        if len(flights)<0:
            return -1

        # time complexity O(nlog)
        sort_flights = sorted(flights,key=lambda x:x[0])
        self.min_fee = float("inf")


        # time complexity K*len(flights)

        def dfs(n,flights,src,dst,K,fee):

            if src==dst:
                self.min_fee = min(self.min_fee, fee)
                return 
            elif K==0:
                return  

            i,m=0,len(flights)
            while (i<m) and (flights[i][0]!=src):
                i+=1

            while i<m and (flights[i][0]==src):
                #print("searching, ",flights[i][1],dst,fee+flights[i][2])
                dfs(n,flights,flights[i][1],dst,K-1,fee+flights[i][2])    
                i+=1

            return
            

        dfs(n,sort_flights,src,dst,K+1,0)

        return self.min_fee


    def flystop(self,n,flight_map,dst,fee_schedule):
    
       # fly with two stops only

       fee_with_stop = [float('inf')]*n 

       for i in range(n):
           # start point->dst, stop via i
            for route in flight_map[i]:
                   stop = route[0]
                   fee = route[1]
                   if fee_schedule[i]!=float('inf'):
                       # fly via stop at i v.s. fly to stop
                       fee_with_stop[stop] = min(min(fee_schedule[i]+fee, fee_schedule[stop]),fee_with_stop[stop])
           

       self.min_fee = min(self.min_fee,fee_with_stop[dst])           

       return fee_with_stop 


    def findCheapestPriceDP(self, n, flights, src,dst, K):              

        # time complexity (len(flights)^K)


        flight_map = {}
        fee_with_stop =[float('inf')]*n 
        self.min_fee = float('inf')

        
        for route in flights:
            
            start = route[0]
            end   = route[1]
            fee   = route[2]

            if not start in flight_map.keys():
                flight_map[start] = []
            
            flight_map[start].append((end,fee))


            if start == src:
                fee_with_stop[end] = fee

        print(flight_map[1])




        # if K==0
        if src in flight_map.keys():
            routes = flight_map[src]
            for route  in routes:
                if route[0]==dst:
                        self.min_fee = route[1]
        
        print(fee_with_stop)
        for i in range(K):
            fee_with_stop = self.flystop(n,flight_map,dst,fee_with_stop)


        return self.min_fee    


            




# n = 3
# edges = [[0,1,100],[1,2,100],[0,2,500]]
# src = 0
# dst = 2
# k = 1
my_sol = Solution()
# result = my_sol.findCheapestPriceDP(n,edges,src,dst,k)      
# print(result)


# n=3
# edges =[[0,1,100],[1,2,100],[0,2,500]]
# src=0
# dst=2
# k=0
# result = my_sol.findCheapestPriceDP(n,edges,src,dst,k)      
# print(result)


# n=3
# edges=[[0,1,2],[1,2,1],[2,0,10]]
# src=1
# dst=2
# k=1
# result = my_sol.findCheapestPriceDP(n,edges,src,dst,k)      
# print(result)

# n=17
# edges = [[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]]
# src =13
# dst =4
# k=13
# my_sol = Solution()
# result = my_sol.findCheapestPriceDP(n,edges,src,dst,k)    
# print(result)

n=15
edges=[[10,14,43],[1,12,62],[4,2,62],[14,10,49],[9,5,29],[13,7,53],[4,12,90],[14,9,38],[11,2,64],[2,13,92],[11,5,42],[10,1,89],[14,0,32],[9,4,81],[3,6,97],[7,13,35],[11,9,63],[5,7,82],[13,6,57],[4,5,100],[2,9,34],[11,13,1],[14,8,1],[12,10,42],[2,4,41],[0,6,55],[5,12,1],[13,3,67],[3,13,36],[3,12,73],[7,5,72],[5,6,100],[7,6,52],[4,7,43],[6,3,67],[3,1,66],[8,12,30],[8,3,42],[9,3,57],[12,6,31],[2,7,10],[14,4,91],[2,3,29],[8,9,29],[2,11,65],[3,8,49],[6,14,22],[4,6,38],[13,0,78],[1,10,97],[8,14,40],[7,9,3],[14,6,4],[4,8,75],[1,6,56]]
src=1
dst=4
k=10
result = my_sol.findCheapestPriceDP(n,edges,src,dst,k)      
print(result)

