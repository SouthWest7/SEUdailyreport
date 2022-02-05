import time
import os
from selenium import webdriver

#打开Chrome浏览器
driver=webdriver.Chrome()
driver.get("http://ehall.seu.edu.cn/qljfwapp2/sys/lwReportEpidemicSeu/index.do?t#/dailyReport")
#driver.maximize_window() #最大化谷歌浏览器

#办事大厅登录
username = driver.find_element_by_css_selector('#username')
password = driver.find_element_by_css_selector('#password')
username.clear()
password.clear()
username.click()
#输入
username.send_keys("your_username")
password.send_keys("your_password")
#点击登录
driver.find_element_by_xpath("//*[@id=\"casLoginForm\"]/p[5]/button").click()
time.sleep(10)

#新增
driver.find_element_by_xpath("/html/body/main/article/section/div[2]/div[1]").click()
time.sleep(1)
driver.find_element_by_name("DZ_JSDTCJTW").send_keys("36")
#driver.find_element_by_xpath("/html/body/div[11]/div[1]/div[1]/div[2]/div[2]/a").click()

driver.quit()
