Title: Python２编码小结
Date: 2013-03-12 17:10
Author: algu
Category: 程序猿
Tags: encode, Python
Slug: pythonefbc92e7bc96e7a081e5b08fe7bb93

Python中的编码挺让人烦的．学习了一下，记录在此．首先查看你系统默认输入输出的编码．  

` #!/usr/bin/env python #!---coding=utf-8--- import sys print 'stdin_encoding:%s' % sys.stdin.encoding print 'stdout_encoding:%s' % sys.stdout.encoding`

OutpUt  
stdin\_encoding:UTF-8  
stdout\_encoding:UTF-8  
</code>  

` >>> a='你好' >>> a 'xe4xbdxa0xe5xa5xbd' >>> type(a) <type 'str'> >>> b=a.decode('utf-8') >>> type(b) <type 'unicode'> >>> a.encode('gbk') Traceback (most recent call last): File "", line 1, in UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)`  
首先a的类型是str，其以UTF-8编码．str有两个关于编码的方法．  
str.encode和str.decode  
b=a.decode('utf-8') 将a解码，返回类型为unicode.  
同时a又有encode方法．但a.encode('gbk')
抛出了解码错误．那么encode方法又有什么用呢？？  
看下面的例子：  

` >>> c='Hello' >>> c 'Hello' >>> c.decode('utf-8') u'Hello' >>> d=c.decode('utf-8') >>> d u'Hello' >>> d.encode('gbk') 'Hello' >>> e=d.encode('gbk') >>> e 'Hello'`  

当str变量中只含有ascii字符时使用c.encode('gbk')顺利通过．我想c.encode()应该是先decode再encode的，而且默认是ascii来解码的．这样因为a中含有汉字，ascii也就无法解码了．  

` >>> f=b.encode('gbk') >>> f 'xc4xe3xbaxc3' >>> g=f.decode('gbk') >>> g u'u4f60u597d' >>> g==b True >>> f.decode('utf-8') Traceback (most recent call last):   File "", line 1, in    File "/usr/lib/python2.7/encodings/utf_8.py", line 16, in decode     return codecs.utf_8_decode(input, errors, True) UnicodeDecodeError: 'utf8' codec can't decode byte 0xc4 in position 0: invalid continuation byte`  

从上面可以看出汉字在不同的编码下，码值是不同的，所以decode时就要传入正确的编码方式，不然就会抛出像上面这样的异常．

在Python3中str取代了unicode类型，没有了decode方法．这样str类型的变量只能encode了，返回的是bytes类型．
