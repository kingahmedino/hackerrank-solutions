def rotLeft():
    a = [1, 2, 3, 4, 5]
    d = 2
    for i in range(d):
        x = a[0]
        a.pop(0)
        a.append(x)
    return list(map(str, a))


print(" ".join(rotLeft()))
