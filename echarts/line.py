"""
 * echarts 折线图
 * Author: xiaojl
 * Date:2023-10-08 22:36
"""

from pyecharts.charts import Line

line = Line()

line.add_xaxis(['周一', '周二', '周三'])                      #
line.add_yaxis("时间", [100, 200, 300])    #

line.render()
