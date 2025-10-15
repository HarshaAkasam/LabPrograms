import time

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    arr = list(range(10_000_000))  # large array to measure time
    target = arr[-1]
    start = time.time()
    idx = binary_search(arr, target)
    end = time.time()
    print(f"Index: {idx}, Time: {end - start:.6f} sec")
