# 求众数


def main_2018_1():
    _ = int(input())
    data = list(map(int, input().split()))
    cnt_dict = {}
    for one in data:
        if one in cnt_dict:
            cnt_dict[one] += 1
        else:
            cnt_dict[one] = 1
    key, value = data[0], cnt_dict[data[0]]
    for k, v in cnt_dict.items():
        if v > value:
            key = k
            value = v
    print(key)


# main_2018_1()


# 解方程

def main_2018_2():
    ss = input()
    a, b = ss.split("=")
    left = [0, 0]
    right = [0, 0]

    def handle(mid_str):
        if mid_str[0] == '-':
            mid_str = "0+" + mid_str[:]
        res_str = ""
        for i in range(len(mid_str)):
            if mid_str[i] == '-' and mid_str[i-1] != '+':
                res_str += "+-"
            else:
                res_str += mid_str[i]
        # print(res_str)
        mid_list = res_str.split('+')
        x_in, not_in = [], []
        for ele in mid_list:
            if 'x' in ele:
                if ele[:-1] == '-':
                    x_in.append(-1)
                elif ele == 'x':
                    x_in.append(1)
                else:
                    x_in.append(int(ele[:-1]))
            else:
                not_in.append(int(ele))
        return sum(not_in), sum(x_in)

    left[0], left[1] = handle(a)
    right[0], right[1] = handle(b)
    if left[1] - right[1] == 0:
        if right[0] - left[0] == 0:
            print('infinite solutions')
        else:
            print('no solution')
    else:
        if right[0] - left[0] == 0:
            print('x=0')
        else:
            print('x='+str(int((right[0] - left[0])/(left[1] - right[1]))))


# main_2018_2()


# 骨牌 - 简单dp

def main_2018_3():
    n = int(input())
    if n < 2:
        print(n)

    a, b = 1, 2
    while n > 2:
        a, b = b, a+b
        n -= 1
    print(b % 999983)


# main_2018_3()


# 2019



















