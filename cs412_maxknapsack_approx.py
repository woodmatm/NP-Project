import math


def main():
    #assume all items fit can individual fit into knapsack (ie no item exceeds knapsack weight)
    #greedily start packing items by weight ratio (S1)
    #make a second solution, with the first item that did not fit
    #The union of S1 and S2  provides an upper bound, one of the sets has m/2.
    #Return whichever set has a better value to btain a 1/2 approx
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
    list_of_objects.sort(key=sort_by_weight)
    list_of_objects.reverse()
    print(list_of_objects)
    cap = capacity
    final_val = 0
    final_obj_list1 = []
    final_obj_list2 = []
    k_start = 0
    list1_value = 0
    list2_value = 0
    first_not_fit = False
    for i in range(0, num_obj):
        for j in range(0, list_of_objects[i][3]):
            if cap - list_of_objects[i][2] >= 0:
                final_obj_list1.append(list_of_objects[i])
                cap -= list_of_objects[i][2]
                list1_value += list_of_objects[i][1]
            else:
                if not first_not_fit:
                    k_start = i
                    first_not_fit = True
    final_obj_list2.append(list_of_objects[k_start])
    num_obj -= 1
    list2_value += list_of_objects[k_start][1]
    cap = capacity - list_of_objects[k_start][2]
    list_of_objects.remove(list_of_objects[k_start])
    for i in range(0, num_obj):
        for j in range(0, list_of_objects[i][3]):
            if cap - list_of_objects[i][2] >= 0:
                final_obj_list2.append(list_of_objects[i])
                cap -= list_of_objects[i][2]
                list2_value += list_of_objects[i][1]
    if list1_value > list2_value:
        return final_obj_list1, list1_value
    else:
        return final_obj_list2, list2_value


def sort_by_weight(e):
    return e[1] / e[2]


if __name__ == "__main__":
    main()