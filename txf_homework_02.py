from tkinter import *

if __name__ == "__main__":
    n = eval(input('please input the number k: '))
    root=Tk()
    root.title('Sorting Network with n=%d (Drawn by Python Tkinter)' % n)
    cvs=Canvas(root,bg='white',width=1200,height=700)
    for i in range(n):
        cvs.create_line(50,50+i*600/(n-1),1200,50+i*600/(n-1))
    for i in range(n-1):
        for j in range(i,n-1):
            cvs.create_oval(100-3+j*1000/(n-1)-i*500/(n-1),50+i*600/(n-1)-3,100+3+j*1000/(n-1)-i*500/(n-1),50+i*600/(n-1)+3,fill='black')
            cvs.create_oval(100-3+j*1000/(n-1)-i*500/(n-1),50+(i+1)*600/(n-1)-3,100+3+j*1000/(n-1)-i*500/(n-1),50+(i+1)*600/(n-1)+3,fill='black')
            cvs.create_line(100+j*1000/(n-1)-i*500/(n-1),50+i*600/(n-1),100+j*1000/(n-1)-i*500/(n-1),50+(i+1)*600/(n-1))
    cvs.pack()
    root.mainloop()