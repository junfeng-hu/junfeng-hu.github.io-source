Title: Crashing Balloon
Date: 2013-05-24 17:15
Author: algu
Category: 程序猿
Tags: ZOJ1003
Slug: crashing-balloon

<style type="text/css"><!--<br />
pre { font-family: monospace; color: #000000; background-color: #ffffff; } body { font-family: monospace; color: #000000; background-color: #ffffff; } .Comment { color: #0000ff; } .Type { color: #2e8b57; font-weight: bold; } .Statement { color: #804040; font-weight: bold; } .Constant { color: #ff00ff; } .PreProc { color: #a020f0; } --><br></br>
--></style>
ZOJ Problem Set - 1003 Crashing Balloon

    #include<iostream>
    #include<cstring>
    using namespace std;
    int cur[101];//记录1~100的数的使用与否。
    int af[101];//记录数a的因式足迹以便回溯
    int bf[101];//记录数b的...
    int CheckMax(int a)//类似于求解b的因式
    {
        int k=1;
        bf[k]=1;
        while(k>0)
        {
            int i=bf[k]+1;
            while(i<=100)
            {
                if(!cur[i])
                    if(a%i==0)
                    {
                        bf[k]=i;
                        bf[++k]=i;
                        cur[i]=1;
                        a/=i;
                        break;
                    }
                ++i;
            }
            if(a==1)
                return 1;
            if(i==101)
            {
                --k;
                if(k==0)
                    break;
                cur[bf[k]]=0;
                a*=bf[k];
            }
        }
        return 0;
    }
    int Checkab(int a,int b)//回溯法求出b的所有因式。
    {
        int k=1,s=0;
        af[k]=1;//初始状态
        while(k>0)
        {
            int i=af[k]+1;
            while(i<=100)
            {
                if(!cur[i])
                    if(b%i==0)
                    {
                        cur[i]=1;
                        af[k]=i;//第k个因子
                        af[++k]=i;//判断第k+1个，从i+1开始
                        b/=i;
                        break;
                    }
                ++i;
            }
            if(b==1)//找到b的一个因式
            {
                if(CheckMax(a))
                    return 1;
                cur[af[--k]]=0;//回溯到第k-1个
                s=1;//标记b能被分解
                b*=af[k];//b回溯
            }
            if(i==101)
            {
                k--;//第k个因子没找到，回溯
                if (k==0)
                    break;
                cur[af[k]]=0;//解除占用
                b*=af[k];//b回溯到上一状态
            }
        }
        if(s==1)
            return 0;
        else
            return 1;
    }
    int main()
    {
        int a,b,t;
        while(cin >> a >> b)
        {
            memset(cur,0,sizeof(cur));
            if(a<b)
            {
                t=a;
                a=b;
                b=t;
            }
            if(Checkab(a,b))
                cout << a << endl;
            else
                cout << b << endl;
        }
        return 0;
    }

两个函数似乎可以合成一个。算了，AC了就行。算是用了一下回溯思想。
