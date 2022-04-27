"""
    Bounded Max Knapsack Optimal Solution

    Author: Joe Drake                  
"""
import time

def fillPack (W, val, weight, num, n):
    
    if W == 0 or n == 0:
        return 0

    if (weight[n-1] > W):
        return fillPack(W, val, weight, num, n-1)
    
    else:
        return max(val[n-1] + fillPack(W-weight[n-1], val, weight, num, n-1),
            fillPack(W, val, weight, num, n-1))
        



def Sort(items):
    items.sort(key = lambda x: x[1])
    return items


def main():
    W = int(input())
    n = int(input())
    items = [input().split() for _ in range(n)]
    
    total = 0
    for element in items:
        element[1]=int(element[1])
        element[2]=int(element[2])
        element[3]=int(element[3])
        total = total + element[3]
    #Sort(items)
    val = [0]*total
    weight = [0]*total
    num = [0]*total

    temp = 0
    for i in range(n):
        for j in range(items[i][3]):
            val[temp] = items[i][1]
            weight[temp] = items[i][2]
            num[temp] = items[i][3]
            temp += 1
    t0 = time.time()
    print(fillPack(W, val, weight, num, total))
    print(time.time()-t0)


if __name__ == "__main__":
    main()