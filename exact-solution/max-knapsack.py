"""
    Bounded Max Knapsack Optimal Solution

    Author: Joe Drake                  
"""


def fillPack (W, val, weight, num, n):
    
    if W == 0 or n == 0:
        return 0

    if (weight[n-1] > W):
        return fillPack(W, val, weight, num, n-1)
    
    else:
        if(num[n-1] == 1):
            return max(val[n-1] + fillPack(W-weight[n-1], val, weight, num, n-1),
                fillPack(W, val, weight, num, n-1))
        else:
            num[n-1] = num[n-1]-1
            return max(val[n-1] + fillPack(W-weight[n-1], val, weight, num, n),
                fillPack(W, val, weight, num, n))



def Sort(items):
    items.sort(key = lambda x: x[1])
    return items


def main():
    W = int(input())
    n = int(input())
    items = [input().split() for _ in range(n)]
    val = [0]*n
    weight = [0]*n
    num = [0]*n
    for element in items:
        element[1]=int(element[1])
        element[2]=int(element[2])
        element[3]=int(element[3])
    for i in range(n):
        val[i] = items[i][1]
        weight[i] = items[i][2]
        num[i] = items[i][3]
    print(fillPack(W, val, weight, num, n))


if __name__ == "__main__":
    main()