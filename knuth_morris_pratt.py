


def kmp_find_pi(a):
    n = len(a)
    pi = [0 for i in range(n)]

    j = 0
    pi[0] = 0
    i = 1
    while i != n:
        if a[i] == a[j]:
            pi[i] = j+ 1
            i += 1
            j += 1
        else:  # a[i] != a[j]
            if j == 0:
                pi[i] = 0
                i += 1
            else:  # j != 0
                j = pi[j - 1]
    return pi


def kmp_find_first(s, a):
    pi = kmp_find_pi(a)
    m = len(s)
    n = len(a)

    k = 0
    l = 0

    while True:
        if s[k] == a[l]:
            k += 1
            l += 1
            if l == n - 1:  # found
                res = k - l
                # print(res)
                break
        else:  # s[k] != a[l]
            if l == 0:
                k += 1
                if k == m - 1:  # string finished
                    res = "Match not found."
                    # print(res)
                    break
            else:  # l != 0
                l = pi[l - 1]

    return res


def kmp_find_all(s, a):
    res = []
    s = a + '#' + s
    pi = kmp_find_pi(s)

    m = len(s)
    n = len(a)

    k = n + 1

    while k != m:

        if pi[k] == n:
            res.append(k - 2*n)  # k-2n = k - (n+1) - (n-1)
        k += 1

    return res


def print_list_as_one_string(my_list):
    res_as_one_str = ""

    for num in my_list:
        res_as_one_str += str(num) + " "

    print(res_as_one_str)





# print(kmp_find_first("my string where i search for a special word", "ring"))
# print(kmp_find_first("my string where i search for a special word", "special"))
# print(kmp_find_first("my string where i search for a special word ring", "awesome"))


# print(kmp_find_all("my string where i search for a special word ring", "ring"))
s = input()
# a = input()

# print_list_as_one_string(kmp_find_all(s, a))

print_list_as_one_string(kmp_find_pi(s))




