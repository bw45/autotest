#project1.py
import time
from auto.case.check import Check

#system_version用例
class Project1(Check):
	def case1(self):
		#编写__doc__,执行用例失败时,会输出用例名称
		#请自定义用例内容
		#example1:
		'''导入用户license'''
		self.xclick('//*[@id="Main"]/div[3]/div[1]/ul/li[8]/ul/li[4]/span[2]')
		self.xsendkey('//*[@id="Main"]/div[3]/div[2]/div[1]/div[2]/div[1]/div[3]/div/input',os.path.abspath("file/auto.lic"))
		self.xclick('//*[@id="Main"]/div[3]/div[2]/div[2]/div/div/div[3]/button[1]')
		self.userquit()
	def case2(self):
		#同上,请自定义用例内容
		#example2:
		'''切换超级管理员登录'''
		self.login(username='superadmin@zdhcs',password='11111111')
		#此处增加睡眠时间,针对于个别加载慢的情况,需要单独处理
		time.sleep(1)
		self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[1]/div/div/input','11111111')
		self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[2]/div/div/input','1qaz@WSX')
		self.xsendkey('//*[@id="Main"]/div[9]/div/div[2]/div/form/div[3]/div/div/input','1qaz@WSX')
		self.xclick('//*[@id="Main"]/div[9]/div/div[3]/div/button[1]/span')	