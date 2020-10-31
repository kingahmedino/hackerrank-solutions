import sys


def hourglassSum():
    arr = [[0, -4, -6, 0, -7, -6],
           [-1, -2, -6, -8, -3, -1],
           [-8, -4, -2, -8, -8, -6],
           [-3, -1, -2, -5, -7, -4],
           [-3, -5, -3, -6, -6, -6],
           [-3, -6, 0, -8, -6, -7]]
    maximum = - sys.maxsize - 1
    array = []
    for a in range(4):
        for b in range(4):
            for i in range(3):
                for j in range(3):
                    array.append(arr[i+a][j+b])
            del array[3]
            del array[4]
            maximum = max(maximum, sum(array))
            array = []
    return maximum


print(hourglassSum())
