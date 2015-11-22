Title: Python struct and Endianness
Date: 2014-01-10 21:02
Author: algu
Category: 程序猿
Tags: endianness, struct
Slug: python-struct-and-endianness

偶然间在stackoverflow上看到下面这个问题:

>     Please explain me what does this piece of code do.
>
>     h should be 32Byte result from sha256 calculation.
>
>     I am rewriting parts of this code for my project in C++ and I'm not sure if this switches byte order per 4byte chunk or change byte order on whole 32byte number.
>
>     def reverse_hash(h):
>         return struct.pack('>IIIIIIII', *struct.unpack('>IIIIIIII', h)[::-1])[::-1]
>     And, how does this array index work ?
>
>        [::-1]
>     Thanks for any and all info

Python的splice到还好理解.但对于代码里struct的使用倒是很是疑惑.  
遂搜索struct module的使用.

> This module performs conversions between Python values and C structs
> represented as Python strings.

用法也就参考文档.

当遇到字节序的时候,产生了疑惑.  

不同的架构有不同的字节序.大致有三种,大端(Big-endian),小端(Little-endian),双端(Bi-endian).(貌似还有Middle-endian).  
简单来说,  
大端是高位字节在低地址处,低位字节在高地址处,  
小端是低位字节在低地址处,高位字节在高地址处.  
双端是字节序可以配置.

理解:  
1. 内存中的数据写进去就不再改变.只是解析的顺序不同才有大端,小端一说.  
2.
字节序大端小端之说针对的是单个内存单元之内的字节顺序.单元与单元之间只是按地址线性增长.

先看wiki上的一个例子:  
字符串"XRAY"的存储分配.  
XRAY 字符值表:

  --- ------
  X   0x58
  R   0x52
  A   0x41
  Y   0x59
  --- ------

  : character int value

以一个字节为存储单元:

  ------- ------- ------- ------- ------- -------
  `...`   `"Y"`   `"A"`   `"R"`   `"X"`   `...`
  ------- ------- ------- ------- ------- -------

  : addresses from right to left

以两个字节为单位:  
要表示"XRAY",内存实际分布:

  ------- -------- -------- -------
  `...`   `"AY"`   `"XR"`   `...`
  ------- -------- -------- -------

  : addresses from right to left

测试代码:

    # coding: utf-8
    import struct
    s="XRAY"
    little_s_uchar_hex=map(hex,struct.unpack("BBBB",s))
    print "big_s_uchar_hex:",big_s_uchar_hex
    big_s_ushort_hex=map(hex,struct.unpack(">HH",s))
    print "big_s_ushort_hex:",big_s_ushort_hex
    #output:
    '''
    little_s_uchar_hex: ['0x58', '0x52', '0x41', '0x59']
    little_s_ushort_hex: ['0x5258', '0x5941']
    big_s_uchar_hex: ['0x58', '0x52', '0x41', '0x59']
    big_s_ushort_hex: ['0x5852', '0x4159']
    '''

观察little\_s\_ushort\_hex的值.由于笔者使用的是x86的机子(小端字节序).  
little\_s\_ushort\_hex在内存中的存储序列是:  
0x52 0x58 0x59 0x41  
即为AYXR(地址从右向左增长)  
和wiki中的表示相符.

