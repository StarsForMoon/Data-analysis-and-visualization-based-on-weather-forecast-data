#dataprocess.py程序是数据处理程序
#负责对来自对数据集进行数据分析和处理，以便于提供给chart.py程序进行可视化

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import chart

# 温度变化图
def temperature(data,city):
    tems = list(data['温度'].astype(int))#导入温度一列
    hours = list(data['小时'].astype(int))#导入时间一列
    temave = sum(tems) / len(tems)  # 求平均温度
    temmin = min(tems)#求最低温度
    tem_minhour = hours[tems.index(temmin)]  # 求最低温度及其时刻
    temmax = max(tems)#求最高温度
    tem_maxhour = hours[tems.index(temmax)]  # 求最低温度及其时刻
    #传递给chart.py中对应的函数进行可视化
    chart.temdiagram(tems, hours, temave, temmin, tem_minhour, temmax, tem_maxhour,city)

# 相对湿度变化图
def humidity(data,city):
    hours = list(data['小时'].astype(int))#导入时间一列
    hums = list(data['相对湿度'].astype(float))#导入相对湿度一列
    humave = sum(hums) / len(hums)  # 求平均相对湿度
    hummax = max(hums)#求最大湿度
    hum_maxhour = hours[hums.index(hummax)]  # 求最高相对湿度及其时刻
    hummin = min(hums)#求最小湿度
    hum_minhour = hours[hums.index(hummin)]  # 求最低相对湿度及其时刻
    #传递给chart.py中对应的函数进行可视化
    chart.humdiagram(hours, hums, humave, hummax, hum_maxhour, hummin, hum_minhour,city)

# 降雨量曲线图
def rainfall(data,city):
    hours = list(data['小时'].astype(int))#导入时间一列
    rainfall = list(data['降水量'].astype(float))#导入降雨量一列
    rainfallavg = sum(rainfall) / len(rainfall)#求平均降雨量
    rainfallmax = max(rainfall)#求最大降雨量
    hour_rainfallmax = hours[rainfall.index(rainfallmax)]#求最大降雨量对应时间
    rainfallmin = min(rainfall)#求最小降雨量
    hour_rainfallmin = hours[rainfall.index(rainfallmin)]#求最小降雨量对应时间
    #传递给chart.py中对应的函数进行可视化
    chart.rainfalldiagram(hours, rainfall, rainfallavg, rainfallmax, hour_rainfallmax, rainfallmin, hour_rainfallmin,city)

# 风向雷达图
def wind(data,city):
    wind = list(data['风力方向'])#导入风力方向一列
    windspeed = list(data['风级'].astype(float))#导入风级一列
    #将定性数据风向转换为定量数据风向
    for i in range(0, 24):
        if wind[i] == "东风":
            wind[i] = 0
        elif wind[i] == "东北风":
            wind[i] = 45
        elif wind[i] == "北风":
            wind[i] = 90
        elif wind[i] == "西北风":
            wind[i] = 135
        elif wind[i] == "西风":
            wind[i] = 180
        elif wind[i] == "西南风":
            wind[i] = 225
        elif wind[i] == "南风":
            wind[i] = 270
        elif wind[i] == "东南风":
            wind[i] = 315
    degs = np.arange(0, 316, 45)#将0-360度分为八块（因为有八个风向）
    
    #下面的循环处理是用于求每个方向的平均风速
    temp = []     
    for deg in degs:
        speed = []  # 获取 wind_deg 在指定方向的风速平均值数据
        for i in range(0, 24):
            if wind[i] == deg:
                speed.append(windspeed[i])
        if len(speed) == 0:
            temp.append(0)
        else:
            temp.append(sum(speed) / len(speed))
    
    #传递给chart.py中对应的函数进行可视化
    chart.windradar(temp,city)

# 皮尔逊相关系数函数
def coefficient(var1,var2):
    aavg = sum(var1)/len(var1)#变量1的平均值
    bavg = sum(var2)/len(var2)#变量2的平均值
    covab = sum([(x - aavg)*(y - bavg) for x,y in zip(var1,var2)])#变量1和变量2的协方差
    asd= math.sqrt(sum([(i - aavg)**2 for i in var1]))#变量1的标准差
    bsd= math.sqrt(sum([(j - bavg)**2 for j in var2]))#变量2的标准差
    raletive_coe = covab/(asd*bsd) #变量1和2的皮尔逊相关系数
    return round(raletive_coe,4)#保留四位小数


    
    
    
    