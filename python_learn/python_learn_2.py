'''
Author ：SunJie
我已经打开了浏览器，现在希望尝试对网站上的控件进行操作
'''

from selenium import webdriver #下载了selenium之后，我可以把selenium导入进来
import time


my_window = webdriver.Chrome() #申明了一个chrome浏览器
my_window.get("http://192.168.14.103:8083/osf-pvs-mock/ftl/requestApplyOsf.jsp") #用浏览器打开测试的网站


'''
使用find_element_by_name方法寻找控件
清空控件原有的内容
往控件里输入123456
'''
membercode = my_window.find_element_by_name('membercode')
membercode.clear()
membercode.send_keys('123456')

time.sleep(2) #插入休眠时间，方便看到效果，可删
my_window.close() #关闭浏览器


