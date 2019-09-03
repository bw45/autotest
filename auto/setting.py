#setting.py
import time
import inspect
from selenium import webdriver
from auto.tool.tools import Getcode

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class Setting:
	def __init__(self):
		self.inputurl()
		self.option=webdriver.ChromeOptions()
		self.option.add_argument("disable-infobars")
		self.driver=webdriver.Chrome(chrome_options=self.option)
		self.driver.maximize_window()
		self.driver.get(self.url)
		self.login()
	def inputurl(self):
		#输入测试地址
		print('################################################')
		print('请输入你要测试的IP地址(http://或者https://)')
		while 1:
			self.url=str(input('>>>>'))
			if 'http://' in self.url or 'https://' in self.url:
				break
			else:
				print('地址输入错误,请重新输入')
	def login(self,username='sysadmin',password='11111111'):
		#登录,具体元素请自定位
		self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
		self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
		code=Getcode(self.driver.page_source,self.driver.get_cookies(),self.url).codeToString()
		self.driver.find_element_by_xpath('//*[@id="auth-code"]').send_keys(code)
		self.driver.find_element_by_xpath('//*[@id="bangcle"]/div/div[3]/div/form/button').click()
		time.sleep(2)
		self.login_check()
	def login_check(self):
		#登录检查,判断页面源码是否改变
		if '登 录' in self.driver.page_source:
			print(r'验证码识别失败,重新识别中(识别率85%)')
			self.login_again()
		else:
			pass
	def login_again(self):
		#再次登录函数
		code=Getcode(self.driver.page_source,self.driver.get_cookies(),self.url).codeToString()
		self.driver.find_element_by_xpath('//*[@id="auth-code"]').send_keys(code)
		time.sleep(1)
		self.driver.find_element_by_xpath('//*[@id="bangcle"]/div/div[3]/div/form/button').click()
		time.sleep(2)
		self.login_check()
	def userquit(self):
		#用户退出,具体元素请自定位
		time.sleep(2)
		quit=self.driver.find_element_by_xpath('//*[@id="lg_header"]/div/div[2]/div[1]/span')
		ActionChains(self.driver).move_to_element(quit).perform()
		time.sleep(2)
		self.driver.find_element_by_xpath('//*[@id="lg_header"]/div/div[2]/div[1]/div/div/ul/li[3]').click()
		time.sleep(2)
	def system_check(self,value,name):
		#自定义系统检查功能
		pass
	def status_check(self,value):
		#自定义状态检查功能
		pass
	def content_check(self,value):
		#自定义报告内容检查功能
		if value in self.driver.page_source:
			pass
		else:
			self.driver.quit()
			print('{}异常'.format(value))
	def xclick(self,param):
		#xpath.click的转换函数,每条后增加睡眠时间,避免代码冗余及因响应问题无法定位
		self.driver.find_element_by_xpath(param).click() 
		time.sleep(1.2)
	def xsendkey(self,param,key):
		#xpath.sendkey的转换函数,同xclick
		self.driver.find_element_by_xpath(param).send_keys(key)
		time.sleep(1.2)
