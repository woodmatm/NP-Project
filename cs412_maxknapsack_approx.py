import math


#This is a greedy algorithm. The greedy choice is sorting the items by value/weight ratio.
#The source of this algorithm is found here under Greedy approximation algorithm: https://en.wikipedia.org/wiki/Knapsack_problem


def main():
    #assume all items fit can individual fit into knapsack (ie no item exceeds knapsack weight)
    capacity = int(input())
    num_obj = int(input())
    list_of_objects = []
    for _ in range(0, num_obj):
        cur_list = [0] * 4
        line = input().split()
        cur_list[0] = line[0]
        cur_list[1] = float(line[1])
        cur_list[2] = float(line[2])
        cur_list[3] = int(line[3])
        list_of_objects.append(cur_list)
    x,y = approx(list_of_objects, capacity, num_obj)
    print(x)
    print(y)

def approx(list_of_objects, capacity, num_obj):
    list_of_objects.sort(key=sort_by_weight)    #sort the items by weight/value ratio
    list_of_objects.reverse()
    cap = capacity
    final_obj_list1 = []
    final_obj_list2 = []
    k_start = 0
    list1_value = 0
    list2_value = 0
    first_not_fit = False
    for i in range(0, num_obj): #for all items, starting with the items with the highest weight/value ratio
        for j in range(0, list_of_objects[i][3]): #begin to all the items of that type first (as many as is allowed)
            if cap - list_of_objects[i][2] >= 0: #if the bag's capacity is exceeded, stop
                final_obj_list1.append(list_of_objects[i])
                cap -= list_of_objects[i][2]
                list1_value += list_of_objects[i][1] #add the item to the first bag, reduce bag capacity, keep track of total value of bag
            else:
                if not first_not_fit: #if this is the first item that does not fit into the bag, keep track of its index
                    k_start = i
                    first_not_fit = True
    final_obj_list2.append(list_of_objects[k_start]) #add the first item that did not fit in to a new bag
    list2_value += list_of_objects[k_start][1]
    cap = capacity - list_of_objects[k_start][2]
    list_of_objects[k_start][3] -= 1 #take out the item placed into the bag so it does not get added again
    for i in range(0, num_obj):
        for j in range(0, list_of_objects[i][3]):
            if cap - list_of_objects[i][2] >= 0:
                final_obj_list2.append(list_of_objects[i])
                cap -= list_of_objects[i][2]
                list2_value += list_of_objects[i][1]
    if list1_value > list2_value: #return whichever set has a higher value
        return final_obj_list1, list1_value
    else:
        return final_obj_list2, list2_value


def sort_by_weight(e):
    return e[1] / e[2]


if __name__ == "__main__":
    main()