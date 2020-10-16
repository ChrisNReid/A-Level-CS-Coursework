from tkinter import *
root=Tk()
root.geometry("500x500")
root.config(background='lavender')
root.resizable(False,False)
top1=Label(root, text='Fianancial management App',background='light sea green').place(x=166,y=10)

Incomeb=Button(root, text='Income',height=5, width=10,background='light sea green').place(x=50, y=200)
Expenseb=Button(root, text='Expenses',height=5, width=10,background='light sea green').place(x=200, y=200)
graphb=Button(root, text='Graph',height=5, width=10,background='light sea green').place(x=350, y=200)
























root.mainloop()
