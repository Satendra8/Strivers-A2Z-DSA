


def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]
    return

def heapify(arr, i, n):
    parent = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[parent]:
        parent = left

    if right < n and arr[right] > arr[parent]:
        parent = right

    if(parent != i):
        swap(arr, parent, i)
        heapify(arr, parent, n)
    return

def buildMaxHeap(arr):
    """
    1. Don't care about the input just build heap from normal array
    Time Complexity: O(N)
    Space Complexity: O(logN) # if while loop is used in heapify then space complexity will be O(1)

    """
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        heapify(arr, i, n)
    return


def heapSort(arr):
    """
    1. create Max Heap
    2. replace first with last
    3. heapify the first element to move it to its correct position
    Time Complexity: O(N) + O(NlogN)
    Space Complexity: O(logN) #use while loop to reduce this
    """
    size = len(arr)
    for i in range(size-1, -1, -1):
        swap(arr, 0, i)
        heapify(arr, 0, i)



arr = [30, 24, 20, 23, 19, 12, 18, 22, 14, 17, 15]
heapSort(arr)
print(arr)