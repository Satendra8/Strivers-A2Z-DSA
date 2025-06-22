class MaxHeap:
    def __init__(self):
        self.arr = []
        self.size = 0

    def swap(self, index1, index2):
        self.arr[index1], self.arr[index2] = self.arr[index2], self.arr[index1]
        return

    def insert(self, value):
        """
        Time Complexity: O(logN)
        Space Complexity: O(1)
        """
        print(f"{value} inserted in heap")
        self.arr.append(value)
        curr = self.size
        self.size += 1

        while curr > 0 and self.arr[(curr-1)//2] < self.arr[curr]:
            self.swap((curr-1)//2, curr)
            curr = (curr-1)//2
        return

    def heapify(self, index):
        parent = index
        left = 2 * parent + 1
        right = 2 * parent + 2

        if left < self.size and self.arr[parent] < self.arr[left]:
            self.swap(parent, left)
            parent = left

        if right < self.size and self.arr[parent] < self.arr[right]:
            self.swap(parent, right)
            parent = right

        if parent != index:
            self.heapify(parent)
        return

    def delete(self):
        """
        Time Complexity: O(logN)
        Space Complexity: O(logN)
        """
        if self.size == 0:
            print("Heap is empty")
            return
        print(f"{self.arr[0]} is deleted")
        self.arr[0] = self.arr[self.size-1]
        self.arr.pop()
        self.size -= 1
        if self.size == 0:
            print("Heap is empty")
            return
        self.heapify(0)


class MinHeap:
    def __init__(self):
        self.arr = []
        self.size = 0

    def swap(self, index1, index2):
        self.arr[index1], self.arr[index2] = self.arr[index2], self.arr[index1]
        return

    def insert(self, value):
        """
        Time Complexity: O(logN)
        Space Complexity: O(1)
        """
        print(f"{value} inserted in heap")
        self.arr.append(value)
        curr = self.size
        self.size += 1

        while curr > 0 and self.arr[(curr-1)//2] > self.arr[curr]:
            self.swap((curr-1)//2, curr)
            curr = (curr-1)//2
        return

    def heapify(self, index):
        parent = index
        left = 2 * parent + 1
        right = 2 * parent + 2

        if left < self.size and self.arr[parent] > self.arr[left]:
            self.swap(parent, left)
            parent = left

        if right < self.size and self.arr[parent] > self.arr[right]:
            self.swap(parent, right)
            parent = right

        if parent != index:
            self.heapify(parent)
        return

    def delete(self):
        """
        Time Complexity: O(logN)
        Space Complexity: O(logN)
        """
        if self.size == 0:
            print("Heap is empty")
            return
        print(f"{self.arr[0]} is deleted")
        self.arr[0] = self.arr[self.size-1]
        self.arr.pop()
        self.size -= 1
        if self.size == 0:
            print("Heap is empty")
            return
        self.heapify(0)

h = MinHeap()
h.insert(7)
h.insert(5)
h.insert(8)
h.insert(9)
h.delete()
h.delete()
h.delete()
h.delete()
h.delete()
h.insert(3)
print(h.arr)