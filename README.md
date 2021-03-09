# This project was made during my studies in UOA University and especially for the course Artificial Intelligence 1.

---

[Project 0: Unix/Python/Autograder Tutorial](https://inst.eecs.berkeley.edu/~cs188/sp19/project0.html#Q1)

> **Run command:** python ./autograder.py

## Question 2

```python
for i in orderList: # loop in the order list and for each thing calculate the cost and add it to the total cost
    if (i[0] in fruitPrices): # checks if the thing in the order is in the list fruitPrices else return error
        totalCost += i[1] * fruitPrices[i[0]] # calculate the cost of each thing and add it to totalCost
    else:
        print("Error")
        return None
return totalCost
```

---

## Question 3

```python
cost = fruitShops[0].getPriceOfOrder(orderList) # Initialize the cost variable with the first shop cost
cheapestShop = fruitShops[0] # Initialize the variable cheapestShop with the first shop so if the first shop is the cheapest i will return it

iterShops = iter(fruitShops)
next(iterShops) # skip the the first shop because we already checked the price of the order for the first shop in the initialization of the variables

for shop in iterShops:  # loop for the each other shop and in every loop we check if the previus is cheaper or not and update the variables if true
    temp = shop.getPriceOfOrder(orderList)
    if(cost > temp):
        cost = temp
        cheapestShop = shop
return cheapestShop # in the end we will have the cheapest shop so we return it
```