再来看一个例子  
将一个8位的字符串unpack成8个unsigned char,4个unsigned short,2个unsigned
int,1个unsigned long long

    #!/usr/bin/env python2
    # coding: utf-8
    import struct

    string='hjflyllx' # my prefered string
    print ('string:%s' % string)
    string_hex=map(hex,map(ord,string))
    print ('-'*20)
    print ('string_hex:')
    print (string_hex)

    little_uchar_string=struct.unpack("BBBBBBBB",string)
    print ('big_uchar_string:')
    print (big_uchar_string)
    big_uchar_string_hex=map(hex,big_uchar_string)
    print ('big_uchar_string_hex:')
    print (big_uchar_string_hex)

    little_ushort_string=struct.unpack("HHHH",string)
    print ('big_ushort_string:')
    print (big_ushort_string)
    big_ushort_string_hex=map(hex,big_ushort_string)
    print ('big_ushort_string_hex:')
    print (big_ushort_string_hex)

    little_uint_string=struct.unpack("II",string)
    print ('big_uint_string:')
    print (big_uint_string)
    big_uint_string_hex=map(hex,big_uint_string)
    print ('big_uint_string_hex:')
    print (big_uint_string_hex)

    little_ullong_string=struct.unpack("Q",string)
    print ('big_ullong_string:')
    print (big_ullong_string)
    big_ullong_string_hex=map(hex,big_ullong_string)
    print ('big_ullong_string_hex:')
    print (big_ullong_string_hex)

    #output:
    '''
    string:hjflyllx
    --------------------
    string_hex:
    ['0x68', '0x6a', '0x66', '0x6c', '0x79', '0x6c', '0x6c', '0x78']
    --------------------uchar big and little endianness--------------------
    little_uchar_string:
    (104, 106, 102, 108, 121, 108, 108, 120)
    little_uchar_string_hex:
    ['0x68', '0x6a', '0x66', '0x6c', '0x79', '0x6c', '0x6c', '0x78']
    big_uchar_string:
    (104, 106, 102, 108, 121, 108, 108, 120)
    big_uchar_string_hex:
    ['0x68', '0x6a', '0x66', '0x6c', '0x79', '0x6c', '0x6c', '0x78']
    --------------------ushort big and little endianness--------------------
    little_ushort_string:
    (27240, 27750, 27769, 30828)
    little_ushort_string_hex:
    ['0x6a68', '0x6c66', '0x6c79', '0x786c']
    big_ushort_string:
    (26730, 26220, 31084, 27768)
    big_ushort_string_hex:
    ['0x686a', '0x666c', '0x796c', '0x6c78']
    --------------------uint big and little endianness--------------------
    little_uint_string:
    (1818651240, 2020371577)
    little_uint_string_hex:
    ['0x6c666a68', '0x786c6c79']
    big_uint_string:
    (1751803500, 2037148792)
    big_uint_string_hex:
    ['0x686a666c', '0x796c6c78']
    --------------------ullong big and little endianness--------------------
    little_ullong_string:
    (8677429850801597032,)
    little_ullong_string_hex:
    ['0x786c6c796c666a68']
    big_ullong_string:
    (7523938743555484792,)
    big_ullong_string_hex:
    ['0x686a666c796c6c78']
    '''

下面是一些表格,假设地址开始于100

  address   character   hex value
  --------- ----------- -----------
  100       h           0x68
  101       j           0x6a
  102       f           0x66
  103       l           0x6c
  104       y           0x79
  105       l           0x6c
  106       l           0x6c
  107       x           0x78

  : string

  address   characters   hex value
  --------- ------------ -----------
  100       jh           0x6a68
  102       lf           0x6c66
  104       ly           0x6c79
  106       xl           0x786c

  : little ushort

  address   characters   hex value
  --------- ------------ ------------
  100       lfjh         0x6c666a68
  104       xlly         0x786c6c79

  : little uint

  address   characters   hex value
  --------- ------------ --------------------
  100       xllylfjh     0x786c6c796c666a68

  : little ulonglong

uchar那一项可以看出当内存单元大小是一个字节时,大端,小端字节序是一样的.  

而其它多于1个字节的内存单元,可以看到**相对应的项的字节顺序正好颠倒.但单元与单元之间的顺势都是递增的.**

现在我们来看其中一个人的回答:

>     >>> h = ''.join(map(str, range(0,21)))
>     >>> h
>     '01234567891011121314151617181920'
>     >>> struct.pack('>IIIIIIII', *struct.unpack('>IIIIIIII', h)[::-1])[::-1]
>     '32107654019821114131615181710291'
>     Equivalent expression:
>
>     >>> struct.pack('<IIIIIIII', *struct.unpack('>IIIIIIII', h))
>     '32107654019821114131615181710291'

主要看其给出的相等实现:

    >>> struct.pack('<IIIIIIII', *struct.unpack('>IIIIIIII', h))

为什么这个也能得出相同的结果?  

采用不同的字节序进行unpack,pack一个字符串,就能得出单元内存内的字符串翻转.  
你应该知道了为什么吧!

同样假设开始内存地址是100,我们只分析一个内存单元(4个字节),

见表:

  address   character
  --------- -----------
  100       '0'
  101       '1'
  102       '2'
  103       '3'

先是以大端字节序来unpack,读出的内容就是'0123'的内存表示的整数.  

然后以小端来pack,小端是低位在前,高位在后,进行继续读,从103-100,读到的也就是'3210'了.  
参考链接:  
http://docs.python.org/2/library/struct.html  
http://en.wikipedia.org/wiki/Endianness  

http://stackoverflow.com/questions/20882693/what-does-this-piece-of-python-indexing-code-do
