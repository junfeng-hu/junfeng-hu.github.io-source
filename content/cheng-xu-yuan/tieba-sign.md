Title: tieba sign
Date: 2013-05-09 17:22
Author: algu
Category: 程序猿
Tags: 贴吧
Slug: tieba-sign

贴吧批量签到

使用requests,bs4

[code language="python"]

\#!/usr/bin/env python  
\#!---coding=utf8---  
import requests  
import bs4

urlt='http://tieba.baidu.com/f?kw='  
signurl='http://tieba.baidu.com/sign/add'

tieba=[]  
f=open('tiebas.txt','r')  
tieba=f.read().splitlines()  
f.close()  
headers={}  
f=open('configs.txt','r')  
for line in f:  
if line[0]=='\#':  
continue  
line=line.rstrip('\\n')  
key,value=line.split('=',1)  
headers[key]=value  
f.close()

data={}  
data['ie']='utf-8'

for t in tieba:  
data['kw']=t.decode('gbk').encode('utf-8')  
\#on linux  
\#data['kw']=t  
\#t=t.decode('utf-8').encode('gbk')  
url=urlt+t  
r=requests.get(url,headers=headers)  

data['tbs']=bs4.BeautifulSoup(r.text).body.find('script').string.split('"')[1].encode('utf-8')  
r=requests.post(signurl,headers=headers,data=data)  
if r.url==signurl:  
print t+'吧签到成功'.decode('utf-8').encode('gbk')  
a=raw\_input('Press Enter to exit:')

[/code]

使用PyInstaller打包成exe文件。

下载地址：[文件](http://pan.baidu.com/share/link?shareid=495612&uk=2887257007)
