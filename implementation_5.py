
from tkinter import *
from PIL import ImageTk,Image  
from tkinter import messagebox


# root - base frame
root = Tk()
root.wm_geometry("800x800")
root.config(background='lavender')
root.resizable(False,False)
root.title('Fianancial management App by Chris')

# name var
name_var = StringVar(root)
monthlyi_var = StringVar(root)
savings_var = StringVar(root)
monthlye_var= StringVar(root)
monthlyetype_var= StringVar(root)
dailye_var= StringVar(root)
goal_var= StringVar(root)
gnote_var= StringVar(root)

# a prompt for name input
name_prompt = "Please enter your name below"

# a prompt for income
monthlyi_prompt = "Please enter your monthly income"

# a promt for savings
savings_prompt = "Please enter your current amount saved"

#a prompt for expense
monthlye_prompt='Please enter your repetive monthly expense amount'

monthlyetype_prompt='Please enter the industry it was spent on'

dailye_prompt='Please enter your average daily expense amount'

#a prompt for goal
goal_prompt='Please enter your financial goal'
gnote_prompt='Please enter a note for your goal(optional)'
# widget to hold the name prompt
name_prompt_widget = Label(root,
            font = "Verdana 10 bold", 
            text=name_prompt)
# widget to hold the name prompt
monthlyi_prompt_widget = Label(root,
            font = "Verdana 9", 
       text=monthlyi_prompt)

# widget to hold the name prompt
savings_prompt_widget = Label(root,
            font = "Verdana 9 ", 
            text=savings_prompt)
#expense widget
monthlye_prompt_widget= Label(root,
        font='Verdana 9',
        text=monthlye_prompt)
monthlyetype_prompt_widget= Label(root,
        font='Verdana 9',
        text=monthlyetype_prompt)
dailye_prompt_widget= Label(root,
        font='Verdana 9',
        text=dailye_prompt)
goal_prompt_widget= Label(root,
        font='Verdana 9',
        text=goal_prompt)
gnote_prompt_widget= Label(root,
        font='Verdana 9',
        text=gnote_prompt)
msg = "Welcome {0}. Please provide the requested info below to get started!"\
        .format(name_var.get())

welcome_prompt_widget = Label(root,
        font = "Verdana 11 bold", 
        text=msg)




# widget to hold the logo
logo = ImageTk.PhotoImage(Image.open("final_logo.jpg"))  
logo_img = Label(root, image=logo)

name_input_widget = Entry(root, width=30, textvariable=name_var)
savings_input_widget = Entry(root, width=30, textvariable=savings_var)
monthlyi_input_widget = Entry(root, width=30, textvariable=monthlyi_var)
monthlye_input_widget = Entry(root, width=30, textvariable=monthlye_var)
monthlyetype_input_widget = Entry(root, width=30, textvariable=monthlyetype_var)
dailye_input_widget = Entry(root, width=30, textvariable=dailye_var)
goal_input_widget = Entry(root, width=30, textvariable=goal_var)
gnote_input_widget = Entry(root, width=30, textvariable=gnote_var)


#def load_results(
        #monthlyi_input_widget,
        #savings_input_widget,
        #dailye_input_widget,
        #monthlyi_input_widget
        #monthlye_input_widget,
        #monthlyetype_input_widget,
        #goal_input_widget,
        #gnote_input_widget,
        #back_name_enter_button,
        #last_page_button,
        #welcome_prompt_widget,
        #name_prompt_widget,
        #name_input_widget ):       
#need to vaidate
        #if savings_var.isnumeric:
                #import name_page
        #else:
         #    messagebox.showerror("Error", "Error message")   

 #       accept= False
 #       if len(savings_input_widget)>1:
  #              alphabet=True
   #             for i in range(0, len(savings_input_widget),1):
    #                    if not savings_input_widget.isalpha():
          #                      alphabet=False
     #                           break
       #         if alphabet== False:
        #                messagebox.showerror("Error", "Error message")
         #       else:
          #              accept=True
        #else:
         #       messagebox.showerror("Error", "Error message")
        text_file = open("output.txt", "w")
        text_file.write("Monthly Income Amount: %s" % monthlyi_var)
        text_file.write("Savings Amount: %s" % savings_input_widget)
        text_file.write("Monthly Expense Amount: %s" % monthlye_input_widget)
        text_file.write("Monthly Expense Type: %s" % monthlyetype_input_widget)
        text_file.write("Daily Expense Amount: %s" % dailye_input_widget)
        text_file.write("Goal Amount: %s" % goal_input_widget)
        text_file.write("Goal Note: %s" % gnote_input_widget)
        text_file.close()

        your_data = {"Purchase Amount": 'monthli_input_widget'}
        print(your_data,  file=open('D:\output.txt', 'w'))






        

