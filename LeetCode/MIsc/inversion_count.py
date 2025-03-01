# Inversion count
def mergeSort(arr, start, end):
    if start < end:
        mid = start + (end - start) //2

        left_count = mergeSort(arr, start, mid) # Left
        right_count = mergeSort(arr, mid +1 , end) # Right

        merge_count = merge(arr, start, mid, end)
        return left_count + right_count + merge_count
    return 0

def merge(arr, start, mid, end):
    tmp = list()
    i, j = start, mid +1
    count = 0
    while i <=mid and j <= end:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i +=1
        else:
            tmp.append(arr[j])
            j += 1
            count += mid - i +1
    while i<= mid:
        tmp.append(arr[i])
        i += 1
    while j<= end:
        tmp.append(arr[j])
        j += 1
    
    for i in range(len(tmp)):
        arr[i + start] = tmp[i]
    return count

if __name__ == '__main__':
    arr = [6,3, 5, 2, 7] # 5
    arr = [1, 3, 5, 10, 2, 6, 8, 9] # 6   
    print(f"Unsorted list: {arr}")
    n = len(arr)
    start, end = 0, n-1
    inversion_count = mergeSort(arr, start, end)
    print(f"Sorted list: {arr}")
    print(f"Inversion count: {inversion_count}")
