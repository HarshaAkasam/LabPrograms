import time, random
def merge(left, right):
    res, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i]); i += 1
        else:
            res.append(right[j]); j += 1
    res.extend(left[i:]); res.extend(right[j:])
    return res

def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr)//2
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))

if __name__ == '__main__':
    arr = [random.randint(0,1000000) for _ in range(200000)]
    start = time.time()
    merge_sort(arr)
    end = time.time()
    print(f"Merge Sort Time: {end-start:.6f} sec")
