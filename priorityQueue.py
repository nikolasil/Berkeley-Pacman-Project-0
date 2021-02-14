import heapq  # importing "heapq" to implement PriorityQueue with heap

class PriorityQueue:
    def __init__(self):
        try:
            self.heap = []  # create the list
            heapq.heapify(self.heap)  # use heapify() to create the heap
            self.count = 0  # initialize count to 0
        except:
            print("Something went wrong in PriorityQueue.__init__(self)")
        return

    # checks if the item is in the queue
    def exists(self,item):
        try:
            x = [x[1] for x in self.heap]   # x takes from the tuples (priority,item) in the heap only the item
            if(item in x):  # checks if the item exists in the heap and if not add it else dont add it
                return True
            return False
        except:
            print("Something went wrong in PriorityQueue.exists(self,item)")
        return
    
    # return the priority of the item
    def priority(self,item,messages=1):
        try:
            if(self.exists(item)):
                x = [x[1] for x in self.heap]   # x takes from the tuples (priority,item) in the heap only the item
                y = [y[0] for y in self.heap]   # y takes from the tuples (priority,item) in the heap only the priority
                return(y[x.index(item)])
            else:
                if(messages):
                    print("priority: The item",item,"does not exists")
        except:
            print("Something went wrong in PriorityQueue.priority(self,item)")
        return

    # return the index of the item in the heap
    def index(self,item,messages=1):
        try:
            if(self.exists(item)):
                x = [x[1] for x in self.heap]   # x takes from the tuples (priority,item) in the heap only the item
                return(x.index(item))
            else:
                if(messages):
                    print("index: The item",item,"does not exists")
        except:
            print("Something went wrong in PriorityQueue.index(self,item)")
        return

    # return the count
    def getCount(self):
        return self.count

    # prints the heap
    def printq(self):
        try:
            print(self.heap)
        except:
            print("Something went wrong in PriorityQueue.print(self)")
        return

    # push item in the queue
    # does not allow duplicate items
    def push(self, item, priority=0,messages=1):
        try:
            if(self.exists(item) == False):  # checks if the item exists in the heap and if not add it else dont add it
                heapq.heappush(self.heap,(priority,item))  # push the tuple (priority,item) to the heap
                self.count += 1  # increase count
            else:
                if(messages):
                    print("push: The item",item,"already exists in the queue.")
        except:
            print("Something went wrong in PriorityQueue.push(self, item, priority)")
        return

    # pop the item with minimum priority and return it
    def pop(self,messages=1):
        try:
            if(self.isEmpty() == False):
                x = heapq.heappop(self.heap)  # pop the item with the minimum priority and save it to x to return it at the end of the function
                self.count -= 1  # decrease the count
                return x[1]  # return the popped item without the priority
            else:
                if(messages):
                    print("pop: The queue is empty")
        except:
            print("Something went wrong in PriorityQueue.pop(self)")
        return

    # returns true if the queue is empty and false otherwise
    def isEmpty(self):
        try:
            if (self.count != 0): 
                return False
            return True
        except:
            print("Something went wrong in PriorityQueue.isEmpty(self)")
        return

    # update the item with the new priority if its smaller. If the item dont exist its beeing pushed.
    def update(self, item, priority,messages=1):
        try:
            if(self.exists(item) == False):  # checks if the item is in the queue
                self.push(item, priority,messages)  # if not add it and return
            else:
                temp = self.priority(item,messages)  # temp has the priority of the item in the heap
                if(temp > priority): # if the priority of the item in the heap is bigger than the priority we try to update it with
                    self.heap[self.index(item,messages)] = (priority,item)   # go to the specific index of the item and change it 
                    heapq.heapify(self.heap)  # use heapify() to recreate the heap afte the change
        except:
            print("Something went wrong in PriorityQueue.update(self, item, priority)")
        return

# function to sort a list using a priority queue
def PQSort(list):
    queue = PriorityQueue() # create a queue
    for i in list:
        queue.push(i,i,0)   # a loop to a push all the intigers in the priority queue
    x = []  # the list that will be returned later
    for i in range(queue.getCount()):   # the pop() method returns the smaller interger and remove it from the queue.
        x.append(queue.pop(0))          # So if we pop() again and again we will have the list sorted
    return x