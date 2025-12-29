# fibonacci
def fibTopDown(T,dp):
    if T<2: return T
    if dp[T]!=-1: return dp[T]
    
    dp[T]=fibTopDown(T-1,dp)+fibTopDown(T-2,dp)
    return dp[T]

def fibBottomUp(T):
    dp=[]
    dp[0]=0
    dp[1]=1
    
    for i in range(2,T):
        dp[i]=dp[i-1]+dp[i-2]
    return dp[T]
   
def ClimbingStairsTD(cost,n,dp):
    if n==0: return cost[0]
    if n==1: return cost[1]
    # check from dp
    if dp[n]!=-1: return dp[n]
    # insert in dp
    dp[n]=cost[n]+min(ClimbingStairsTD(cost,n-1,dp),ClimbingStairsTD(cost,n-2,dp))
    return dp[n]

def ClimbingStairsBU(cost,n):
    dp=[]
    # base case
    dp[0]=cost[0]
    dp[1]=cost[1]
    # insert dp in recur relation from topDown
    for i in range(2,n):
        dp[i]=cost[i]+min(ClimbingStairsTD(cost,i-1,dp),ClimbingStairsTD(cost,i-2,dp))
    return dp[n]
# climbingStairs (frogJumping)  
def ClimbingStairsMain(cost):
    n=len(cost)
    dp=[-1]*n
    answer=min(ClimbingStairsTD(cost,n-1,dp),ClimbingStairsTD(cost,n-2,dp))
    # answer=ClimbingStairsBU(cost,n)
    return answer

def MaxCoinsTD(nums,T,dp):
    minimum=float('inf')
    # basecase
    if T==0: return 0
    if T<0: return float('inf')
    if dp[T]!=-1: return dp[T]
    
    for i in range(len(nums)):
        # ans stores the mini return val for specific coin
        ans=MaxCoinsMain(nums,T-nums[i],dp)
        if ans!=float('inf'): minimum=min(minimum,1+ans)
    dp[T]=minimum
    return dp[T]

def MaxCoinsBU(nums,T):
    #basecase
    n=len(nums)
    dp=[float('inf')]*n+1
    dp[0]=0
    
    for i in range(1,T):
        for j in range(n):
            # base case checking if it is valid to use (not out of bound) 
            if(i-nums[j]>=0 and dp[i-nums[j]!=float('inf')]):
                # find minimum from dp[T]=(prev number of coins used for target) and dp[i-nums[j]]=(current coin used for the target)
                dp[i]=min(dp[T],1+dp[i-nums[j]])
    if dp[T]!=float('inf'): return -1
    else: return dp[T]    
        
# maxNumberofCoins
def MaxCoinsMain(nums):
    n=len(nums)
    target=0
    dp=[-1]*n
    answer=MaxCoinsTD(nums,target,dp)
    # answer=MaxCoinsBU(nums,target)
    if answer==float('inf'): return -1
    else: return answer
    
def RodCuttingTD(rod,x,y,z,dp):
    if rod==0: return 0
    if rod<0: return float('-inf')
    if dp[rod]!=-1: return dp[rod]
    
    a=RodCuttingTD(rod-x,x,y,z)+1
    b=RodCuttingTD(rod-y,x,y,z)+1
    c=RodCuttingTD(rod-z,x,y,z)+1
    
    dp[rod]=max(a,b,c)
    return dp[rod]
    
def RodCuttingBU(rod,x,y,z):
    dp=[float('-inf')]*len(rod)+1
    dp[0]=0
    
    for i in range(rod):
        # if that range is valid then get max of prev else the current we are calculating+1
        if i-x>=0: dp[i]=max(dp[i],dp[i-x]+1)
        if i-y>=0: dp[i]=max(dp[i],dp[i-y]+1)
        if i-z>=0: dp[i]=max(dp[i],dp[i-z]+1)
    
    if dp[rod]<0: return 0
    else: return dp[rod]

# rodCutting
def RodCuttingMain(rod):
    x,y,z=5,2,1
    dp=[-1]*(len(rod)+1)
    answer=RodCuttingTD(rod,x,y,z,dp)
    # answer=RodCuttingBU(rod,x,y,z)
    return answer

def knapsack01TD(W,V,n,cap,dp):
    # basecase
    if n==0:
        if W[0]<cap: 
            return V[0]
        else:
            return 0
    if dp[n][cap]!=-1:
        return dp[n]
    # if current Weight is < cap then add its val + recur it with n-1 and cap-current weight used
    if W[n]<cap:
        include=V[n]+knapsack01TD(W,V,n-1,cap-W[n],dp)
    exclude=knapsack01TD(W,V,n-1,cap,dp)
    
    dp[n][cap]=max(include,exclude)
    return dp[n][cap]
    
def  knapsack01BU(W,V,n,cap):
    dp=[-1][-1]*len(cap)+1
    # basecase (initializing dp)
    for i in range(cap):
        if W[0]<cap:
            dp[0][i]=V[0]
        else:
            dp[0][i]=0
    
    for index in range(1,n):
        for capacity in range(cap):
            if W[index]<capacity:
                include=V[index]+dp[index-1][capacity-W[index]]
            exclude=dp[index-1][capacity]
        dp[index][capacity]=max(include,exclude)
        
    return dp[n-1][cap]    
# 0/1 knapsack problem
def knapsack01Main(W,V,capacity):
    dp=[-1][-1]*len(capacity)+1
    return knapsack01TD(W,V,len(W)-1,capacity,dp)
    # return knapsack01BU(W,V,len(W)-1,capacity)
    
def unboundedknapsackTD(rodlen,lengthsArr,PricesArr,n,dp):
    if n<0 or rodlen==0:
        return 0
    if dp[n][rodlen]!=-1:
        return dp[n][rodlen]
    
    notTake=unboundedknapsackTD(rodlen,lengthsArr,PricesArr,n-1,dp)
    if lengthsArr[n]<rodlen:
        # unbounded means by taking a specific length then we donot decrease the "n" while not tsking it then we do "n-1"
        Take=unboundedknapsackTD(rodlen-lengthsArr[n],lengthsArr,PricesArr,n,dp)+PricesArr[n]
    
    dp[n][rodlen]=max(Take,notTake)
    return dp[n][rodlen]

def unboundedknapsackBU(rodlen,lengthsArr,PricesArr,n):
    dp=[-1][-1]*len(rodlen)+1
    # initializing dp with some formula base idk
    for i in range(lengthsArr[0],rodlen):
        dp[0][i]=i/(lengthsArr[0])*PricesArr[0]
        
    for i in range(1,n-1):
        for j in range(rodlen):
            if lengthsArr[i]<j:
                # here we included 'dp[i]' instead of doing 'dp[i-1]'
                include=PricesArr[i]+dp[i][j-rodlen[i]]
            exclude=dp[i-1][j]
        dp[i][j]=max(exclude,include)
        
    return dp[n-1][rodlen]
                
#unboundend knapsack (rod cutting)
def unboundedknapsackMain(rodlength,lengths,prices):
    dp=[-1][-1]*len(lengths)
    return unboundedknapsackTD(rodlength,lengths,prices,len(lengths)-1,dp)
    # return unboundedknapsackBU(rodlength,lengths,prices,len(lengths)-1)