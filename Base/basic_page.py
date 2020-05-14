from selenium import webdriver
from time import  sleep

#定义页面的基础类，所有的页面都需要继承这个基础类
class BasePage(object):
    #初始化基础类
    def __init__(self,driver,url):
        self.driver = driver
        self.url = url

    #启动浏览器，访问指定页面
    def open(self):
        self.driver.get(self.url)

    #定位元素
    def locator_element(self,*locator):
        el = self.driver.find_element(*locator)
        return el
