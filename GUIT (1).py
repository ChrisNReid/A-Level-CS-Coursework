

from tkinter import *
name = ""

def page3():
    global name
    name = entry.get() 
    root.destroy()
    import select_page


    
root=Tk()
root.geometry("500x500")

root.config(background='lavender')
root.resizable(False,False)
top1=Label(root, text='Fianancial management App',background='light sea green').place(x=166,y=10)
name_label=Label(root, text='Please enter your name:').place(x=20, y=50)
entry=Entry(root, width=30) # , place(x=150, y=50)
entry.pack()
entry.focus_set()
name_enterb=Button(root, text='Enter',command=page3).place(x=330, y=50)
#name_enterb.pack()

#label=Label(root, text='Welcome '+ name + ' to my Fianancial management App').place(x=20,y=170)

#label2=Label(root, text= 'Click the button to be directed to your inputs').place(x=20, y=210)
#homepage_button=Button(root, text='Inputs').place(x=20, y=250)

#top1=label(root, text='Fianancial management App').grid(row=0,column=0)

#initial savings
#i_label=Label(root, text='Enter your initial savings').grid(row=1,column=0)
#initial_savings=Entry(root, width=50).grid(row=1, column=1)

#monthly income
#label=Label(root, text='Enter your monthly income').grid(row=2,column=0)
#monthyi=Entry(root, width=50).grid(row=2, column=1)

#daily expense
#m_label=Label(root, text='Enter your daily expense').grid(row=3,column=0)
#daily_expense=Entry(root, width=50).grid(row=3, column=1)

root.mainloop()
