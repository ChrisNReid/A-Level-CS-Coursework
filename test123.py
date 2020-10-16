from tkinter import *
import time 
def countDown():
    '''start countdown 10 seconds before new year starts'''
    lbl1.config(bg='white')
    lbl1.config(height=3, font=('times', 20, 'bold'))
    for k in range(10, 0, -1):
        lbl1["text"] = k
        root.update()
        time.sleep(1)
    lbl1.config(bg='red')
    lbl1.config(fg='white')
    lbl1["text"] = "Goal reached!"
    
root = Tk()
root.title("Countdown")
lbl1 = Label()
lbl1.pack(fill=BOTH, expand=1)
countDown()
root.mainloop()
