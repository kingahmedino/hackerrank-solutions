
def sockMerchant():
    ar = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]
    count = 0
    dicto = {}
    for i in ar:
        if i in dicto.keys():
            dicto[i] += 1
        else:
            dicto[i] = 1
    singles = dicto.values()
    for i in singles:
        count += int(i / 2)

    return count


if __name__ == '__main__':
    result = sockMerchant()
    print(result)
