from tkinter import *
#from name_page import name
root=Tk()
root.geometry("500x500")
root.config(background='lavender')
root.resizable(False,False)
top1=Label(root, text='Fianancial management App',background='light sea green').place(x=166,y=10)

def callback_func():
    initial_savings = entry1.get()
    monthi = entry2.get()
    dailye = entry3.get()

#initial savings
i_label=Label(root, text='Enter your initial savings').place(x=20, y=90)
entry1=Entry(root, width=20).place(x=200, y=90)

#monthly income
label=Label(root, text='Enter your monthly income').place(x=20, y=140)
entry2=Entry(root, width=20).place( x=200, y=140)

#daily expense
m_label=Label(root, text='Enter your daily expense').place(x=20, y=190)
entry3=Entry(root, width=20).place(x=200, y=190)

button=Button(root, text='submit', command=callback_func).place(x=20,y= 250)
