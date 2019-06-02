from tkinter import *
import math

def alpha(c1,c2):
    return abs(ord(c1)-ord(c2))
def edit_dp(st1,st2,xlow,ylow,xhigh,yhigh,delta,reverse):
    m=xhigh-xlow
    n=yhigh-ylow
    dist=[0]*(m+1)
    dp=[[0 for i in range(n+1)] for i in range(m+1)]
    if reverse==False:
        dp[0][0]=0
        for i in range(1,n+1):
            dp[0][i]=dp[0][i-1]+delta
        for i in range(1,m+1):
            dp[i][0]=dp[i-1][0]+delta
            for j in range(1,n+1):
                dp[i][j]=dp[i-1][j-1]+alpha(st1[xlow+i-1],st2[ylow+j-1])
                dp[i][j]=min(dp[i][j],dp[i-1][j]+delta)
                dp[i][j]=min(dp[i][j],dp[i][j-1]+delta)
        for i in range(m+1):
            dist[i]=dp[i][n]
    if reverse==True:
        dp[m][n]=0
        for j in range(n-1,-1,-1):
            dp[m][j]=dp[m][j+1]+delta
        for i in range(m-1,-1,-1):
            dp[i][n]=dp[i+1][n]+delta
            for j in range(n-1,-1,-1):
                dp[i][j]=dp[i+1][j+1]+alpha(st1[xlow+i],st2[ylow+j])
                dp[i][j]=min(dp[i][j],dp[i+1][j]+delta)
                dp[i][j]=min(dp[i][j],dp[i][j+1]+delta)
        for i in range(m+1):
            dist[i]=dp[m-i][0]  
    return dist 
def edit_dc(st1,st2,xlow,ylow,xhigh,yhigh,delta,point):
    if yhigh-ylow<=1:
        dist=edit_dp(st1,st2,xlow,ylow,xhigh,yhigh,delta,False)
        qmin=xlow
        Min=dist[0]+(xhigh-xlow)*delta
        for i in range(1,xhigh-xlow+1):
            tmp=dist[i]+(xhigh-xlow-i)*delta
            if tmp<Min:
                qmin=xlow+i
                Min=tmp
        if qmin==xlow:
            point[xlow][ylow]=1
        elif (qmin-xlow-1)*delta+alpha(st1[qmin-1],st2[yhigh-1])<=((qmin - xlow) * delta + delta):
            for i in range(xlow,qmin):
                point[i][ylow]=1
        else:
            for i in range(xlow,qmin+1):
                point[i][ylow]=1
        for i in range(qmin,xhigh+1):
            point[i][yhigh]=1
        return Min
    ymid=(ylow+yhigh)//2
    dist1=edit_dp(st1,st2,xlow,ylow,xhigh,yhigh,delta,False)
    dist2=edit_dp(st1,st2,xlow,ylow,xhigh,yhigh,delta,True)
    qmin=xlow
    Min=dist1[0]+dist2[xhigh-xlow]
    for i in range(1,xhigh-xlow+1):
        tmp=dist1[i]+dist2[xhigh-xlow-i]
        if tmp<Min:
            qmin=xlow+i
            Min=tmp
    point[qmin][ymid]=1
    return edit_dc(st1,st2,xlow,ylow,qmin,ymid,delta,point)+edit_dc(st1,st2,qmin,ymid,xhigh,yhigh,delta,point)
def edit_dcdp(st1,st2,delta,point):
    return edit_dc(st1,st2,0,0,len(st1),len(st2),delta,point)
if __name__ == "__main__":
    delta=13
    print('Please input two strings:')
    str1=str(input())
    str2=str(input())
    len1=len(str1)
    len2=len(str2)
    point=[[0 for i in range(len(str2)+1)]for i in range(len(str1)+1)]
    answer=edit_dcdp(str1,str2,delta,point)
    root=Tk()
    root.title('shortest eidt ditance: %d'%answer)
    cvs=Canvas(root,bg='white',width=800,height=800)
    colunm=700/(len1+1)
    raw=700/(len2+1)
    print(point)
    for i in range(len2+2):
        cvs.create_line(50+i*raw,50,50+i*raw,750)
        if i<=len2 and i>0:
            cvs.create_text(50+i*raw+colunm/3,50-raw/3,text=str2[i-1])
    for i in range(len1+2):
        cvs.create_line(50,i*colunm+50,750,i*colunm+50)
        if i<=len1 and i>0:
            cvs.create_text(50-colunm/3,i*colunm+50+raw/4,text=str1[i-1])
    for i in range(len2+1):
        for j in range(len1+1):
            if point[j][i]==1:
                cvs.create_rectangle(50+i*raw,50+j*colunm,50+(i+1)*raw,50+(j+1)*colunm,fill='red')
    cvs.pack()
    root.mainloop()