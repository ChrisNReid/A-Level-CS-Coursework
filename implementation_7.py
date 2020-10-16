
from tkinter import *
from PIL import ImageTk,Image  
from tkinter import messagebox
import matplotlib

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
# trying to add a a seperate background for the area with the logo
#f1=Frame(root,width=800,height=100,bg= 'blue')
#f1.pack()
logo = ImageTk.PhotoImage(Image.open("final_logo.jpg"))  
logo_img = Label(root, image=logo)

countdownB=Button(root, text='Countdown',font='Verdana 10 bold', bg='royal blue',fg='white')
graphB=Button(root, text='graph',font='Verdana 10 bold', bg='royal blue', fg='white',command=graph)

name_input_widget = Entry(root, width=30, textvariable=name_var)
savings_input_widget = Entry(root, width=30, textvariable=savings_var)
monthlyi_input_widget = Entry(root, width=30, textvariable=monthlyi_var)
monthlye_input_widget = Entry(root, width=30, textvariable=monthlye_var)
monthlyetype_input_widget = Entry(root, width=30, textvariable=monthlyetype_var)
dailye_input_widget = Entry(root, width=30, textvariable=dailye_var)
goal_input_widget = Entry(root, width=30, textvariable=goal_var)
gnote_input_widget = Entry(root, width=30, textvariable=gnote_var)
       
def graph():
        labels = 'Income', 'Monthly expense', 'Daily Expense'
        sizes = [monthlyi_var, monthlye_var, dailye_var]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
        plt.axis('equal')
        plt.show()    


        
def selection():

        global name_prompt_widget 
        global savings_prompt_widget 
        global monthlyi_prompt_widget
        global monthlye_prompt_widget 
        global monthlyetype_prompt_widget 
        global dailye_prompt_widget 
        global goal_prompt_widget 
        global gnote_prompt_widget
        
        global name_input_widget 
        global savings_input_widget 
        global monthlyi_input_widget
        global monthlye_input_widget 
        global monthlyetype_input_widget 
        global dailye_input_widget 
        global goal_input_widget 
        global gnote_input_widget
        global back_name_enter_button
        global countdownB
        global graphB
        name_prompt_widget.forget() 
        savings_prompt_widget.forget()
        monthlyi_prompt_widget.forget()
        monthlye_prompt_widget.forget()
        monthlyetype_prompt_widget.forget() 
        dailye_prompt_widget.forget()
        goal_prompt_widget.forget() 
        gnote_prompt_widget.forget()
        
        name_input_widget.forget() 
        savings_input_widget.forget()
        monthlyi_input_widget.forget()
        monthlye_input_widget.forget() 
        monthlyetype_input_widget.forget() 
        dailye_input_widget.forget() 
        goal_input_widget.forget() 
        gnote_input_widget.forget()
        last_page_button.forget()
        
        
        back_name_enter_button['command']=load_income_savings_widget
        countdownB['command']=count
        countdownB.pack(pady=10,
                ipady = 10,
                ipadx = 10, 
                anchor=N, )

        graphB.pack(pady=10,
                ipady = 10,
                ipadx = 10,
                after=countdownB, 
                anchor=N, )
        #countdownB.pack()
        #graphB.pack()

def selection1():

        global name_prompt_widget 
        global savings_prompt_widget 
        global monthlyi_prompt_widget
        global monthlye_prompt_widget 
        global monthlyetype_prompt_widget 
        global dailye_prompt_widget 
        global goal_prompt_widget 
        global gnote_prompt_widget
        
        global name_input_widget 
        global savings_input_widget 
        global monthlyi_input_widget
        global monthlye_input_widget 
        global monthlyetype_input_widget 
        global dailye_input_widget 
        global goal_input_widget 
        global gnote_input_widget
        global back_name_enter_button
        global countdownB
        global graphB
        name_prompt_widget.forget() 
        savings_prompt_widget.forget()
        monthlyi_prompt_widget.forget()
        monthlye_prompt_widget.forget()
        monthlyetype_prompt_widget.forget() 
        dailye_prompt_widget.forget()
        goal_prompt_widget.forget() 
        gnote_prompt_widget.forget()
        
        name_input_widget.forget() 
        savings_input_widget.forget()
        monthlyi_input_widget.forget()
        monthlye_input_widget.forget() 
        monthlyetype_input_widget.forget() 
        dailye_input_widget.forget() 
        goal_input_widget.forget() 
        gnote_input_widget.forget()
        last_page_button.forget()
        
        
        back_name_enter_button['command']=load_income_savings_widget
        countdownB['command']=count
        countdownB.pack()
        graphB.pack()

