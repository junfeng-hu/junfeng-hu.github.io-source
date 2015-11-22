Title: OAuth 2.0 Bearer Token Usage
Date: 2015-06-08 16:17:44
Author: junfeng
Category: 程序员
Tags: OAuth2.0, Bearer

###引入
在给Tornado编写豆瓣API的类时, 在查看文档时, 发现其access_token
并不像其它网站那样是传在query或者body中的. 而是放入headers中.
即: `headers["Authorization"] = Bearer <access_token>`

搜索OAuth2.0 Bearer, 在RFC 6750中找到了详细介绍

###使用access_token方法
标准中给出了3种access_token的使用方法:

1. 使用headers的Authorization字段(格式如上)
2. form字段形式放入POST请求的body中
3. query形式放入url中

标准推荐使用第一种方法. 第三种并不推荐, 因为access_token有可能泄漏.


###参考
http://self-issued.info/docs/draft-ietf-oauth-v2-bearer.html
