# This project was made during my studies in UOA University and especially for the course Artificial Intelligence 1.

---

[Project 0: Unix/Python/Autograder Tutorial](https://inst.eecs.berkeley.edu/~cs188/sp19/project0.html#Q1)

> **Run command:** python ./autograder.py

> There are comments all over my code if there is something that i didn't covered here.

I created 5 more methods of the PriorityQueue class:

- exists(self,item) helped me find an item in the queue.
- priority(self,item,messages=1) helped me find a priority of an item.
- index(self,item,messages=1) helped me find an index of an item in the heap.
- getCount(self) helped me find the length of the queue.
- printq(self) helped me print the queue for testing the code.

> The messages = 1 in some methons is there to enable | disable the prints if there was an error.

---

```python
push(self, item, priority=0,messages=1)
# Doesn't allow duplicates items in the queue. But is is allowed to have duplicates of priorities.
```

```python
PQSort(list)
# Doesn't allow duplicates like push.
#Example:
list = [1,2,6,8,5,2,3]
# then the return will be
[1,2,3,5,6,8]
# The number 2 exists only 1 time. 
```
