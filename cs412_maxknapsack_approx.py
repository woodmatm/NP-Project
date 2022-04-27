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
    list_of_objects.sort(key=lambda x: (int(x[1]) / int(x[2])))
    print(list_of_objects)
    cap = capacity
    final_val = 0
    final_obj_list1 = []
    final_obj_list2 = []
    k_start = 0
    for i in range(0, num_obj):
        for j in range(0, list_of_objects[i][3]):
            if cap - list_of_objects[i][3] > 0:
                final_obj_list1.append(list_of_objects[i])
                cap -= list_of_objects[i][2]
            else:
                k_start = i
                break
    final_obj_list2.append(list_of_objects[k_start])
    cap = capacity - list_of_objects[k_start][2]
    for i in range(0, num_obj):
        for j in range(0, list_of_objects[i][3]):
            if cap - list_of_objects[i][3] > 0:
                final_obj_list1.append(list_of_objects[i])
                cap -= list_of_objects[i][2]
            else:
                break
    print(final_obj_list1)
    print(final_obj_list2)




if __name__ == "__main__":
    main()