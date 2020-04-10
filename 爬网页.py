import os
import requests  # 导入网络请求库
import random  # 导入随机数库

# 这才是真实的url
url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false'

# 请求头中的这些参数一般被用来做反爬的判断依据，每个人的User-Agent是不一样的
the_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'Host': 'www.lagou.com',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': None,
    'X-Requested-With': 'XMLHttpRequest'
}

# # 循环爬取30页的数据
# for pages in range(1, 31):
#     # post请求中要带上一些参数
the_data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
    }

# 向服务器请求数据
result = requests.post(url, headers=the_headers, data=the_data)
# result = requests.post(url, headers=the_headers)
print(result)

jsonResult = result.json()

print(jsonResult)

# # 我们想要的数据内容就从下面的关键字中一个层级一个层级的向下找
# json_result = jsonResult['content']['positionResult']['result']
#
# print(json_result)
#
# # 为了模拟真实的浏览器操作，需要不定时休眠
# random.randint(20, 36)
#
# print('所有页面爬取成功')
