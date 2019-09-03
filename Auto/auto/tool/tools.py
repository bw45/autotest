#tools.py
import requests
import tesserocr
from bs4 import BeautifulSoup
from PIL import Image,ImageEnhance

class Getcode:
	def __init__(self,page_source,cookie,url):
		#获取源码及url、cookie
		self.page_source=page_source
		self.cookie=cookie
		self.url=url
	def getCodeurl(self):
		#获取验证码请求链接,请自定义
		html=BeautifulSoup(self.page_source,'lxml')
		url=[self.url+i['src'] for i in html.select('#bangcle > div > div:nth-child(3) > div > form > div:nth-child(4) > span:nth-child(4) > img')][0]
		self.getCode(url)
	def getCode(self,url):
		#请求验证码
		session='AK_SESSION={}'.format(self.cookie[0]['value'])
		header={'cookie':session}
		response=requests.get(url,headers=header)
		img=response.content
		#保存至本地图片
		with open('D:\\code1.jpg','wb') as f:
			f.write(img)
	def codeToString(self):
		#获取此次登录验证码随机数、请求验证码
		self.getCodeurl()
		#打开本地图片
		img=Image.open('D:\\code1.jpg')
		#色度增强
		img=ImageEnhance.Color(img).enhance(10)
		#亮度增强
		img=ImageEnhance.Brightness(img).enhance(100)
		#灰度处理
		img=img.convert('L')
		#展示图片
		# img.show()
		#阈值,控制二值化程度,自行检测适合该验证码的阈值
		threshold = 43
		#其实我也不知道这里是啥
		table = []
		for i in range(256):
			if i < threshold:
				table.append(0)
			else:
				table.append(1)
		#图片二值化
		img = img.point(table, '1')
		#转换图片至文字
		result=tesserocr.image_to_text(img)
		#...
		return result.strip()[-4:]
