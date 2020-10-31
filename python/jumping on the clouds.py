def jumping():
    c = [0, 0, 1, 0, 0, 1, 0]
    jumps = 0
    jumpsStr = "".join(list(map(str, c)))
    jumpsArr = jumpsStr.split("1")
    for string in jumpsArr:
        jumps += int(len(string) / 2)
    jumps += len(jumpsArr) - 1
    return jumps


print(jumping())
