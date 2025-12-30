from collections import deque
import heapq

def bfsConnected(src,V,adj,visited,result):
    # make a queue
    queue=deque()
    # mark and insert source in visited and queue
    visited[src]=True
    queue.append(src)
    
    while queue:
        # take out the front of queue sa current, put it in result arr
        curr=queue.pop()
        result.append(curr)
        
        # for each neighbor for current
        for i in adj[curr]:
            # if neighbour not already visited then mark in visited and put it in queue
            if not visited[i]:
                visited[i]=True
                queue.append(i)
        
#BFS TC-> O(V + E) SC-> O(V)
def bfs(adj):
    V=len(adj)
    visited=[False]*V
    result=[]
    
    # loop for disconnected components
    for i in range(V):
        if not visited[i]:
            bfsConnected(i,V,adj,visited,result)
    return result

# TopologicalSort + is Cyclic for directed (Kahns Algorithm )
def topologicalSort(adj):
    V=len(adj)
    indegrees=[0]*V
    result=[]
    queue=deque()
    # visited is to count the alerady visited nodes
    visited=0
    
    # count indegrees
    for i in range(V):
        for neighbour in adj[i]:
            indegrees[neighbour]+=1
            
    # append neighbours with indegrees 0
    for i in range(V):
        if indegrees[i]==0:
            queue.append(i)
    
    while queue:
        curr=queue.pop()
        result.append(curr)
        visited+=1
        
        # for each neighbour of the current node, decrement its indegree by 1
        for neighbour in adj[curr]:
            indegrees[neighbour]-=1
            # if thatt indegree==0 then add to queue
            if indegrees[neighbour]==0:
                queue.append(neighbour)
                
    if visited!=V:
        print('cycle detected in graph')
    return result
        
# djikstras algorithms for shorted path TC-> (V+E)logV SC-> V+E 
def djikstras(adj,src):
    V=len(adj)
    pq=[]
    dist=[max]*V
    dist[src]=0
    # pusing weight and node in pq
    heapq.heappush(pq,(0,src))
    
    while pq:
        currweight,mainNode=heapq.heappop(pq)
        # if current weight for a node is > then weight in dist arr for that node, only then proceed
        if currweight>dist[mainNode]:
            continue
        for neiWeight,neiNode in adj[mainNode]:
            # if dist to reach its parent (main node) + the weight to reach the neigh < the already dist of the node in dist  
            if dist[mainNode]+neiWeight<dist[neiNode]:
                # update with less dist
                dist[neiNode]=dist[mainNode]+neiWeight
                heapq.heappush(pq,(dist[neiNode],neiNode))
    return dist

def DFSconnected(adj,visited,result,src):
    visited[src]=True
    result.append(src)
    # recursive call for all adjecent neighbors that not visited yet
    for i in adj[src]:
        if not visited[i]:
            DFSconnected(adj,visited,result,i)
        
# DFS TC ->  O(V + E) SC-> O(V + E)
def DFS(adj):
    V=len(adj)
    visited=[False]*V
    result=[]
    # to handle disconnected components
    for i in range(V):
        if not visited[i]:
            DFSconnected(adj,visited,result,i)
    return result

def isCyclicInUndirected(adj,visited,src,parent):
    # mark the src true
    visited[src]=True
    # if its adj neighbour not visited then recur for em
    for neighbour in adj[src]:
        if not visited[neighbour]:
           if isCyclicInUndirected(adj,visited,neighbour,src):
               return True
        #    if neighbour visited but not the parent of the current then cycle found
           elif neighbour!=parent:
               return True
    return False

# Cycle detection in undirected using DFS
# returns True if cyce found
def iscyclicDFS(adj):
    V=len(adj)
    visited=[False]*V

    # to handle disconnected components
    for i in range(V):
        if not visited[i]:
            if isCyclicInUndirected(adj,visited,i,-1):
                return True
    return False

# topologicalSort using DFS and Stack
def topoSort(adj,visited,stack,node):
    visited[node]=True
    
    for neighbour in adj[node]:
        if not visited[neighbour]:
            topoSort(adj,visited,stack,neighbour)
    # push node in stack after all its neighbours
    stack.append(node)    
    
def findtopoSort(adj):
    stack=[]
    visited=[False]*len(adj)
    
    for i in range(len(adj)):
        if not visited[i]:
            topoSort(adj,visited,stack,i)
    
    result=[]
    # push stack back 
    while stack:
        result.append(stack.pop())
    return result

def PrimsAlgo(adj):
    pq=[]
    res=[]
    visited=[False]*len(adj)
    
    heapq.heappush(pq,(0,0,0)) #weight,parent,vertex
    
    while pq:
        u,v,w=heapq.heappop(pq)
        
        if visited[v]:
            continue
        
        res.append(u,v,w)
        visited[v]=True
        
        for vertex,weight in adj[v]:
            if not visited[vertex]:
                heapq.heappush(pq,(weight,v,vertex))
    return res[1:]

def BellmanFord(edges,V,src):
    dist=[max]*V
    dist[src]=0
    
    for i in range(V):
        changed=False

        for u,v,w in edges[i]:
               
            if dist[u]+w < dist[v]:
                if i==V-1: # if Negative Weight Cycle
                    return [-1]
                dist[v]=dist[u]+w
                changed=True
                
        if not changed: break
    return dist

def FloydWarshall(edges):
    V=len(edges)
    dist=[max*V]*V
    
    for i in range(V):
        dist[i][i]=0
    
    for u,v,w in edges:
        dist[u][v]=w
    
    for k in range(V):  # k is the intermediate node
        for i in range(V):   # source node
            for j in range(V):       # vertices as destination node
                # minimum distance from src to dest or from src->intermediate->dest
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][i])
    
    for i in range(V):
        if dist[i][i]<0:
            return [-1]
    
    return dist