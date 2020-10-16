from tkinter import *
from name_page import *
#import matplotlib.pyplot as plt
#import numpy as np

root=Tk()
root.geometry("500x500")
root.config(background='lavender')
root.resizable(False,False)
top1=Label(root, text='Fianancial management App',background='light sea green').place(x=166,y=10)
top2=Label(root, text='This is your graph estimate till you reach goal if your consisent',background='white').place(x=90,y=90)

#input graph from matplotlib
#
#x = np.linspace(0, 2 * np.pi, 20)
#y = np.sin(x)
#yp = None
#xi = np.linspace(x[0], x[-1], 100)
#yi = np.interp(xi, x, y, yp)

#fig, ax = plt.subplots()
#ax.plot(x, y, 'o', xi, yi, '.')
#plt.show()
