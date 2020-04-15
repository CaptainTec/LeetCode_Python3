def calculate_k_b(start, end):
    if start[0] == end[0]:  # x = scalar 此时斜率无穷大
        print ("", start[0])
    elif start[1] == end[1]:  # y = scalar 此时斜率为0
        print (start[1], "")
    else:
        k = (start[1] - end[1]) / (start[0] - end[0])
        b = start[1] - k*start[0]
        print (k, b)

calculate_k_b([1, 1], [0, -1])
