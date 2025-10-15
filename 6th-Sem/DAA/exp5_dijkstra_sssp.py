import time, heapq
def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start]=0
    pq=[(0,start)]
    while pq:
        d,u = heapq.heappop(pq)
        if d>dist[u]: continue
        for v,w in graph[u].items():
            nd = d+w
            if nd < dist[v]:
                dist[v]=nd; heapq.heappush(pq,(nd,v))
    return dist

if __name__=='__main__':
    # generate weighted graph
    import random
    n=1000
    graph={i:{} for i in range(n)}
    for i in range(n):
        for j in range(3): # sparse
            v = random.randint(0,n-1)
            if v==i: continue
            graph[i][v] = random.randint(1,100)
    start = time.time()
    dist = dijkstra(graph, 0)
    end = time.time()
    print(f"Dijkstra Time: {end-start:.6f} sec, sample dist to 1: {dist.get(1)}")
