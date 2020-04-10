"""
easy

"""


def isHappy(n):
    # data_set = set()
    data_dict = {}
    while True:
        data = []
        while n:
            data.append(n % 10)
            n = n // 10
        n = 0
        for one in data:
            n += one ** 2
        if n == 1:
            return True
        if n in data_dict:
            return False
        else:
            # data_set.add(n)
            data_dict[n] = 1


print(isHappy(9))

