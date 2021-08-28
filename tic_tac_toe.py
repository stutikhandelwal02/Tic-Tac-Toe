from tkinter import *
import tkinter.messagebox
root=Tk()
root.title('Game time')
root.configure(bg='black')
winc=[{0,3,6},{1,4,7},{2,5,8},{8,4,0},{2,4,6},{0,1,2},{4,5,3},{6,7,8}]


def win():
    global winc
    global l1
    global l2
    
    for i in winc:
        if i.issubset(l1):
            tkinter.messagebox.showinfo("Result" ,'Player 1 win')
            label1.destroy()
            label2.destroy()
            Reset()
        elif i.issubset(l2):
            tkinter.messagebox.showinfo("Result" ,'Player 2 win')
            label1.destroy()
            label2.destroy()
            Reset()
        elif count==9:
            tkinter.messagebox.showinfo("Result" ,'Draw')
            label1.destroy()
            label2.destroy()
            Reset()
          
    
        
def Active():
    for b in lb:
        b['state']='active'
    s['state']='disable'
    s['text']='Start'
    global label1
    label1=Label(root,text='Player 1',bg='red',fg='yellow',width=5,height=2,font='magneto 14 bold',)
    label1.grid(row=4,column=0,padx=1,pady=1,sticky='nswe')

    
def pf1(t):
    global turn
    global l1
    global count
    global label1
    global label2
    label1.destroy()
    label2=Label(root,text='Player 2',bg='red',fg='yellow',width=5,height=2,font='magneto 14 bold',)
    label2.grid(row=4,column=2,padx=1,pady=1,sticky='nswe')
    turn=False
    count=count+1
    l1.append(t[0]*3+t[1])
    b=lb[t[0]*3+t[1]]
    b['bg']='light green'
    b['text']='0'
    b['state']='disable'
    if count>=5:
        win()
    
    
def pf2(t):
    global turn
    global l2
    global count
    count=count+1
    global label1
    global label2
    turn=True
    label2.destroy()
    label1=Label(root,text='Player 1',bg='red',fg='yellow',width=5,height=2,font='magneto 14 bold',)
    label1.grid(row=4,column=0,padx=1,pady=1,sticky='nswe')
    l2.append(t[0]*3+t[1])
    b=lb[t[0]*3+t[1]]
    b['bg']='sky blue'
    b['text']='X'
    b['state']='disable'
    if count>=5:
        win()
    
    

    
Label(root,text='TIC-TAC-TOE',font='Times 14 italic',bg='yellow').grid(row=0,column=1)
def Reset():
    global lb
    global s
    global l1
    global l2
    global count
    global turn
    l2=[]
    l1=[]
    count=0
    lb=[]
    turn=True
    for i in range(3):
        for j in range(3):
            lb.append(Button(root,state='disable',width=5,height=2,
                             bg='orange',font='times 50 italic',
                             relief=RAISED,command=lambda t=(i,j):pf1(t)
                             if turn==True else pf2(t)))
            lb[-1].grid(row=i+1,column=j,sticky='nswe')
    s=Button(root,text='Start',bg='red',fg='yellow',width=5,height=2,command=Active,font='times 14 bold',)
    s.grid(row=4,column=1,padx=1,pady=1,sticky='nswe')
Reset()

for i in range(5):
    root.grid_rowconfigure(i,weight=1)
for i in range(3):
    root.grid_columnconfigure(i,weight=1)
        
root.mainloop()
