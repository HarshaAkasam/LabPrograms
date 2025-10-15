import time

def is_valid(v, path, graph):
    if graph[path[-1]][v]==0: return False
    if v in path: return False
    return True

def hamiltonian_cycles(graph):
    n = len(graph)
    path = [0]
    cycles = []

    def backtrack():
        if len(path)==n:
            if graph[path[-1]][path[0]]==1:
                cycles.append(path.copy())
            return
        for v in range(1,n):
            if is_valid(v, path, graph):
                path.append(v)
                backtrack()
                path.pop()

    backtrack()
    return cycles

if __name__=='__main__':
    # sample graph (complete graph of small size)
    n=8
    graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j: graph[i][j]=1
    start = time.time()
    cycles = hamiltonian_cycles(graph)
    end = time.time()
    print(f"Found {len(cycles)} Hamiltonian cycles in {end-start:.6f} sec (note: cycles may be many)")
