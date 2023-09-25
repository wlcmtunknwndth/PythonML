import math


def entropy(value_arr):
    # sum += value_arr[x] for x in range(len(value_arr))
    tmp = []
    for i in range(len(value_arr)):
        tmp.append(value_arr[i] * math.log2(value_arr[i]))
    zeta = sum(tmp)
    return -zeta


def cross_entropy(first_arr, second_arr):
    tmp = []
    for i in range(len(first_arr)):
        tmp.append(first_arr[i] * math.log2(first_arr[i]/second_arr[i]))
    zeta = sum(tmp)

    return -zeta


def str_arr_to_float_arr():
    ls = input().split()
    if len(ls) == 0:
        return
    for i in range(len(ls)):
        ls[i] = float(ls[i])
    return ls

# 0.6789 0.3434 0.8343 0.5345 0.1295 0.9731
# 0.4343 0.3545 0.5678 0.9032 0.8921 0.3491


if __name__ == '__main__':
    # arr_1 = [0.6789, 0.3434, 0.8343, 0.5345, 0.1295, 0.9731]
    # arr_2 = [0.4343, 0.3545, 0.5678, 0.9032, 0.8921, 0.3491]
    arr_1 = str_arr_to_float_arr()
    # print(arr_1)
    arr_2 = str_arr_to_float_arr()
    # print(arr_2)
    en_x = entropy(arr_1)
    en_xy = cross_entropy(arr_1, arr_2)
    # print('En(x): ', en_x)
    # print('En(x,y): ', en_xy)
    print(round(en_x - en_xy, 2))
