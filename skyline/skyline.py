
class Solution:
    
    def inRange(self,window_left,window_right,arr):

       if ( arr[0]<=window_right and arr[0]>= window_left):
            return True
       else:
            return False

    def getSkyline(self, buildings):

        result = []
        n = len(buildings)

        if n<1:
            return []

        left, right=0,0
       
        while right < len(buildings):
            this_window=[]
            #this_window.append([buildings[left][0],buildings[left][2]])
            window_left, window_right,window_height= buildings[left][0],buildings[left][1],buildings[left][2]
            #append left most edge
            this_window.append([buildings[left][0],buildings[left][2]])
            # one window size
            while right < n and self.inRange(window_left,window_right,buildings[right]):

                
                # append a new hight point
                if buildings[right][2]>window_height :
                    this_window.append([buildings[right][0],buildings[right][2]])
                    window_height = buildings[right][2]
                # end of previous height	
                elif buildings[right][2]<window_height and window_right<buildings[right][1]:
                    this_window.append([buildings[left][1],buildings[right][2]])
                    window_height = buildings[right][2]
                # update right boundary of current window	
                if buildings[right][1] > window_right:
                    window_right = buildings[right][1]	
                left = right	
                right +=1
            
            # ending point of current window    
            this_window.append([window_right,0])

            print(left,right)
            result.extend(this_window)
                
            left = right

        final_result =[]
        prev = result[0]
        i = 1
        print(result)

        # max height
        while i <len(result):
            max_height = prev[1]
            while i<len(result) and result[i][0]==prev[0]:
                max_height = result[i][1] if result[i][1]>max_height else max_height
                i += 1
            final_result.append([prev[0],max_height]) 
            if i< len(result):
                prev = result[i]

        prev = final_result[0]
        final_result_hat=[]
        i=1
        while i <len(final_result):
            while i<len(final_result) and final_result[i][1]==prev[1]:
                i+=1
            final_result_hat.append([prev[0],prev[1]])       
            if i <len(final_result):
                prev = final_result[i]
        print(final_result_hat)        

        return final_result_hat 


my_sol = Solution()
buildings = [[1,2,1],[1,2,2],[1,2,3]]
result = my_sol.getSkyline(buildings)
print(result)

buildings = [[0,1,3]]
#buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10]]
result = my_sol.getSkyline(buildings)
print(result)

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
#buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10]]
result = my_sol.getSkyline(buildings)

print(result)
print([[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]])



buildings = [[1,2,1],[1,2,2],[1,2,3],[2,3,1],[2,3,2],[2,3,3]]
result = my_sol.getSkyline(buildings)
print(result)
print([[1,3],[3,0]])

            