def count():
        
        global savings_var
        global monthlyi_var
        global monthlye_var
        global monthlyetype_var
        global dailye_var
        global goal_var
        global gnote_var
        global back_name_enter_button
        
        last_page_button.forget()
        
        savings_var.get()
        monthlyi_var.get()
        monthlye_var.get()
        monthlyetype_var.get()
        dailye_var.get()
        goal_var.get()
        gnote_var.get()

        int_savings_var=float(savings_var.get())
        int_monthlyi_var=float(savings_var.get())
        int_monthlye_var=float(savings_var.get())
        int_dailye_var=float(savings_var.get())
        int_goal_var=float(savings_var.get())
        
        back_name_enter_button['command']=selection

        monthly_expense_t=(int_dailye_var*30)+int_monthlye_var
        monthly_net=int_monthlyi_var-monthly_expense_t
        goal_final=int_goal_var - int_savings_var
        eta=goal_final/monthly_net
        print(eta)
        etag=eta*60*60*24*30.4
        etag2=int(round(float(etag)))
        print(etag)
        print(etag2)



def load_results():

        global name_prompt_widget 
        global savings_prompt_widget 
        global monthlyi_prompt_widget
        global monthlye_prompt_widget 
        global monthlyetype_prompt_widget 
        global dailye_prompt_widget 
        global goal_prompt_widget 
        global gnote_prompt_widget
#I have been strugging with the passing of variables and creating new windows with this
        

#trying# to vaidate the entries and produce a message box error
        #if str(savings_var.get()).isdigit() and str(savings_var.get()) !='':
           #     import selection
       # else:
              #     


 #       accept= False
#
#
 #       if len(savings_input_widget)>1:
  #              alphabet=True
   #             for i in range(0, len(savings_input_widget),1):
    #                    if not savings_input_widget.isalpha():
          #                      alphabet=False
     #                           break
      #          
       #         if alphabet== False:
        #                messagebox.showerror("Error", "Error message")
         #       else:
          #              accept=True

        #else:
         #       messagebox.showerror("Error", "Error message")



# trying to get it to print on a text document and or database system
        text_file = open("output.txt", "a")
        str1 = "Monthly Income Amount: "
        str2='Savings Amount: '
        str3="Monthly Expense Amount: "
        str4='Monthly Expense Type: '
        str5="Daily Expense Amount: "
        str6="Goal Amount: "
        str7="Goal Note: "
        header = "{0:30},{1:30},{2:30},{3:30},{4:30},{5:30},{6:30}"\
                .format(str1, str2, str3, str4, str5, str6, str7)
        # text_file.write(header+'\n')
        str1 = str(monthlyi_var.get())
        str2=str(savings_var.get())
        str3=str(monthlye_var.get())
        str4=str(monthlyetype_var.get())
        str5=str(dailye_var.get())
        str6=str(goal_var.get())
        str7=str(gnote_var.get())
        header = "{0:30},{1:30},{2:30},{3:30},{4:30},{5:30},{6:30}"\
                .format(str1, str2, str3, str4, str5, str6, str7)
        text_file.write(header+'\n')
        # text_file.write("Monthly Income Amount: %s" % monthlyi_var.get())
        # text_file.write("Savings Amount: %s" % savings_var.get())
        # text_file.write("Monthly Expense Amount: %s" % monthlye_var.get())
        # text_file.write("Monthly Expense Type: %s" % monthlyetype_var.get())
        # text_file.write("Daily Expense Amount: %s" % dailye_var.get())
        # text_file.write("Goal Amount: %s" % goal_var.get())
        # text_file.write("Goal Note: %s" % gnote_var.get())
        text_file.close()

        # your_data = {"money Amount": 'monthli_'}
        # print(your_data,  file=open('.\output.txt', 'w'))

        selection()



        

def load_income_savings_widget():
        global monthlyi_prompt_widget
        global savings_prompt
        global welcome_prompt_widget
        global monthlye_prompt_widget
        global monthyetype_prompt_widget
        global dailye_rompt_widget
        global goal_prompt_widget
        global gnote_prompt_widget
        countdownB.forget()
        graphB.forget()

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

