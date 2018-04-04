# -*- coding:utf-8 -*-

import requests
from bs4 import BeautifulSoup
import re
#DOWNLOAD_URL = 'http://www.cnblogs.com/grandyang/p/8642157.html'
DOWNLOAD_URL = 'http://www.cnblogs.com/grandyang/p/4606334.html'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36'
                                      ' (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}


class Leetcode:
	def __init__(self,url,headers):
		self.headers=headers
		self.baseUrl=url

	def getUrls(self):
		res=requests.get(self.baseUrl,headers=self.headers).content

		html=BeautifulSoup(res, 'lxml')
		soup=html.find('tbody').findAll('tr')
		Info=[]
		for page in soup:
			title=page.get_text().strip().split('\n')
			#print(page.get_text())
			href=page.find('a').get('href')
			
			title.append(href)
			#print(title)
			Info.append(title)
		return Info
	def nextPage(self,next_url):
		html=requests.get(next_url,headers=headers).content
		res=BeautifulSoup(html,'lxml')	

		name=res.find('a',class_='postTitle2').get_text()
		txtBody=res.find('div',id='cnblogs_post_body')

		str1=txtBody.get_text()
		return name+'\n'+str1


	def getPage(self,title):
		QuestionNo=title[0]
		Questiontitle=title[1]
		PassingRate=title[2]
		diffCult=title[3]
		PageUrl=title[-1]

		html=requests.get(PageUrl,headers=headers).text
		res=BeautifulSoup(html,'lxml')
		#print(res)

		name=res.find('a',class_='postTitle2').get_text()
		title[1]=name

		txtBody=res.find('div',id='cnblogs_post_body')
		#nextUrl=txtBody.find('a',target='_blank').get('href')
		#print(nextUrl+'nextUrl')
		#print(txtBody.get_text().replace('\xa0',''))


		#print(txtBody.get_text())
		with open('leetCode.txt','a',encoding='utf-8') as f:
			
			#f.write(str('\n'.join(title)).replace('\xa0',''))
			#f.write('\t'.join(title)+'\n')				
			f.write(txtBody.get_text())

			'''
			if not nextUrl:
				str1=self.nextPage(nextUrl)
				f.write(str1.replace('\xa0',''))
			'''
	
if __name__ == '__main__':
	Leetcode=Leetcode(DOWNLOAD_URL,headers)
	urlList=Leetcode.getUrls()
	for url in urlList:
		print(url)
		Leetcode.getPage(url)






'''
code=res.find('tbody')
#.get_text()
#print(code[0])
for page in code.findAll('tr'):
	title=page.get_text()
	href=page.find('a').get('href')
	print(title.split('\n')[1])
	print(href)

#print(code.split('\n'))

#print(list(code))
'''






