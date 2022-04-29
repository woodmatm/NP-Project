"""
    Bounded Max Knapsack Optimal Solution

    Author: Joe Drake                  
"""
import time

def fillPack (W, items, n):
    
    if W == 0 or n == 0:
        return 0, []

    if (items[n-1][2] > W):
        return fillPack(W, items, n-1)
    
    else:
        useItem, tempList1 = fillPack(W-items[n-1][2], items, n-1)
        tempList1.append(items[n-1])
        useItem += items[n-1][1]
        skipItem, tempList2 = fillPack(W, items, n-1)
        if(useItem > skipItem):
            return useItem, tempList1
        else:
            return skipItem, tempList2

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

    fullList = [0]*total
    temp = 0
    for i in range(n):
        for j in range(items[i][3]):
            fullList[temp] = items[i]
            temp += 1

    t0 = time.time()
    items = fullList
    finalVal, finalList =fillPack(W, items, total)
    print(finalList)
    print(finalVal)
    print(time.time()-t0)


if __name__ == "__main__":
    main()