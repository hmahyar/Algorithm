#Graph.py
graph ={"a": ["b", "c"],
    	"b": [],
    	"c": ["d"],
    	"d": ["b"],
    	"e": ["g", "f", "q"],
    	"g": [],
    	"f": [],
    	"q": []}

graph = {
    1: [2,11],
    2: [3],
    11: [12],
    12: [13]
    }

def directed_count_components(graph):
	stack,nodes = [],set(graph)
	def dfs(n):
		visited = []
		stack.append(n)
		while stack:

			node = stack.pop()
			if node not in visited:
				visited.append(node)
				nodes.discard(node)
				if graph.get(node):stack.extend([_ for _ in graph.get(node) if _ not in visited])
				
		return visited[::-1]
	while nodes:
		print dfs(nodes.pop())

directed_count_components(graph)


def undirected_count_components(n, edges):
	def root(ids ,i):
		if i==ids[i]:
			return i
		return root(ids,ids[ids[i]])

	ids = [_ for _ in range(n)]
	for edge in edges:
		i = root(ids,edge[0])
		j = root(ids,edge[1])
		ids[i]=j

	result,i  = 0,0
	while i <n:
		if ids[i]==i:
			result+=1
		i+=1
	return result
print undirected_count_components(6,[[0, 1], [0, 2],[3, 4],[2,5]])
