# def count_substring(string, sub_string):
#     count1 = 0
#     if string.find(sub_string) != -1:
#         count1 += 1
#         index = string.find(sub_string)
#         count1 += count_substring(string[index + 1:], sub_string)
#     return count1
#
#
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
#
#     count = count_substring(string, sub_string)
#     print(count)


def sockMerchant(n, ar):
    ar = ar.sorted()
    count = 0
    if n > 1:
        if ar[0] == ar[1]:
            count += 1
            del ar[0]
            del ar[1]
            count += sockMerchant(len(ar), ar)
    return count
