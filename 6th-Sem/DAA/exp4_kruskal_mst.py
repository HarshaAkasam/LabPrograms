import time
class DSU:
    def __init__(self,n):
        self.parent=list(range(n)); self.rank=[0]*n
    def find(self,x):
        while self.parent[x]!=x:
            self.parent[x]=self.parent[self.parent[x]]
            x=self.parent[x]
        return x
    def union(self,a,b):
        ra, rb = self.find(a), self.find(b)
        if ra==rb: return False
        if self.rank[ra]<self.rank[rb]: self.parent[ra]=rb
        elif self.rank[rb]<self.rank[ra]: self.parent[rb]=ra
        else:
            self.parent[rb]=ra; self.rank[ra]+=1
        return True

def kruskal(n, edges):
    edges = sorted(edges, key=lambda x: x[2])
    dsu = DSU(n)
    mst=[]
    for u,v,w in edges:
        if dsu.union(u,v):
            mst.append((u,v,w))
    return mst

if __name__ == '__main__':
    # create a random dense graph
    import random
    n = 200
    edges = []
    for i in range(n):
        for j in range(i+1, min(n, i+10)):
            edges.append((i,j, random.randint(1,1000)))
    start = time.time()
    mst = kruskal(n, edges)
    end = time.time()
    print(f"MST edges: {len(mst)}, Time: {end-start:.6f} sec")
