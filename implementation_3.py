from tkinter import *
from PIL import ImageTk,Image  

# root - base frame
root = Tk()
root.wm_geometry("800x600")
root.config(background='lavender')
root.resizable(False,False)
root.title('Fianancial management App by Chris')


# a prompt for name input
name_prompt = "Please enter your name below"

# widget to hold the name prompt
name_prompt_widget = Label(root,
            font = "Verdana 12 bold", 
            text=name_prompt)

# widget to hold the logo
logo = ImageTk.PhotoImage(Image.open("final_logo.jpg"))  
logo_img = Label(root, image=logo)


if __name__ == "__main__":

    logo_img.pack(anchor=N)

    name_prompt_widget.pack(pady=35,             
            ipady = 5,
            ipadx = 5,
            after=logo_img, 
            anchor=N, )

    root.mainloop()

