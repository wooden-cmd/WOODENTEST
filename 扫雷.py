from tkinter import *
from random import *



root=Tk()
root.geometry("560x510")
root.title('扫雷')
root["background"]='#ffffff'

font=('宋体',20)
lis=[]
buttonlist=[]
row=10
column=10

for y in range(row):
    for x in range(column):
        buttonlist.append('buttom'+str(x)+str(y))
for y in range(row):
    linex=[]
    for x in range(column):
        test=randint(0,3)
        if test==0:
            linex.append('boom')
        else:
           linex.append(0)
    lis.append(linex)
def creatnum():
    for y in range(row):
        for x in range(column):
            up=y-1
            down=y+1
            left=x-1
            right=x+1
            if lis[x][y] !='boom':
                if up>=0:
                    if lis[x][up]=='boom':
                        lis[x][y]+=1
                if down<=row-1:
                    if lis[x][down]=='boom':
                        lis[x][y]+=1
                if left>=0:
                    if lis[left][y]=='boom':
                        lis[x][y]+=1
                if right<=column-1:
                    if lis[right][y]=='boom':
                        lis[x][y]+=1
                if up>=0 and left>=0:
                    if lis[left][up]=='boom':
                        lis[x][y]+=1
                if up>=0 and right<=column-1:
                    if lis[right][up]=='boom':
                        lis[x][y]+=1
                if down<=row-1 and left>=0:
                    if lis[left][down]=='boom':
                        lis[x][y]+=1
                if down<=row-1 and right<=column-1:
                    if lis[right][down]=='boom':
                        lis[x][y]+=1
def click(clickx,clicky):
    if lis[clickx][clicky]=='boom':
        print('你输了')
    elif lis[clickx][clicky]==0:
        button.config(bg='#ffffff')
    else :
        button.config(bg='#ffffff',text=lis[clickx][clicky])
        
        
creatnum()
for y in range(row):
    for x in range(column):
        buttonlist[x][y]=Button(root,width=3,font=font,relief=FLAT,bg='#b1b2b2',command=lambda:click(x,y)).grid(row=x,column=y,padx=2,pady=2)
    lis.append(linex)

                


    
