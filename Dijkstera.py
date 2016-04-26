def dijkstra(edges, s, d):
    g = defaultdict(list)
    for l,r,c in edges:
        g[l].append((c,r))
    
    q, seen = [], []
    heappush(q,[0,s,[]])
    #print q
    while q:
        [cost,v1,path] = heappop(q)

        if v1 not in seen:
            seen.append(v1)
            path=path+[v1]
            
            if v1 == d: return (cost, path) 

            for c, v2 in g.get(v1, ()):
                if v2 not in seen:
                    heappush(q, [cost+c, v2, path])
        #print q
        #print path,'\n'
    return float("inf")