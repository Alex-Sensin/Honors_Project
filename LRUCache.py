import random
import sys
import array as arr

class Node:
    def __init__(self, key):
        self.key = key
        self.value = key
        self.next = None
        self.front = None

class LinkedList:
    def __init__(self, capacity):
        self.head = None
        self.capacity = capacity
        self.tail = None
        self.size = 0

    def push(self, newKey):
        newNode = Node(newKey)
        newNode.next = self.head
        if self.head == None:
            self.tail = newNode
        self.head = newNode
        if self.head != self.tail:
            self.head.next.front = self.head
        self.size += 1
        hashDelete = self.nodeCapacity()
        return hashDelete

    def delete(self, newKey):
        tempNode = self.head
        if newKey == self.head.key:
            self.head = self.head.next
            self.head.front = None
            tempNode = None
            self.size -=1
            return

        if newKey == self.tail.key:
            self.tail = self.tail.front
            self.tail.next = None
            tempNode = None
            self.size -=1
            return

        for i in range(self.capacity):
            tempNode = tempNode.next
            if tempNode == None:
                return
            elif tempNode.key == newKey:
                break

        if tempNode is None:
            return
        if tempNode.next is None:
            return

        next = tempNode.next
        front = tempNode.front
        front.next = next
        next.front = front
        self.size -=1

    def nodeCapacity(self):
        if self.size > self.capacity:
            hashDelete = self.deleteTail()
        else:
            hashDelete = None
        return hashDelete

    def deleteTail(self):
        tempKey = self.tail.key
        temp = self.tail.front
        self.tail = None
        self.tail = temp
        self.tail.next = None
        return tempKey

    def printList(self):
        temp = self.head
        count = 1
        while (temp):
            endString = " "
            if (count % 10) == 0:
                endString = "\n"
            else:
                endString = " "
            print (temp.value, end =endString)
            temp = temp.next
            count += 1
        print()

    def setNodeToHead(self, key):
        self.delete(key)
        newNode = Node(key)
        newNode.next = self.head
        self.head = newNode
        if self.head != self.tail:
            self.head.next.front = self.head
        self.size +=1
        


class HashTable:
    def __init__(self, size):
        self.size = size
        self.hashTable = self.createMap()

    def createMap(self):
        return [[] for _ in range(self.size)]

    def put(self, key, list):
        map = self.hashTable[hash(key) % self.size]
        cacheCall = self.searchCache(key)
        print(cacheCall)
        if cacheCall == 'cache hit':
            list.setNodeToHead(key)    #makes the node in the linked list the head of the linked list
        elif cacheCall == 'cache miss':
            map.append(key)
            hashDelete = list.push(key)
            if hashDelete != None:
                self.remove(hashDelete)

    def searchCache(self, key):
        map = self.hashTable[hash(key) % self.size]
        miss = True
        for index, out in enumerate(map):
            outKey = out
            if out == key:
                miss = False
                break
        if miss == False:
            return "cache hit"
        else:
            return "cache miss"

    def remove(self, key):
        map = self.hashTable[hash(key) % self.size]
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

class UserInterface:

    def __init__(self):
        hashMap, list = self.createCache()
        self.UserOptions(hashMap, list)
    
    def createCache(self):
        print("Welcome to the LRU Cache")
        print("This Cache is designed to take in integers only")
        capCheck = False
        while not capCheck:
            cap = input("What is the capacity of the Cache? \n")
            try:
                intCap = int(cap)
                if intCap > 1:
                    capCheck = True
                else:
                    print("Please choose a larger Cache capacity")
            except ValueError:
                print("Please choose a number")

        hashMap = HashTable(intCap)
        list = LinkedList(hashMap.size)
        return hashMap, list


    def UserOptions(self, hashMap, list):
        print("Your Cache has been created")

        end = False
        while (not end):
            command = input("Enter a command or press 'h' for a list of commands\n")
            if command == 'h':
                print("-------------------------------------------------------------")
                print("Press 'a' to input multiple values into the cache")
                print("Press 'b' to input a single value into the cahce")
                print("Press 'p' to print the contents of the cache")
                print("Press 'ph' to print the contents of the hash map")
                print("Press 'q' to quit")
                print("Press 'h' for the list of command again")
                print("-------------------------------------------------------------")
            elif command == 'q':
                end = True
            elif command == 'a':
                quit = False
                while not quit:
                    inValue = input()
                    if inValue == 'q' or inValue == 'quit':
                        quit = True
                        break
                    try:
                        intValue = int(inValue)
                        hashMap.put(intValue,list)
                        list.printList()
                    except ValueError:
                        print("Please type in a number or press 'q' to quit")
            elif command == 'b':
                inValue = input("What is the value to run through the cache\n")
                try:
                    hashMap.put(int(inValue),list)
                    list.printList()
                except ValueError:
                    print("Please enter a number")
            elif command == 'p':
                list.printList()
            elif command == 'ph':
                print(hashMap)
            else:
                print('Invalid command. Try again')


if __name__=='__main__':
    UserInterface()
    
