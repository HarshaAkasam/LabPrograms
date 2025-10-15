import time, random, sys
sys.setrecursionlimit(1000000)
def quick_sort(arr):
    if len(arr) <= 1: return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

if __name__ == '__main__':
    arr = [random.randint(0,1000000) for _ in range(150000)]
    start = time.time()
    quick_sort(arr)
    end = time.time()
    print(f"Quick Sort Time: {end-start:.6f} sec")
