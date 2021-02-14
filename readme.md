## This was an exercise that i did on a class Artificial Intelligence in University 
---
There are comments in my code.

I created 5 more methods of the PriorityQueue class:

- exists(self,item) helped me find an item in the queue.
- priority(self,item,messages=1) helped me find a priority of an item.
- index(self,item,messages=1) helped me find an index of an item in the heap.
- getCount(self) helped me find the length of the queue.
- printq(self) helped me print the queue for testing the code.

The messages=1 in some methons is there to enable\disable the prints if there was an error.

push(self, item, priority=0,messages=1):
Doesn't allow duplicates items in the queue. But is is allowed to have duplicates of priorities.

PQSort(list) doen't allow duplicates like push.

Example:
list = [1,2,6,8,5,2,3]
then return [1,2,3,5,6,8]. The 2 exists only 1 time. 
