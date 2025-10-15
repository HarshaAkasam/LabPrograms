import time
def solve_n_queens(n):
    solutions = []
    cols = set(); pos_diag = set(); neg_diag = set()
    board = [-1]*n

    def backtrack(r):
        if r==n:
            solutions.append(board.copy()); return
        for c in range(n):
            if c in cols or (r+c) in pos_diag or (r-c) in neg_diag: continue
            cols.add(c); pos_diag.add(r+c); neg_diag.add(r-c); board[r]=c
            backtrack(r+1)
            cols.remove(c); pos_diag.remove(r+c); neg_diag.remove(r-c)

    backtrack(0)
    return solutions

if __name__=='__main__':
    n=8
    start = time.time()
    sols = solve_n_queens(n)
    end = time.time()
    print(f"Found {len(sols)} solutions for {n}-Queens in {end-start:.6f} sec")
