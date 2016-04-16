#Graph.py
graph ={"a": ["b", "c"],
    	"b": [],
    	"c": ["d"],
    	"d": ["b",'e'],
    	"e": ["g", "f", "q"],
    	"g": ["d"],
    	"f": [],
    	"q": []}

graph_1 = [[4], 
		   [2],
		   [3,6,7],
		   [4],
		   [1,5,2],
		   [0],
		   [7],
		   [1,3]]

#------------------------------------

def all_pathes(graph, s, d , path=[]):
	path=path+[s]
	if s == d:
		return [path]
	paths = []
	for node in graph[s]:
		if node not in path:
			paths.extend(all_pathes(graph, node, d , path))
	return paths

print all_pathes(graph_1,4,7)

#------------------------------------
def minimum_spanning_trees(graph):
	graph = sorted(graph, key=lambda x:x[2])
	visited_v = []
	path =[]
	for e in graph: 
		if e[0] and e[1] not in visited_v:
			path.append(e)
			visited_v.extend((e[0],e[1]))
	return path
#print minimum_spanning_trees([['a','b',1],['a','c',3],['b','d',1],['b','c',3],['d','c',1]])
#O(E log v)

#------------------------------------


def Cycle_directed(graph):
		result , visited,nodes = [],{},set(graph)
		stack=[]
		def dfs(node):
			visited[node]=0
			for n in graph.get(node):
				if visited.get(n)==0: 
					#stack.append(n)
					print ((stack+[n],'Cycel'))
					del stack[:]
					continue
				if visited.get(n)==1: continue
				stack.append(n)
				nodes.discard(n)
				dfs(n)
			visited[node]=1
			result.append(node)

		while nodes:
			 dfs(nodes.pop())
		return result


#print Cycle_directed(graph_1)
#------------------------------------


def graph_dfs(graph,start):
	result ,nodes,state = [],set(graph),{}

	def dfs(node):
		state[node]=0
		for e in graph.get(node):
			print e
			if e in state:
				continue
			nodes.discard(e)
			dfs(e)
		result.append(node)
		state[node]==1

	#while nodes:
	dfs(start)
	return result

	
import Queue
def graph_bfs(graph,start):
	Q,visited=Queue.Queue(),[]
	Q.put(start)
	while not Q.empty():
		node = Q.get()
		if node not in visited:
			visited.append(node)
			for n in graph.get(node):
				 if n not in visited:
				 	Q.put(n)
	return visited

#print graph_dfs(graph,'a')
#print graph_bfs(graph_1,'2')

#-------------------------------------------
def minimum_paths(graph):
	nodes = set(graph)
	distnce =[[0 for _ in len(nodes)] for n in len(nodes)] 
	path   = [[0 for _ in len(nodes)] for n in len(nodes)]

	






