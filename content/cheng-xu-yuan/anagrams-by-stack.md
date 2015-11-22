Title: Anagrams by Stack
Date: 2013-05-29 23:40
Author: algu
Category: 程序猿
Tags: stack
Slug: anagrams-by-stack

<style type="text/css"><!--<br />
pre { font-family: monospace; color: #000000; background-color: #ffffff; } body { font-family: monospace; color: #000000; background-color: #ffffff; } .Special { color: #6a5acd; } .Comment { color: #0000ff; } .Type { color: #2e8b57; font-weight: bold; } .Statement { color: #804040; font-weight: bold; } .Constant { color: #ff00ff; } .PreProc { color: #a020f0; } --><br></br>
--></style>
ZOJ Problem Set - 1004 Anagrams by Stack  

题目：[来源](http://acm.zju.edu.cn/onlinejudge/showProblem.do?problemCode=1004)

    #include <iostream>
    #include<cstring>
    using namespace std;
    #define N 100
    char source[100];//原word
    char target[100];//目标word
    char pop_push[200];//栈操作序列
    char stackf[100];//保存栈中栈中当前情况
    char out[100];//保存生成word
    void Search(int n,int p)//递归出所有的进栈出栈操作
    {
        if(p==2*n)//边界条件
        {
            int i=0,s=0,f=0,o=0;//s指向当前要进栈的字母，f指向栈顶，o指向out中当前可放位置
            for (;i!=p;++i)
            {
                if(pop_push[i]=='i')
                {
                    if(s==n)
                        break;//不合法的进栈，跳出
                    stackf[f++]=source[s++];
                }
                else
                {
                    if(f==0)
                        break;//不合法的出栈，跳出
                    out[o++]=stackf[--f];
                }
            }
            out[o]='\0';
            if(strcmp(target,out)==0)
            {
                int i;
                for (i=0;i!=p;++i)//输出
                    cout << pop_push[i] << " ";
                cout << endl;
            }
            return ;
        }
        pop_push[p++]='i';//首先进栈
        Search(n,p);//递归到下一层
        pop_push[p-1]='o';//退回，改成出栈
        Search(n,p);//下一层
    }
    int main()
    {
        while (cin >> source >> target)
        {
            int n=strlen(source);
            cout << "[" << endl;
            Search(n,0);
            cout << "]" << endl;
        }
        return 0;
    }

递归出所有栈操作，排除不合法的。找到满足条件的操作序列。
