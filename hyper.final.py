from tkinter import *
import webbrowser

def callback(event):
    webbrowser.open_new(r"https://www.thebalance.com/the-50-30-20-rule-of-thumb-453922")

root = Tk()
link = Label(root, text='Try to restrict your expeneses and follow the 50/30/20 rule', fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", callback)
root.mainloop()
