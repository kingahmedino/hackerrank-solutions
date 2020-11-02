def minimumBribes():
    q = [2, 1, 5, 3, 4]
    bribes = 0
    for i, val in reversed(list(enumerate(q))):
        if q[i] != i + 1:
            if i - 1 >= 0 and q[i-1] == i+1:
                temp = q[i-1]
                q[i-1] = q[i]
                q[i] = temp
                bribes += 1
            elif i - 2 >= 0 and q[i-2] == i+1:
                temp = q[i-2]
                q[i-2] = q[i-1]
                q[i-1] = q[i]
                q[i] = temp
                bribes += 2
            else:
                return "Too chaotic"

    return bribes


print(minimumBribes())
