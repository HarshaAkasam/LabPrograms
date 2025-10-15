import time
from functools import lru_cache

def tsp(dist):
    n = len(dist)
    ALL = (1<<n) - 1

    @lru_cache(None)
    def dp(mask, pos):
        if mask == ALL:
            return dist[pos][0] or float('inf')
        ans = float('inf')
        for city in range(n):
            if mask & (1<<city) == 0 and dist[pos][city] != 0:
                ans = min(ans, dist[pos][city] + dp(mask | (1<<city), city))
        return ans

    return dp(1,0)

if __name__=='__main__':
    # small n due to 2^n complexity
    n = 12
    import random
    dist = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j: dist[i][j] = random.randint(1,100)
    start = time.time()
    cost = tsp(dist)
    end = time.time()
    print(f"TSP (DP) cost (n={n}): {cost}, Time: {end-start:.6f} sec")
