# 求众数


def main_2018_1():
    _ = int(input())
    data_list = map(int, input().split())
    data_dict = {}
    for one in data_list:
        if one in data_dict:  # {key: value}
            data_dict[one] += 1
        else:
            data_dict[one] = 1
    # print(data_dict)
    res, cnt = 0, 0
    for k, v in data_dict.items():
        if v > cnt:
            cnt = v
            res = k
        elif v == cnt:
            res = min(res, k)
    print(res)


# main_2018_1()


# 解方程

def main_2018_2():
    s = input()
    a, b = s.split("=")

    def handle(str_mid):
        res_str = ""
        if str_mid[0] == "-":
            str_mid = "0+" + str_mid
        for i in range(len(str_mid)):
            if str_mid[i] == "-" and str_mid[i-1] != "+":
                res_str += "+-"
            else:
                res_str += str_mid[i]
        mid_list = res_str.split("+")
        # print(mid_list)
        x_in, not_in = [], []
        for one in mid_list:
            if 'x' in one:
                if one[:-1] == "-":  # -x
                    x_in.append(-1)
                elif one == "x":  # x
                    x_in.append(1)
                else:
                    x_in.append(int(one[:-1]))
            else:
                not_in.append(int(one))
        return sum(not_in), sum(x_in)
    left, right = [0, 0], [0, 0]
    left[0], left[1] = handle(a)
    right[0], right[1] = handle(b)
    if left[1] == right[1]:
        if right[0] == left[0]:
            print("infinite solutions")
        else:  # x-1=x-2
            print("no solution")
    else:
        print("x=" + str(int((right[0] - left[0])/(left[1] - right[1]))))


# main_2018_2()


# 骨牌 -- 简单dp
# 状态转移方程 f(n) = f(n-1) + f(n-2)
# [0, 1, 2, 3, 5, 8, 13, 21, 34 ... ]

def main_2018_3():
    n = int(input())
    # n = 1->1, 2->2
    if n <= 2:
        return n

    a, b = 1, 2
    while n > 2:
        a, b = b, a+b
        n -= 1
    print(b % 999983)


# main_2018_3()


a = [1, 1, 2, 3, 3]
print(a.pop(0))
print(a.pop(-1))
print(a.pop())




