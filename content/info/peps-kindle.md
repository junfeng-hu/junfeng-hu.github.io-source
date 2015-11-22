Title: PEPS doc Kindle版本
Date: 2015-06-09 22:07:32
Author: junfeng
Category: 信息
Tags: Python, Kindle

###介绍
Python上遇到的很多问题搜到最后经常链接到PEP, 觉得PEPS需要研读一下.
一时半会儿看不完的东西总想着放到Kindle里看(很有可能不会再看), 于是
就制作了这个mobi版本的Python Enhancement Proposals.

[下载地址][1]

###过程
hg clone下来, 然后转成html. 使用[代码][2]解析html, 用kindlegen生成
mobi文件.

吐槽:

1. Python官方积极推动代码移植到Python 3, 可peps中的转换代码都是
   老版本的Python 2
2. kindlegen的`-c2`选项很占用CPU, 且处理时间臭长, 但生成文件体积
   变化并不大
3. PEP的两种格式处理起来带来不少麻烦, 并且其生成的html文档结构
   很简单, 没有程序处理需要的元信息.

###TODO
本来应该按照分类做成类似期刊格式的文档, 但时间不够用, 没有制作
期刊的模板, 以后有时间再做.

应该免去转成html那一步, 直接利用原生格式, 需要学习PEP文档的两种
格式.

Python应该统一PEP格式, 把两种格式使用程序转成一种.



[1]: https://raw.githubusercontent.com/grepcook/peps_mobi/master/Python%20Enhancement%20Proposals.mobi
[2]: https://github.com/grepcook/peps_mobi/blob/master/pep2mobi.py
