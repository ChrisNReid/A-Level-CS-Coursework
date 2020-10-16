from tkinter import *
from PIL import ImageTk,Image  


if __name__ == "__main__":
    root = Tk()
    root.wm_geometry("800x600")
    root.config(background='lavender')
    root.resizable(False,False)
    root.title('Fianancial management App by Chris')

    logo = ImageTk.PhotoImage(Image.open("final_logo.jpg"))  
    logo_img = Label(root, image=logo)
    logo_img.pack(pady=10, anchor=N)

    root.mainloop()

