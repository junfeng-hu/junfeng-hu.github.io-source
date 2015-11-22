Title: setjmp and longjmp
Date: 2013-11-03 15:35
Author: junfeng
Category: 程序猿
Tags: nolocaljmp
Slug: setjmp-and-longjmp

 

全局,静态,易失变量不受优化影响保存在存储器中,存放在存储器中的变量具有调用longjmp()时的值;进行优化后自动,寄存器变量保存寄存器中,CPU和浮点寄存器中的值恢复为调用setjmp()时的值.不进行优化,五种变量全部保存在存储器中.(来自APUE)
