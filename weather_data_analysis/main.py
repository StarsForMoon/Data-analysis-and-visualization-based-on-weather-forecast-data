from PyQt5.QtWidgets import QMainWindow, QApplication
from img.MainWindow import Ui_MainWindow  # 导入主窗体文件中的ui类
import sys                   # 导入系统模块
import dataprocess as dataprocess        # 导入自定义天气数据分析模块
import dataprocess                 # 导入自定义绘图模块
import pandas as pd
import matplotlib.pyplot as plt
import os
from os import path

import requests
from bs4 import BeautifulSoup
import csv
import json

# 主窗体初始化类
#解决基本显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  # 解决中文显示问题
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题




def city_num():
    localpath=path.dirname(__file__)
    path1=os.path.join(localpath,'dataset/中国天气城市编号.csv')
    city = input("请输入您想要查询天气情况的城市：")
    file = pd.read_csv(path1, encoding="utf-8")  # 读取本地文件
    index = file[file['城市'] == '{}'.format(city)].index.tolist()[0]  # 根据城市查找行标签
    num = file.loc[index, '编号']  # 根据行标签和列表签锁定值
    return num,city

def getHTMLtext(url):     
    """请求获得网页内容"""
    try:         
        r = requests.get(url, timeout = 30)         
        r.raise_for_status()         
        r.encoding = r.apparent_encoding         
        print("成功访问")         
        return r.text     
    except:         
        print("访问错误")         
        return" " 

def get_content(html):
    final = []  							 # 初始化一个列表保存数据
    bs = BeautifulSoup(html, "html.parser")  # 创建BeautifulSoup对象
    body = bs.body
    data = body.find('div', {'id': '7d'})    # 找到div标签且id = 7d
    # 下面爬取当天的数据
    data2 = body.find_all('div',{'class':'left-div'})
    text = data2[2].find('script').string	 
    text = text[text.index('=')+1 :-2]		 # 移除改var data=将其变为json数据
    jd = json.loads(text)
    dayone = jd['od']['od2']				 # 找到当天的数据
    final_day = []						     # 存放当天的数据
    count = 0
    for i in dayone:
        temp = []
        if count <=23:
            temp.append(i['od21'])				 # 添加时间
            temp.append(i['od22'])				 # 添加当前时刻温度
            temp.append(i['od24'])				 # 添加当前时刻风力方向
            temp.append(i['od25'])				 # 添加当前时刻风级
            temp.append(i['od26'])				 # 添加当前时刻降水量
            temp.append(i['od27'])				 # 添加当前时刻相对湿度
            temp.append(i['od28'])				 # 添加当前时刻控制质量
            #print(temp)
            final_day.append(temp)
        count = count +1
    # 下面爬取7天的数据	
    ul = data.find('ul')					 # 找到所有的ul标签
    li = ul.find_all('li')					 # 找到左右的li标签
    i = 0  			# 控制爬取的天数
    for day in li:  						 	# 遍历找到的每一个li
        if i < 7 and i > 0:
            temp = []  						 	# 临时存放每天的数据
            date = day.find('h1').string  	 	# 得到日期
            date = date[0:date.index('日')]  	# 取出日期号
            temp.append(date)				        
            inf = day.find_all('p')  		 	# 找出li下面的p标签,提取第一个p标签的值，即天气
            temp.append(inf[0].string)

            tem_low = inf[1].find('i').string  	# 找到最低气温

            if inf[1].find('span') is None:  	# 天气预报可能没有最高气温
                tem_high = None
            else:
                tem_high = inf[1].find('span').string  # 找到最高气温
            temp.append(tem_low[:-1])
            if tem_high[-1] == '℃':
                temp.append(tem_high[:-1])
            else:
                temp.append(tem_high)

            wind = inf[2].find_all('span')		# 找到风向
            for j in wind:
                temp.append(j['title'])

            wind_scale = inf[2].find('i').string # 找到风级
            index1 = wind_scale.index('级')
            temp.append(int(wind_scale[index1-1:index1]))
            final.append(temp)
        i = i + 1
    return final_day,final


def write_to_csv(file_name, data, day=14):
    with open(file_name, 'a', errors='ignore', newline='') as f:
        if day == 14:
            header = ['日期','天气','最低气温','最高气温','风向1','风向2','风级']
        else:
            header = ['小时','温度','风力方向','风级','降水量','相对湿度','空气质量']
        f_csv = csv.writer(f)
        f_csv.writerow(header)
        f_csv.writerows(data)

class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

    def show_temperature(self):
        dataprocess.temperature(data,city)

    def show_humidity(self):
      dataprocess.humidity(data,city) #湿度变化曲线

    def show_rainfall(self):
        dataprocess.rainfall(data,city)#降雨量曲线图

    def show_windradar(self):
        dataprocess.wind(data,city)#风级风向雷达图

if __name__ == '__main__':
    print("Weather test")
    num,city = city_num()
    url1 = 'http://www.weather.com.cn/weather/{}.shtml'.format(num)    # 7天天气中国天气网	
    html1 = getHTMLtext(url1)
    data1,_= get_content(html1)		# 获得当天的数据
    localpath=path.dirname(__file__)
    writepath=os.path.join(localpath,'dataset/weathertest.csv')
    write_to_csv(writepath,data1,1)
    #原始数据集导入
    srcdata = pd.read_csv(writepath, encoding='gb2312')
    data=srcdata[0:24]
    app = QApplication(sys.argv)
    # 主窗体对象
    main = Main()
    # 显示温度变化曲线图，按钮事件
    main.btn_1.triggered.connect(main.show_temperature)
    # 显示湿度变化曲线图，按钮事件
    main.btn_2.triggered.connect(main.show_humidity)
    # 显示降雨量变化曲线，按钮事件
    main.btn_3.triggered.connect(main.show_rainfall)
    # 显示风向雷达图，按钮事件
    main.btn_4.triggered.connect(main.show_windradar)
    # 显示主窗体
    main.show()
    sys.exit(app.exec_())  # 当窗口创建完成，需要结束主循环过程

