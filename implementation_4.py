from tkinter import *
from PIL import ImageTk,Image  



# root - base frame
root = Tk()
root.wm_geometry("800x600")
root.config(background='lavender')
root.resizable(False,False)
root.title('Fianancial management App by Chris')

# name var
name_var = StringVar(root)


# a prompt for name input
name_prompt = "Please enter your name below"

# widget to hold the name prompt
name_prompt_widget = Label(root,
            font = "Verdana 12 bold", 
            text=name_prompt)

# widget to hold the logo
logo = ImageTk.PhotoImage(Image.open("final_logo.jpg"))  
logo_img = Label(root, image=logo)

name_input_widget = Entry(root, width=30, textvariable=name_var)


def load_input_widgets():
        global name_input_widget
        global name_enter_button
        global name_prompt_widget


        # clear screen and load next page
        name_input_widget.pack_forget()
        name_enter_button.pack_forget()
        name_prompt_widget.pack_forget()
        

name_enter_button = Button(root, text='Enter', command=load_input_widgets)

if __name__ == "__main__":

    logo_img.pack(anchor=N)

    name_prompt_widget.pack(pady=35,             
            ipady = 5,
            ipadx = 5,
            after=logo_img, 
            anchor=N, )

    name_input_widget.pack()
    name_enter_button.pack()

    root.mainloop()

