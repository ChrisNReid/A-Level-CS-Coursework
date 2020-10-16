


from tkinter import *
#from name_page import name
root=Tk()
root.geometry("600x600")
root.config(background='lavender')
root.resizable(False,False)
#img = ImageTk.PhotoImage(Image.open("final_logo"))
#panel = Label(root, image = img)


top1=Label(root, text='Fianancial management App',background='light sea green').place(x=166,y=10)

def back():
    root.destroy()
    import name_page
    
def callback_func():
    initial_savings = entry1.get()
    monthi = entry2.get()
    monthe = entry3.get()
    ind_type = entry3.get()
    dailye = entry5.get()
    goal = entry6.get()
    gnote = entry7.get()
    print(initial_savings)
    print(monthi)
    print(monthe)
    print(ind_type)
    print(dailye)
    print(goal)
    print(g_note)
    
#need validation


#initial savings
i_label=Label(root, text='Enter your initial savings').place(x=20, y=90)
entry1=Entry(root, width=20).place(x=50,y=90)
entry1.pack()
entry1.focus_set()
entry1.place(x=200, y=90)

#monthly income
label=Label(root, text='Enter your monthly income').place(x=20, y=140)
entry2=Entry(root, width=20).place(x=50,y=140)
entry2.pack()
entry2.focus_set()
entry2.place(x=200, y=140)

#monhly repeptive expense
me_label=Label(root, text='Enter your repetitive monthly expense').place(x=20, y=190)
entry3=Entry(root, width=20).place(x=50,y=190)
entry3.pack()
entry3.focus_set()
entry3.place(x=200, y=190)

#insustry sector
ind_label=Label(root, text='what industry sector was its spent on (food/travel/fun)?').place(x=20, y=240)
entry4=Entry(root, width=20).place(x=50,y=240)
entry4.pack()
entry4.focus_set()
entry4.place(x=200, y=240)

#daily expense
m_label=Label(root, text='Enter your daily expense').place(x=20, y=290)
entry5=Entry(root, width=20).place(x=50,y=290)
entry5.pack()
entry5.focus_set()
entry5.place(x=200, y=290)

#goal amount
g_label=Label(root, text='Enter your daily expense').place(x=20, y=340)
entry6=Entry(root, width=20).place(x=50,y=340)
entry6.pack()
entry6.focus_set()
entry6.place(x=200, y=340)

#goal note
g_n_label=Label(root, text='Enter your daily expense').place(x=20, y=390)
entry7=Entry(root, width=20).place(x=50,y=390)
entry7.pack()
entry7.focus_set()
entry7.place(x=200, y=390)



button=Button(root, text='submit', command=callback_func).place(x=250,y=400)

buttonback=Button(root, text='Back', command=back).place(x=50,y=450)
