Title: 图的最短路径
Date: 2012-11-24 00:56
Author: algu
Category: 程序猿
Tags: 图的最短路径
Slug: e59bbee79a84e69c80e79fade8b7afe5be84

迪杰斯特拉算法

<div>

-----------data.txt-----------

</div>

<div>

<div>

6 8

</div>

<div>

0 0 100 30 0 10

</div>

<div>

0 0 0 0 0 5

</div>

<div>

0 0 0 0 0 0

</div>

<div>

0 0 60 0 20 0

</div>

<div>

0 0 10 0 0 0

</div>

<div>

0 0 0 0 50 0

</div>

</div>

<div>

----------code.cpp----------

</div>

<div>

<div>

\#include\<stdio.h\>

</div>

<div>

\#include\<stdlib.h\>

</div>

<div>

\#include\<limits.h\>

</div>

<div>

\#define Max\_vnum 50

</div>

<div>

int final[Max\_vnum];

</div>

<div>

int D[Max\_vnum];

</div>

<div>

typedef struct Path{int adj;struct Path \*next;}Path;

</div>

<div>

Path \*P[Max\_vnum];

</div>

<div>

typedef struct {

</div>

<div>

     int arc[Max\_vnum][Max\_vnum];

</div>

<div>

     int vexnum,arcnum;

</div>

<div>

}MGraph;

</div>

<div>

void InitGraph(MGraph &G)

</div>

<div>

{

</div>

<div>

     FILE \*fin;

</div>

<div>

     int t;

</div>

<div>

     fin=fopen("data.txt","r");

</div>

<div>

     fscanf(fin,"%d%d",&G.vexnum,&G.arcnum);

</div>

<div>

     for(int i=0;i\<G.vexnum;++i)

</div>

<div>

     {

</div>

<div>

          for(int j=0;j\<G.vexnum;++j)

</div>

<div>

          {

</div>

<div>

               fscanf(fin,"%d",&t);

</div>

<div>

               if(t==0)

</div>

<div>

                    G.arc[i][j]=INT\_MAX;

</div>

<div>

               else

</div>

<div>

                    G.arc[i][j]=t;

</div>

<div>

          }

</div>

<div>

     }

</div>

<div>

     return ;

</div>

<div>

}

</div>

<div>

void ShortestPath\_DIJ(MGraph G,int v0)

</div>

<div>

{

</div>

<div>

     int min,w,v,isend=-1;

</div>

<div>

     Path \*p;

</div>

<div>

     for(v=0;v\<G.vexnum;++v)

</div>

<div>

     {

</div>

<div>

          final[v]=0;

</div>

<div>

          D[v]=G.arc[v0][v];

</div>

<div>

          P[v]=(Path\*)malloc(sizeof(Path));

</div>

<div>

          P[v]-\>next=NULL;

</div>

<div>

          p=(Path\*)malloc(sizeof(Path));

</div>

<div>

          p-\>adj=v0;

</div>

<div>

          p-\>next=NULL;

</div>

<div>

          P[v]-\>next=p;

</div>

<div>

     }

</div>

<div>

     D[v0]=0;

</div>

<div>

     final[v0]=1;

</div>

<div>

     for(int i=1;i\<G.vexnum;i++)

</div>

<div>

     {

</div>

<div>

          min=INT\_MAX;

</div>

<div>

          for(w=0;w\<G.vexnum;++w)

</div>

<div>

               if(!final[w])

</div>

<div>

                    if(D[w]\<min)

</div>

<div>

                    {

</div>

<div>

                         min=D[w];

</div>

<div>

                         v=w;

</div>

<div>

                    }

</div>

<div>

           if(isend==v)

</div>

<div>

                break;

</div>

<div>

          isend=v;

</div>

<div>

          final[v]=1;

</div>

<div>

          for(p=P[v]-\>next;p-\>next;p=p-\>next)

</div>

<div>

               printf("v%d",p-\>adj)

</div>

<div>

          printf("v%d",p-\>adj);

</div>

<div>

          Path \*p2;

</div>

<div>

          p2=(Path\*)malloc(sizeof(Path));

</div>

<div>

          p2-\>adj=v;

</div>

<div>

          p2-\>next=NULL;

</div>

<div>

          p-\>next=p2;

</div>

<div>

          printf("v%dn",v);

</div>

<div>

          for(w=0;w\<G.vexnum;++w)

</div>

<div>

             
 if(!final[w]&&G.arc[v][w]!=INT\_MAX&&(min+G.arc[v][w]\<D[w]))

</div>

<div>

               {

</div>

<div>

                    //printf("%d %d %d n",min,G.arc[v][w],D[w]);

</div>

<div>

                    D[w]=min+G.arc[v][w];

</div>

<div>

                    P[w]=P[v];

</div>

<div>

               }

</div>

<div>

     }

</div>

<div>

     return ;

</div>

<div>

}

</div>

<div>

int main()

</div>

<div>

{

</div>

<div>

     MGraph G;

</div>

<div>

     InitGraph(G);

</div>

<div>

     ShortestPath\_DIJ(G,0);

</div>

<div>

     getchar();

</div>

<div>

     return 0;

</div>

<div>

}

</div>

</div>

<div>

</div>

<div>

----------Output----------

</div>

<div>

<div>

v0v5

</div>

<div>

v0v3

</div>

<div>

v0v3v4

</div>

<div>

v0v3v4v2

</div>

<div>

算是打出正确结果了，改天再认真研究一下。

</div>

</div>
