#To create a LFU use a Min-heap data structure and 
#use a hash map to search for values fast
import sys

class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmall(Error):
    """Raised whe the input is too small"""
    pass

class Node:
    def __init__(self, key, frequency):
        self.key = key
        self.frequency = frequency
        self.pos = None

class MinHeap:

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1
        self.freqTable = HashTable(10 * maxsize)
        self.posTable = HashTable(10 * maxsize)


    def parent(self, pos):
        return pos//2
    
    def left(self,pos):
        return 2 * pos

    def right(self,pos):
        return (2 * pos) + 1

    def isLeaf(self, pos):
        if pos >= (self.size//2) and pos <= self.size:
            return True
        return False

    def swap(self, fpos, spos):
        self.Heap[fpos].pos = spos
        self.Heap[spos].pos = fpos
        self.posTable.putPos(self.Heap[fpos])
        self.posTable.putPos(self.Heap[spos])
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            if (self.Heap[pos].frequency > self.Heap[self.left(pos)].frequency or self.Heap[pos].frequency > self.Heap[self.right(pos)].frequency):
                if self.Heap[self.left(pos)].frequency < self.Heap[self.right(pos)].frequency:
                    self.swap(pos, self.left(pos))
                    self.minHeapify(self.left(pos))
                else:
                    self.swap(pos, self.right(pos))
                    self.minHeapify(self.right(pos))

    def insert(self, node):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = node
        self.Heap[self.size].pos = self.size
        self.posTable.putPos(self.Heap[self.size])
        self.freqTable.putFreq(node)
        current = self.size

        # print(self.Heap[current].frequency)

        # print(self.Heap[self.parent(current)].frequency)

        # print(self.Heap[self.parent(current)])
        
        # while self.Heap[current].frequency < self.Heap[self.parent(current)]:
        #     self.swap(current, self.parent(current))
        #     current = self.parent(current) 

    def Print(self):
        for i in range(1, (self.size//2)+1):
            parent = self.Heap[i].key
            parentFreq = self.Heap[i].frequency
            try:
                # print("left: ", self.Heap[2 * i])
                left = self.Heap[2 * i].key
                leftFreq = self.Heap[2 * i].frequency
            except IndexError:
                left = None
                leftFreq = ""
            except AttributeError:
                left = None
                leftFreq = ""
            try:
                # print("right: ", self.Heap[2 * i + 1])
                right = self.Heap[2 * i + 1].key
                rightFreq = self.Heap[2 * i + 1].frequency
            except IndexError:
                right = None
                rightFreq = ""
            except AttributeError:
                right = None
                rightFreq = ""

            print("PARENT Key, Freq : " + str(parent) + ", " + str(parentFreq) +" | LEFT Key, Freq : " + str(left) + ", "+ str(leftFreq) + " | RIGHT Key, Freq : " + str(right) + ", " + str(rightFreq))

    def minHeap(self):
        for pos in reange(self.size//2, 0, -1):
            self.minHeapify(pos)

    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        return popped

    def increaseFreq(self, key):
        self.freqTable.increaseFreq(key)
        newFreq = self.freqTable.getFreq(key)
        pos = self.posTable.getPos(key)
        self.Heap[pos] = Node(key, newFreq)



class HashTable:
    def __init__(self, size):
        self.size = size
        self.hashTable = self.createMap()

    def createMap(self):
        return [[] for _ in range(self.size)]

    def putPos(self, node):
        map = self.hashTable[hash(node.key)]
        map.insert(node.key, node.pos)

    def getPos(self, key):
        map = self.hashTable[hash(key)]
        return map[0]

    def putFreq(self, node):
        map = self.hashTable[hash(node.key)]
        map.insert(node.key, node.frequency)

    def getFreq(self, key):
        map = self.hashTable[hash(key)]
        out = map[0]
        return out

    def increaseFreq(self, key):
        map = self.hashTable[hash(key)]
        map[0] += 1

    def put(self, key, heap):
        map = self.hashTable[hash(key) % self.size]
        cacheCall = self.searchCache(key)
        if cacheCall == 'cache hit':
            print('cache hit')
            heap.increaseFreq(key)
        elif cacheCall == 'cache miss':
            print('cache miss')
            node = Node(key, 1)
            map.append(key)
            heap.insert(node)
        heap.minHeapify(1)


        
    def searchCache(self, key):
        map = self.hashTable[hash(key) % self.size]
        miss = True
        for index, out in enumerate(map):
            outKey = out
            if out == key:
                miss = False
                break
        if miss == False:
            return 'cache hit'
        else:
            return 'cache miss'

    def remove(self, key):
        map = self.hahsTable[hash(key) % self.size]
        check = True
        for index, out in enumerate(map):
            outKey = out
            if outKey == key:
                check = False
                break
        if check == False:
            map.pop(index)
        return

    def __str__(self):
        return "".join(str(item) for item in self.hashTable)

if __name__=='__main__':
    
    array = [3,2,5,4,7,10,1,19,17,6,5,7,6,10]
    
    length = 5
    cache = HashTable(length)
    heap = MinHeap(length)
    # cache.put(3,heap)
    # cache.put(4,heap)
    # cache.put(3,heap)
    # heap.Print()

    cache.put(7,heap)
    cache.put(2,heap)
    cache.put(5,heap)
    cache.put(3,heap)
    cache.put(1,heap)

    heap.Print()

    cache.put(2,heap)
    heap.Print()

    cache.put(2,heap)
    heap.Print()

    cache.put(7,heap)
    heap.Print()
    # cache.put(5,heap)
    cache.put(12,heap)

    # heap.freqTable.putNode(Node(4,2))
    # heap.freqTable.putNode(Node(7,3))
    # heap.freqTable.putNode(Node(8,4))
    # heap.freqTable.putNode(Node(9,6))

    # heap.freqTable.increaseFreq(9)

    # print(heap.freqTable.getNode(8))
    # print(heap.freqTable.getNode(9))
    # print(heap.freqTable.getNode(4))

    # i = 0
    # while i < len(array):
    #     cache.put(array[i], heap)
    #     i += 1
    
    heap.Print()
    print(cache)
    
    # heap.Heapsort(array)
    # heap.printHeap()

