
import matplotlib  # 导入图表模块
import matplotlib.pyplot as plt # 导入绘图模块
# 避免中文乱码
matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
#chart.py程序是调用matplotlib中的库函数进行可视化
#数据的接收自dataprocess.py程序，然后进行可视化

import matplotlib.pyplot as plt
import math
import numpy as np
import os
from os import path

#设置处理后图片的保存路径
path=path.dirname(__file__)#当前文件的目录
#parent_path=os.path.dirname(path)#当前文件目录的父目录
savepath=os.path.join(path,'result')#连接路径，保存在Result文件夹中

# 温度变化图
def temdiagram(tems,hours,temave,temmin,tem_minhour,temmax,tem_maxhour,city):
    x = []#以时间为x坐标
    y = []#以温度为y坐标
    plt.figure(1,figsize=(16,10))#定义图片大小和序号
    
    #制作数据变化的动画效果
    for i in range(0, 24):
        x.append(i)
        y.append(tems[hours.index(i)])  # 每迭代一次，将i放入y中画出来
        plt.clf()  # 清除键
        plt.plot(x, y, color='#7FFFD4', label='温度')
        plt.legend()
        plt.pause(0.15)#暂停0.15s便可以得到动画效果
    
    #定义图片标题，x轴和y轴坐标名称
    plt.title(city+'一天温度变化曲线图')
    plt.xlabel('时间/h')
    plt.ylabel('摄氏度/℃')
    plt.scatter(x, y, color='#7FFFD4')  # 点出每个时刻的温度点
   
    # 画出平均温度虚线
    plt.plot([0, 24], [temave, temave], color='#5595F9', linestyle='--', label='平均温度')
    plt.text(tem_maxhour + 0.15, temmax - 0.25, str(temmax) + '℃', ha='center', va='bottom', fontsize=10.5,
             color='#9370DB')  # 标出最高温度
    plt.text(tem_minhour + 0.15, temmin - 0.20, str(temmin) + '℃', ha='center', va='bottom', fontsize=10.5,
             color='#9370DB')  # 标出最低温度
    
    plt.xticks(x)
    plt.savefig(savepath+'\温度变化图.png', dpi=800)#保存图片到指定文件夹
    plt.show()
    #plt.close()


# 相对湿度变化图
def humdiagram(hours,hums,humave,hummax,hum_maxhour,hummin,hum_minhour,city):
    x = []#时间为x坐标
    y = []#湿度为y坐标
    plt.figure(2, figsize=(16, 10))#定义图片大小和序号
    
    #制作数据变化的动画效果
    for i in range(0, 24):
        x.append(i)
        y.append(hums[hours.index(i)])  # 每迭代一次，将i放入y中画出来
        plt.cla()  # 清除键
        plt.plot(x, y, color='#7FFFD4', label='相对湿度')  # 相对湿度曲线
        plt.legend()
        plt.pause(0.15)#暂停0.15s便可以得到动画效果
        
    #定义图片标题，x轴和y轴坐标名称
    plt.title(city+'一天相对湿度变化曲线图')
    plt.xlabel('时间/h')
    plt.ylabel('百分比/%')
    plt.scatter(x, y, color='#7FFFD4')  # 点出每个时刻的相对湿度
   
    # 画出平均相对湿度虚线
    plt.plot([0, 24], [humave, humave], color='#5595F9', linestyle='--', label='平均相对湿度')
    plt.text(hum_maxhour + 0.15, hummax + 0.15, str(hummax) + '%', ha='center', va='bottom', fontsize=10.5,
             color='#9370DB')  # 标出最高相对湿度
    plt.text(hum_minhour + 0.15, hummin - 0.95, str(hummin) + '%', ha='center', va='bottom', fontsize=10.5,
             color='#9370DB')  # 标出最低相对湿度
    
    plt.xticks(x)
    plt.savefig(savepath+'\相对湿度变化图.png', dpi=800)#保存图片到指定文件夹
    plt.show()
    #plt.close()


