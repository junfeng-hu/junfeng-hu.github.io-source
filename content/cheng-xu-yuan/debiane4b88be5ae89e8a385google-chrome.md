Title: Debian下安装Google Chrome
Date: 2012-09-21 20:52
Author: algu
Category: 程序猿
Tags: Debian装google chrome
Slug: debiane4b88be5ae89e8a385google-chrome

今天突然发现了一个小问题，wmaker下竟然没有一个可用的浏览器！自带的w3m实在过于奇葩，于是就在软件源里找可用的浏览器，可软件源今天也出问题了！不知怎么的竟然发现了我们学校的源没有公共许可密钥。于是开始自救。网上说在任意文件下新建个名为“key0x07DC563D1F41B907.asc”的文件。我建在home/下，键入命令：nano
key0x07DC563D1F41B907.asc

输入以下内容：

> -----BEGIN PGP PUBLIC KEY BLOCK-----  
>  Version: PGP Universal 2.0.3  
>  mQGiBDf3hHARBAC/pUIb79CHi2b1LdPI1pUgAMMVAcpLk+g+LRUcNnTVWrXBUkLv  
>  gjbraraA1jw728X7RE7BCqQc8TO2AkqZu4E16a4hFms58agPRtyXHcQMqRSBjkT2  
>  hXC73sO/nookcmtFNeiNSTTvrITcDabhs8rnVNYCJxpUm0yZBwnripzNlwCgl2OZ  
>  7W3M0hMahh/nPO/pqkQIO60D/RUoWs5bBZ0BAeTfUJpCjGpE0SiT/cryZSF9sKEx  
>  cPN135PURKVytofxc8bv2ZSd9v1CG+iO2JcmQ8ie7CD+qnub6AW9Uf6uFFfDpdgG  
>  2k2cZGoHMdiw6mnSb5fbvwCKgi9Nj3AOeDF7WcgFdQFLags28vfypL/RH2XhPfBe  
>  4EV+A/9TZ1Kxgk69dn3l5BGpwudmzHiD1142G7eZI1JlM4pJuOw6YY+NRDeVEbcF  
>  iP5diGZWdcoRYgwEEfLpgl7ok0ScRN3wPfZtmUl3GACsAZbxh06utkP2X3Lptopd  
>  PuoJhlKD6FpK99TDD34TWy76tBmigzm/CkLaTI4gawpWs5D89LQoQ2hyaXN0aWFu  
>  IE1hcmlsbGF0IDxtYXJpbGxhdEBkZWJpYW4ub3JnPohGBBARAgAGBQI9GPl1AAoJ  
>  ELed76p6J6DMsMwAn2/I4VYcMENSdO/FM+6Yb/1PGv+HAJ4zn+3i7Z+R/iDhx7c+  
>  luDpfBTe+IhGBBARAgAGBQI9GWSJAAoJELz2xg9ugWnSt6AAoJPHD0N6LnQMUZxv  
>  7MkcUIRE88CMAJwI5lVoJ0TCFHG/49pcjN7Lzbc1RohhBBMRAgAZBAsKBAMDFQMC  
>  AxYCAQIXgAUCQRiYygIZAQASB2VHUEcAAQEJEAfcVj0fQbkHn/IAmwahlSO4z8f3  
>  YToV+72CX6sWvkehAJ4q9zOytEMKy/Vk08w7h+3mOLR56IkBIgQQAQIADAUCQ7jd  
>  6AUDABJ1AAAKCRCXELibyletfNmOB/9V5AMQgN8WCxrToFjWf8aEN3v+6frpfUa/  
>  6u88J+31/6jGQI83lK1Kp9fIZQwA9JuZxT+hTwsmc6SiU3NnGQl8ZejupoJwvxex  
>  OPSB3CtzmhjB2VDNE5tU9yRq6Qpz9QNK0e4vl8pDvrUjkqHJH3VPz+ORYbPrsCHx  
>  afrIosI7alyjqv231i8mriOjFY5JDIXuj+xq4hMzGtFJOC4BNZWqtIH3tkFj2m/f  
>  l7SIwUa42YboT9IAfJ+ZVr2FZREOrXmVA9rDJPodAD8ComxS0VUWYxi85mE2KqPw  
>  HcARXGri10hmfSpiUBRH4snUZzJozEAgah5W/g/heSyiHYEGsPvtuQGNBDf3hM4Q  
>  BgCM2yVxcrBFgwUDOxbBqBbTEfYc5If3POLMRglvOuJ9/H1iEJ5Wk6+zcz21jxPa  
>  4FQrk2F/faGeRV1cy0A7qmibmQpvewJwgzeY7wOIulPYlAd23+VQPhN53GYVwO75  
>  GA1vst0tI26VRKscpt73PatCcykrgNWHWjvDKmDC4V2T+OFz4okOC1VYc9qfcVvH  
>  F1R3lgAnFBTObx49K1+UyGatvWiZTtofETDZ8aHzsd0ObJoLHHmmHye5bgE9yRLj  
>  5L8AAwUF/0L/TXmzjtJ3hmXC86OB7Vzqe/n8MVqWElq4OzzEXi0PxzbgLzcEN+KV  
>  o4iXaNZ2/oI79dLblYixS6wh/cG2XT6RTG1R1CiubmJXGiFn6xeAw5aiQTKZBjUi  
>  nXqFxR/ZtH4p8/ZAzk2SpAOEIp5Gqfg0OCxgHqWmNWR64vfPJKND6qcoQRQ8a+3V  
>  77xq0ZurHejwprjaUf7FHOK/u6lc8eW7JdCKisZ7efdGdu8QVFnmkpeHvyCyDpkC  
>  rc4mmetj4ohGBBgRAgAGBQI394TOAAoJEAfcVj0fQbkHp0QAnA3/HBLEhjAydk5n  
>  Z+PeV+Fxs+h8AJoDew5wFKb477LBOz0qyWxe+byZzg==  
>  =oDfT  
>  -----END PGP PUBLIC KEY BLOCK-----

Crtl+o保存，Crtl+x退出nano。

再在root下输入命令：apt-key add key0x07DC563D1F41B907.asc

更新源，成功认证！

但google，firefox，opera在源里都找不到！于是再次上网，由于对google的怀旧，就找装google
chrome的方法：

nano /etc/apt/sources.list 打开源地址设置文件，追加google的源

deb http://dl.google.com/linux/deb/ stable main

同样要设置认证：

输入：wget -q -O –
https://dl-ssl.google.com/linux/linux\_signing\_key.pub | sudo apt-key
add -

然后：apt-get update

安装测试版：apt-get install google-chrome-beta

不稳定版：apt-get install google-chrome-unstable

不过貌似装下来比较大需要100多M的硬盘空间，这对爱惜内存、磁盘空间的linux用户可不算好。

最后秀一下自己的劳动成果

[![](http://www.jcodef.com/wp-content/uploads/2012/09/igc-300x230.jpg "igc")](http://www.jcodef.com/wp-content/uploads/2012/09/igc.jpg)

 
