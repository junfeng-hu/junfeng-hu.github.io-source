Title: 传话游戏
Date: 2013-04-06 23:38
Author: algu
Category: 程序猿
Tags: 传话游戏
Slug: e4bca0e8af9de6b8b8e6888f

<div>

非游戏规则，仅含代码．

</div>

<div>

编程之美资格赛题一代码

</div>

<div>

纯C++风格，那什么Ｃ风格弱暴了．

</div>

<div>

大神轻拍．

</div>

<div>

</div>

<div>

</div>

[code language="cpp"]

\#include\<iostream\>  
\#include\<string\>  
\#include\<map\>  
\#include\<vector\>  
\#include\<cstdio\>  
using namespace std;  
map\<string,string\> word\_change;  
vector\<string\> sentence;  
void change()  
{  
for(vector\<string\>::iterator
be=sentence.begin();be!=sentence.end();++be)  
{  
if(word\_change.count(\*be)==0)  
continue;  
if(word\_change.count(\*be)==1)  
\*be=word\_change[\*be];  
}  
}  
int main()  
{  
int T,N,M;  
char en;  
cin \>\> T;  
string word,key,value;  
for (int i=0 ;i!=T;++i)  
{  
cin \>\> N \>\> M;  
for (int j=0;j!=M;++j)  
{  
cin \>\> key \>\> value;  
word\_change[key]=value;  
}  
while(cin \>\> word)  
{

sentence.push\_back(word);  
if((en=getchar())=='\\n'|| en==EOF)  
break;  
}  
for(int k=0;k!=N-1;k++)  
change();  
cout \<\< "Case \#" \<\< i+1 \<\< ":";  
for(vector\<string\>::iterator
be=sentence.begin();be!=sentence.end();++be)  
cout \<\< " " \<\< \*be ;  
cout \<\< endl;  
word\_change.clear();  
sentence.clear();  
}  
return 0;  
}

[/code]
