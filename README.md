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
    * Enumerate all possible combinations. Power Set
    * Remove all the combinations that does not keep the constrains
    * Select the best combination possible from the remaining
    
    * **Done using search tree** _Left first, depth first enumeration_ [File.](Week%201/Decision-Trees.py)
        Optimized using memoization [here](Week%201/Dynamic-Programming.py)
        * Take an element from the still to be considered items. 
        * If there is room for that item, a node is made that represents that choice, that will be the left node. Always check the consequences of not taking the item, that will be the right node. 
        * This has to be recursively called to non-leaf nodes.
        
        Time is based on the number of nodes generated. 
        The number of levels is the same as the number of items to consider.
        Number of nodes at level x is 2^x.
        So with n items, the total number of nodes is the sum of 2^x, n times.
        O(2^(x+1))
        _Optimization_ could be done if the nodes that violates the constrains are excluded, 
        this doesn't change the complexity.

* **Greedy Algorithm** [File](Week%201/Optimization-Knapsack.py)
    ```
    while knapsack not full
       put "best" available item in knapsack
    ```
    * Can lead to local optimum instead of global optimum solution
    * Can't know how good is the approximation
    * It's easy to implement
    * Computationally efficient

**Dynamic Programming.**

*Memoization.*
Create a table to record what we've done. Trade time for space.
* Before computing fib(x), check if value of fib(x) is already stored in the table
    * If so, look it up.
    * If not, compute it and then add it to table
    
Works great when:
* **Optimal substructure.** A global solution can be found when solving local sub problems.
Case of Fibonacci.
* **Overlapping sub problems.** Finding the global solution involves solving the same problem
multiple times.

In search trees, dynamic programming works because in each node, the problem is _given 
the remaining weight, maximize value by choosing among the toConsider items_. Which means that
it should be checked if there are more nodes with the same remaining weight and the same toConsider items.
[Done here.](Week%201/Dynamic-Programming.py)