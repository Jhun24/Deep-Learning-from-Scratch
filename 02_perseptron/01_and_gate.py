import numpy as np

def AND(x1,x2):
    weight = np.array([2,3])
    data = np.array([x1,x2])

    bias = 4

    num = np.sum(weight*data)-bias

    if(num <= 0):
        return 0
    else:
        return 1

def OR(x1,x2):
    data = np.array([x1, x2])
    weight = np.array([2,2])

    bias = 1

    num = np.sum(weight * data) - bias

    if (num <= 0):
        return 0
    else:
        return 1



def NAND(x1,x2):
    data = np.array([x1, x2])
    weight = np.array([-1,-1])

    bias = -2

    num = np.sum(data*weight) - bias

    if (num <= 0):
        return 0
    else:
        return 1

def XOR(x1,x2):
    y1 = NAND(x1,x2)
    y2 = OR(x1,x2)

    num = AND(y1,y2)

    return num




if __name__ =="__main__":
    print("AND GATE : ")
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = AND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
    print("------------\n")

    print("NAND GATE : ")
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
    print("------------\n")

    print("OR GATE : ")
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = OR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
    print("------------\n")

    print("XOR GATE : ")
    for xs in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
    print("------------\n")