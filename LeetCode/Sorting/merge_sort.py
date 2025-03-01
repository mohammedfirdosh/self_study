# Merge sort
# TC: O(n * logn)
# SC: O(n)
def mergeSort(arr, start, end):
    if start < end:
        mid = start + (end - start) //2

        mergeSort(arr, start, mid) # Left
        mergeSort(arr, mid +1 , end) # Right

        merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    tmp = list()
    i, j = start, mid +1
    while i <=mid and j <= end:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i +=1
        else:
            tmp.append(arr[j])
            j += 1
    while i<= mid:
        tmp.append(arr[i])
        i += 1
    while j<= end:
        tmp.append(arr[j])
        j += 1
    
    for i in range(len(tmp)):
        arr[i + start] = tmp[i]

if __name__ == '__main__':
    arr = [12, 31, 35, 8, 32, 17]
    print(f"Unsorted list: {arr}")
    n = len(arr)
    start, end = 0, n-1
    mergeSort(arr, start, end)
    print(f"Sorted list: {arr}")
