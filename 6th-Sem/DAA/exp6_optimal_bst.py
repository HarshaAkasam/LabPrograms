import time
def optimal_bst(keys, freq):
    n = len(keys)
    dp = [[0]*n for _ in range(n)]
    sumf = [[0]*n for _ in range(n)]
    for i in range(n):
        dp[i][i] = freq[i]
        sumf[i][i] = freq[i]
    for L in range(2, n+1):
        for i in range(0, n-L+1):
            j = i+L-1
            sumf[i][j] = sumf[i][j-1] + freq[j]
            dp[i][j] = float('inf')
            for r in range(i, j+1):
                left = dp[i][r-1] if r>i else 0
                right = dp[r+1][j] if r<j else 0
                cost = left + right + sumf[i][j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
    return dp[0][n-1]

if __name__=='__main__':
    # example
    keys = [10,12,20,35,46]
    freq = [34,8,50,21,16]
    start = time.time()
    cost = optimal_bst(keys, freq)
    end = time.time()
    print(f"Optimal BST cost: {cost}, Time: {end-start:.6f} sec")
