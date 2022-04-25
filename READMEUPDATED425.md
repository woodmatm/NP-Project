# NP-Project
Group members: Joe Drake, Trevor Woodman, Jacob Hataway, Patrick Glebus

Problem Definition (Max Knapsack):
Given a bag, or a knapsack, that can hold some maximum positive weight w, and given a list of items, each with a unique name, a weight, a value, and a maximum amount of copies of the item (c), determine the maximum amount of value the bag can hold without exceeding w, and no item is present in a quantity greater than its c amount in the bag.
 
Workload Assignment Between Members:
Trevor Woodman: Approximation Code/Evaluation of Other Projects

Joe Drake: Exact Code/Problem Presentation

Patrick Glebus: Approximation Code/Presentation

Jacob Hataway: Exact Code/Problem Presentation

Form of Input:
Input will begin with a single line containing a nonnegative integer weight w, representing the maximum capacity of the knapsack. This is followed by a single line that contains a nonnegative integer n followed by exactly n lines each of which contains four items (String, real, real, int).  The first value is the item's name, the second is the dollar value of the item, the third is the item's weight, and the fourth is the bound on how many of that item you can put into the knapsack.
Ex:

11

3

ring 100 5 2

gold 50 10 5

silver 50 5 1


Form of Output:
The first lines are the list of items in the knapsack with the name, value and weight. The final line is the total value of items in the knapsack, formatted to two decimal places.
Ex:

ring 100 50

silver 50 25

gold 5 1 

155.00

