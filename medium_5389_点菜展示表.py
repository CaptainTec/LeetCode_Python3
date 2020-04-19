class Solution:
    def displayTable(self, orders):
        food = set()
        data_dict = {}
        for one in orders:
            food.add(one[2])
            if one[1] in data_dict:
                if one[2] in data_dict[one[1]]:
                    data_dict[one[1]][one[2]] += 1
                else:
                    data_dict[one[1]][one[2]] = 1
            else:
                data_dict[one[1]] = {}
                data_dict[one[1]][one[2]] = 1
        
        food_sorted = sorted(food)
        head = ["Table"] + list(food_sorted)
        res = []
        for k, v in data_dict.items():
            mid = [int(k)] + [0] * len(food_sorted)  # k表示 桌号
            for key, value in v.items():
                mid[food_sorted.index(key)+1] = value
            res.append(mid)
        res = sorted(res)
        final = [head]
        for one in res:
            mid = [str(_) for _ in one]
            final.append(mid)
        return final
            
orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
res = Solution().displayTable(orders)
print(res)          
                
            