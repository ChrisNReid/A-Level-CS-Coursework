from tkinter import *
root=Tk()

top1=Label(root, text='Fianancial management App').grid(row=0,column=0)

#initial savings
i_label=Label(root, text='Enter your initial savings').grid(row=1,column=0)
initial_savings=Entry(root, width=50).grid(row=1, column=1)

#monthly income
label=Label(root, text='Enter your monthly income').grid(row=2,column=0)
monthyi=Entry(root, width=50).grid(row=2, column=1)

#daily expense
m_label=Label(root, text='Enter your daily expense').grid(row=3,column=0)
daily_expense=Entry(root, width=50).grid(row=3, column=1)


button=Button(root, text='submit').grid(row=4, column=0)


root.mainloop()
