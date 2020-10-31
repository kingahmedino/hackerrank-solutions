def repeatedString():
    s = "abcac"
    n = 10
    no_of_As_in_s = s.count('a')
    no_of_As = int(n / len(s)) * no_of_As_in_s
    for i in range(n % len(s)):
        if 'a' == s[i]:
            no_of_As += 1
    return no_of_As


print(repeatedString())
