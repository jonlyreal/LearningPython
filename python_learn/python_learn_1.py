'''
Author ：SunJie
一开始，我希望我能使用selenium来打开一个网页
于是，我安装了Python3.6的包，然后用pip install selenium的方法，下载了selenium
'''

from selenium import webdriver #下载了selenium之后，我可以把selenium导入进来

my_window = webdriver.Chrome() #申明了一个chrome浏览器
my_window.get("https://www.99bill.com") #用浏览器打开快钱的官网
my_window.close() #关闭浏览器

'''
至此，我发现，我已经可以用selenium打开浏览器并访问我输入的网站了
'''







