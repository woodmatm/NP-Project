"""
    Bounded Max Knapsack Optimal Solution

    Author: Joe Drake                  
"""






def Sort(items):
    items.sort(key = lambda x: x[1])
    return items


def main():
    weight = int(input())
    r = int(input())
    n = int(input())
    items = [input().split() for _ in range(n)]
    for element in items:
        element[1]=int(element[1])
        element[2]=int(element[2])
    Sort(items)


if __name__ == "__main__":
    main()