import time

def graph_coloring(graph, m):
    n = len(graph)
    colors = [0]*n
    solutions = []

    def valid(v, c):
        for u in range(n):
            if graph[v][u] and colors[u]==c: return False
        return True

    def backtrack(v):
        if v==n:
            solutions.append(colors.copy()); return True
        for c in range(1, m+1):
            if valid(v,c):
                colors[v]=c
                backtrack(v+1)
                colors[v]=0
        return False

    backtrack(0)
    return solutions

if __name__=='__main__':
    # simple graph: triangle + tail
    graph = [
        [0,1,1,0],
        [1,0,1,1],
        [1,1,0,0],
        [0,1,0,0]
    ]
    m = 3
    start = time.time()
    sols = graph_coloring(graph, m)
    end = time.time()
    print(f"Found {len(sols)} colorings with {m} colors in {end-start:.6f} sec")
