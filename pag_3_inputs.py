from tkinter import *
from GUIT import *
def graph():
    import graph_page
def input_page():
    import inputs_page
root=Tk()
root.geometry("500x500")
root.config(background='lavender')
root.resizable(False,False)
top1=Label(root, text='Fianancial management App',background='light sea green').place(x=166,y=10)
top2=Label(root, text='Hi '+(GUIT.name)+ ', please pick one of the options below ',background='white').place(x=130,y=90)

Inputsb=Button(root, text='Inputs',height=5, width=10,background='light sea green', command=input_page).place(x=50, y=200)
graphb=Button(root, text='Graph',height=5, width=10,background='light sea green', command=graph).place(x=350, y=200)
























root.mainloop()

