def int_input():
    ls = input().split()
    if len(ls) == 0:
        return
    for i in range(len(ls)):
        ls[i] = int(ls[i])
    return ls


class Graph:

    def __init__(self, v):
        self.__matrix = [[0]*v for i in range(v)]
        self.__v = v

    def fulfill(self):
        for i in range(self.__v):
            q = int_input()
            for j in range(self.__v):
                self.__matrix[i] = q

    def print(self):
        # adj = [i for i in range(self.__v)]
        # print(' ', adj)
        for i in range(self.__v):
            print(self.__matrix[i])

    def is_tree(self):
        visited = [0]
        for i in range(self.__v):
            visited.append(i)
            for j in range(self.__v):
                if self.__matrix[i][j] == 1 and j in visited and (i-1 not in visited):
                    return 'NO'
                else:
                    continue
        return 'YES'


if __name__ == '__main__':
    gr = Graph(int(input()))
    gr.fulfill()
    print(gr.is_tree())
