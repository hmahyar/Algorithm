#find_path

edges = [
        ['A', 'B', 7],
        ['A', 'D', 5],
        ['B', 'C', 8],
        ['B', 'D', 9],
        ['B', 'E', 7],
        ['C', 'E', 5],
        ['D', 'E', 15],
        ['D', 'F', 6],
        ['E', 'F', 8],
        ['E', 'G', 9],
        ['F', 'G', 11]
    ]
graph = {0:[4], 
		   1:[2],
		   2:[3,6,7],
		   3:[4],
		   4:[1,5,2],
		   5:[0],
		   6:[7],
		   7:[1,3]}
from collections import defaultdict
from heapq import *
 #O(|V|+|E|log|V|)   
def dijkstra(graph,s,d):
    
    #convert ot adjecancy List
    g = defaultdict(list)
    for s_,d_,c_ in graph:
        g[s_].append([c_,d_])  
    
    q,visited =[[0,s,[]]],[]
    while q:
        cost,node , path = heappop(q)
        if node not in visited:
            visited.append(node)
            path= path+[node]

            if node ==d:  return cost,path
            #if len(g)==len(visited):return path,len(g),len(visited)

            for c,child in g.get(node):
                if child not in visited:
                    heappush(q,[(cost+c),child,path]) 
    return 'No path'


print dijkstra(edges, "A", "G")
	


def find_all_pathes(graph,s,d,path=[]):
	path = path+[s]
	if s ==d:
		
		return [path]
	pathes=[]
	for node in graph.get(s):
		if node not in path:
			#print 1,
			pathes.extend(find_all_pathes(graph,node,d,path))
	return pathes

#print find_all_pathes(graph,4,7)