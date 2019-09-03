#encoding=utf-8
#################################################################################################
#Author：bo.wu
#   1.0：简单框架搭建
#   2.0：用tesseract解决验证码识别的问题
#   2.1：用requests添加header的验证方式库解决登录时无法获取验证码的问题
#   2.2：解决模块导入问题-代码分离
#   2.3：beautifulsoup解决随机classname无法捕捉元素问题
#   2.4：inspect库解决通用每个步骤睡眠时间问题(因打包原因导致无法getsourceline,后期再优化)
#   2.5：目前只能使用继承的方式解决类属性传入装饰器的问题(因打包原因导致无法getsourceline,后期再优化)
#   2.6：在__init__.py文件中添加__all__属性,可以导入所有的文件,帮助获取最新的用例类名
#   2.7：接入可视化数据报告(working)
#################################################################################################


import re
import sys
import os
import time
from case import *

#增加tesseract的临时环境变量,否则无法使用tesseract软件及验证码识别函数
os.system(r'set TESSDATA_PREFIX=C:\Tesseract-OCR')

#获取最新的用例,project为case目录下你的用例文件名去除数字编号
maincase=[i for i in dir() if 'project' in i][-1]
mainclass=maincase.capitalize()


#主程序，执行每一条用例
class Start:
	def __init__(self):
		#定义报告中统计的失败用例,通过用例,程序开始时间
		self.pass_case=0
		self.fail_case=0
		self.startime=time.time()
	def __call__(self):
		#调用并执行系统检查、系统功能测试用例
		self.syscheck()
		print('联动配置检查完毕,下面开始功能测试')
		self.runcase()
		self.report()
	def syscheck(self):
		#实例化测试用例类
		self.Test=eval('{}.{}()'.format(maincase,mainclass))
		#获取系统检查类用例
		checkcase=re.findall(r'example\d+',str(dir(self.Test)))#获取所有check名称
		#执行检查类用例
		for i in checkcase:
			eval('self.Test.{}()'.format(i))
	def runcase(self):
		#获取系统功能类用例
		self.allcase=re.findall(r'case\d+',str(dir(self.Test)))#获取所有case名称
		#将用例按照编号排序(根据长度排序)
		self.allcase.sort(key=lambda x:len(x))
		#执行功能类用例,并计数
		for i in self.allcase:
			try:
				eval('self.Test.{}()'.format(i))
				self.pass_case+=1
			except:
				self.fail_case+=1
				print('测试用例：{} 执行失败'.format(eval('self.Test.{}.__doc__'.format(i))))
	def report(self):
		#打印测试结果	,并退出
		print('###############################################################')
		print('总计用例：{}条,成功：{}条,失败：{}条'.format(len(self.allcase),self.pass_case,self.fail_case))
		print('All case finished in {:.2f} seconds'.format(time.time()-self.startime))
		sys.exit()


if __name__ == '__main__':
	Start()()