def load_income_savings_widget():
        global monthlyi_prompt_widget
        global savings_prompt
        global welcome_prompt_widget
        global monthlye_prompt_widget
        global monthyetype_prompt_widget
        global dailye_rompt_widget
        global goal_prompt_widget
        global gnote_prompt_widget
        welcome_prompt_widget.pack(pady=15,             
            ipady = 5,
            ipadx = 5,
            after=logo_img, 
            anchor=N, )
        monthlyi_prompt_widget.pack(pady=5,             
            ipady = 2,
            ipadx = 5,
            after=welcome_prompt_widget, 
            anchor=N, )
        monthlyi_input_widget.pack()
        savings_prompt_widget.pack(pady=5,             
            ipady = 2,
            ipadx = 5,
            after=monthlyi_input_widget, 
            anchor=N, )
        savings_input_widget.pack()
        monthlye_prompt_widget.pack(pady=5,             
            ipady = 2,
            ipadx = 5,
            after=savings_input_widget, 
            anchor=N, )
        monthlye_input_widget.pack()
        monthlyetype_prompt_widget.pack(pady=5,             
            ipady = 2,
            ipadx = 5,
            after=monthlye_input_widget, 
            anchor=N, )
        monthlyetype_input_widget.pack()
        dailye_prompt_widget.pack(pady=5,             
            ipady = 2,
            ipadx = 5,
            after=monthlyetype_input_widget, 
            anchor=N, )
        dailye_input_widget.pack()
        goal_prompt_widget.pack(pady=5,             
            ipady = 2,
            ipadx = 5,
            after=dailye_input_widget, 
            anchor=N, )
        goal_input_widget.pack()
        gnote_prompt_widget.pack(pady=5,             
            ipady = 2,
            ipadx = 5,
            after=goal_input_widget, 
            anchor=N, )
        gnote_input_widget.pack()
        last_page_button.pack(anchor=SE)
        back_name_enter_button.pack(anchor=SW)

def load_input_widgets():
        global name_input_widget
        global name_enter_button
        global name_prompt_widget

        print(name_var.get())
        update_welcome_message(name_var.get())

        # clear screen and load next page
        name_input_widget.pack_forget()
        name_enter_button.pack_forget()
        name_prompt_widget.pack_forget()
        
        load_income_savings_widget()

def update_welcome_message(str1):
        global welcome_prompt_widget
        msg = "Welcome {0}. Please provide the requested info below to get started!"\
                .format(str1)

        welcome_prompt_widget = Label(root,
                font = "Verdana 11 bold", 
                text=msg)

def load_namep():
    monthlyi_input_widget.pack_forget()
    monthlyi_prompt_widget.pack_forget()
    savings_input_widget.pack_forget()
    savings_prompt_widget.pack_forget()
    back_name_enter_button.pack_forget()
    last_page_button.pack_forget()
    welcome_prompt_widget.pack_forget()
    name_prompt_widget.forget()
    name_input_widget.forget()
    monthlye_input_widget.pack_forget()
    monthlye_prompt_widget.pack_forget()
    monthlyetype_input_widget.pack_forget()
    monthlyetype_prompt_widget.pack_forget()
    dailye_input_widget.pack_forget()
    dailye_prompt_widget.pack_forget()
    goal_input_widget.pack_forget()
    goal_prompt_widget.pack_forget()
    gnote_input_widget.pack_forget()
    gnote_prompt_widget.pack_forget()

    name_prompt_widget.pack(pady=35,             
            ipady = 5,
            ipadx = 5,
            after=logo_img, 
            anchor=N, )

    name_input_widget.pack()
    name_enter_button.pack(pady=10,
                ipady = 10,
                ipadx = 10,
                after=name_input_widget, 
                anchor=N, )


name_enter_button = Button(root, text='Enter',font=' Verdana 10 bold',background='royal blue', foreground='white', command=load_input_widgets)
back_name_enter_button = Button(root, font="Verdana 10 bold", text='Back',background='royal blue', foreground='white', command=load_namep)
last_page_button = Button(root, font='Verdana 10 bold' ,text='Result',background='royal blue', foreground='white', command=load_results)


if __name__ == "__main__":

    logo_img.pack(anchor=N)
    load_namep()
    root.mainloop()