# 降雨量曲线图
def rainfalldiagram(hours,rainfall,rainfallavg,rainfallmax,hour_rainfallmax,rainfallmin,hour_rainfallmin,city):
    x = []#时间为x坐标
    y = []#降雨量为y坐标
    plt.figure(3, figsize=(16, 10))#定义图片大小和序号
    
    #制作数据变化的动画效果
    for i in range(0, 24):
        x.append(i)
        y.append(rainfall[hours.index(i)])  # 每迭代一次，将i放入y中画出来
        plt.cla()  # 清除键
        plt.bar(x, y, color='#7FFFD4', width=0.7,label='降水量')
        plt.legend()
        plt.pause(0.15)#暂停0.15s便可以得到动画效果
        
    #定义图片标题，x轴和y轴坐标名称
    plt.title(city+'一天降水量变化柱状图')
    plt.xlabel('时间/h')
    plt.ylabel('降水量/mm')
   
   # 画出平均降水量虚线
    plt.plot([0, 24], [rainfallavg, rainfallavg], color='#5595F9', linestyle='--', label='平均降水量')  
    plt.text(hour_rainfallmax, rainfallmax + 0.01, str(rainfallmax) + 'mm', ha='center', va='bottom', fontsize=10.5,
             color='#9370DB')  # 标出最高降水量
    plt.text(hour_rainfallmin, rainfallmin + 0.01, str(rainfallmin) + 'mm', ha='center', va='bottom', fontsize=10.5,
             color='#9370DB')  # 标出最低降水量
    
    plt.xticks(x)
    plt.savefig(savepath+'\降水量变化图.png', dpi=800)#保存图片到指定文件夹
    plt.show()
    #plt.close()


# 风向雷达图
def windradar(temp,city):
    plt.figure(4, figsize=(16, 10))#定义图片大小和序号
    N = 8 #定义分为八个方向
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)#将0-2pi分为8块
    radii = np.array(temp)#半径为该方向的平均风级大小
    width = np.pi / 4 #每一块为pi/4大小
    colors = plt.cm.viridis(np.random.rand(N))#随机八块的颜色
    labels=['东风','东北风','北风','西北风','西风','西南风','南风','东南风']#用于对八块进行贴标签
    
    plt.subplot(projection='polar')
    #定义图片标题
    plt.title(city+'一天风级图')
    plt.bar(theta, radii, width=width, color=colors,alpha=0.3, bottom=0.0)#绘制极坐标图
   
    #对每一块贴上对应的标签
    for angle,radius,label in zip(theta,radii,labels):
        plt.text(angle,radius,label,ha='center',va='bottom',fontsize=14.5,color='black')
   
    plt.savefig(savepath+'\风向雷达图.png', dpi=800)#保存图片到指定文件夹
    plt.show()
    #plt.close()


# 皮尔逊相关系数函数
def coefficient(var1,var2):
    var1=var1[0:24].astype(float)
    var2=var2[0:24].astype(float)
    aavg = sum(var1)/len(var1)#变量1的平均值
    bavg = sum(var2)/len(var2)#变量2的平均值
    covab = sum([(x - aavg)*(y - bavg) for x,y in zip(var1,var2)])#变量1和变量2的协方差
    asd= math.sqrt(sum([(i - aavg)**2 for i in var1]))#变量1的标准差
    bsd= math.sqrt(sum([(j - bavg)**2 for j in var2]))#变量2的标准差
    raletive_coe = covab/(asd*bsd) #变量1和2的皮尔逊相关系数
    return round(raletive_coe,4)

# 温湿度相关性分析
def relevancediagram(tems,hums,x,w,b,f):
    plt.figure(5, figsize=(16, 10))#定义图片大小和序号
    
    #定义图片标题，x轴和y轴坐标名称
    plt.title("温湿度相关性分析图")
    plt.xlabel("温度/℃")
    plt.ylabel("相对湿度/%")
    
    plt.scatter(tems, hums, color='#7FFFD4')#绘制散点图
    plt.plot(x, f)#绘制线性回归拟合曲线
    
    #标出线性回归方程和皮尔逊相关系数
    plt.text(20.1, 95.0, '线性回归方程:\nY=' + str(round(w, 3)) + 'X+' + str(round(b, 3)),
             fontdict={'size': '10', 'color': '#02082D'})
    if (coefficient(tems, hums) < 0):
        plt.text(20, 77.5, "相关系数为：" + str(coefficient(tems, hums)) + ',温湿度线性负相关',
                 fontdict={'size': '15', 'color': '#5595F9'})
    elif (coefficient(tems, hums) == 0):
        plt.text(20, 77.5, "相关系数为：" + str(coefficient(tems, hums)) + ',温湿度不存在线性相关',
                 fontdict={'size': '15', 'color': '#5595F9'})
    elif (coefficient(tems, hums) > 0):
        plt.text(20, 77.5, "相关系数为：" + str(coefficient(tems, hums)) + ',温湿度线性正相关',
                 fontdict={'size': '15', 'color': '#5595F9'})
        
    plt.savefig(savepath+'\温湿度相关性分析图.png', dpi=800)#保存图片到指定文件夹
    plt.show()
    #plt.close()
