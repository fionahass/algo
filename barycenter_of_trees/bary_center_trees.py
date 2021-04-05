from collestions import defaultdict

class Solution:
    def BaryCenterTrees(self,x,y):

        if len(x)<1 or len(y)<1:
            return 0

        # sort edges 
        n = len(x)+1
        g = [[] for i in range(n+1)]
        dp =[ 0 for i in range(n+1)]

        for i in range(len(x)):
            g[x[i]].append(y[i])
            g[y[i]].append(x[i])

        self.ansNode = 0
        self.ansSize = n+1
        self.dfs(1,0,n,dp,g)

        return self.ansNode

    def dfs(child,parent,n,dp,g):

        dp[child] = 1
        max_sub_tree = 0

        for i in g[child]:
            if i==parent:
                continue
            # get all the node in the tree with root i    
            self.dfs(i,child,n,dp,g)
            dp[child]+=dp[i]
            # max sub tree node for child
            max_sub_tree = max(max_sub_tree,dp[i]) 
        # max sub tree node for child from parent
        max_sub_tree = max(max_sub_tree,n-dp[child])

        if max_sub_tree<self.ansSize or (max_sub_tree==self.ansSize and child<self.ansNode):
            self.ansSize = max_sub_tree
            self.ansNode = child


my_sol = Solution()
x = [1,2,2]
y =[2,3,4]
result = my_sol.BaryCenterTrees(x,y)    

