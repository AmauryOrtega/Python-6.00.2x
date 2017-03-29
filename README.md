# Python-6.00.2x
Introduction to Computational Thinking and Data Science

## Week 1
### Optimization model
- Objective function that has to be maximized or minimized
- Set of constrains

**Knapsack problem.** Take the maximum of items in your backpack without surpassing the constrains
* 0/1 problem - inherently O(2^n)
    * Take it or not
* Continuous or fractional problem
    * Can take part of an item

**Solving**
* **Brute Force O(2^n)**

    Enumerate all possible combinations. Power Set
    
    Remove all the combinations that doesn't keep the constrains
    
    Select the best combination possible from the remaining
    
* **Greedy Algorithm**
    ```
    while knapsack not full
       put "best" available item in knapsack
    ```
    Can lead to local optimum instead of global optimum solution
    
    Can't know how good is the approximation
    
    It's easy to implement

    Computationally efficient
