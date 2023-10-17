"""
 * 美国新冠趋势折线图
 * Author: xiaojl
 * Date:2023-10-08 23:33
"""
import json

from pyecharts.charts import Line
import re

us_data = None

with open("/Users/xiao/Developer/Python/资料/第1-12章资料/资料/可视化案例数据/折线图数据/美国.txt", "r",
          encoding="UTF-8") as file:
    us_data = file.read()

us_data = re.sub(r"jsonp.*\(", '', us_data)
us_data = us_data[:-2]
# print(us_data)
us_data = json.loads(us_data)
# print(us_data)

trend = us_data['data'][0]['trend']

dates = trend['updateDate']
datas = trend['list'][0]['data']

show_date = []
show_data = []

index = 0
while index < len(dates):
    date = dates[index]
    if float(date) > 3.25:
        break
    show_date.append(date)
    show_data.append(datas[index])
    index += 1

line = Line()
line.add_xaxis(show_date)
line.add_yaxis("人数", show_data)

line.render()

