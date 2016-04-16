#Topological_Search
graph ={"a": ["b", "c"],
    	"b": [],
    	"c": ["d"],
    	"d": ["b"],
    	"e": ["g", "f", "q"],
    	"g": [],
    	"f": [],
    	"q": []}

def topological(graph):
	result ,nodes,state = [],set(graph),{}
	def dfs(node):
		state[node] = 0
		for c in graph.get(node):
			c_state =state.get(c) 
			if c_state==0: raise Exception('Loop')
			if c_state==1: continue
			nodes.discard(c)
			dfs(c)
		result.append(node)
		state[node] = 1
	while nodes:
		dfs(nodes.pop())
	return result[::-1]

print topological(graph)