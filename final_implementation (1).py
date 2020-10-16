from tkinter import *
from PIL import ImageTk,Image  
from tkinter import messagebox
import matplotlib.pyplot as plt

# root - base frame
root = Tk()

class FinanceApp():
    def __init__(self, root):
        self.root = root
    
    def prepare_app_vars(self):
        self.root.wm_geometry("800x800")
        self.root.config(background='lavender')
        self.root.resizable(False,False)
        self.root.title('Fianancial management App by Chris')

        # name var
        self.name_var = StringVar(self.root)
        self.monthlyi_var = StringVar(self.root)
        self.savings_var = StringVar(self.root)
        self.monthlye_var = StringVar(self.root)
        self.monthlyetype_var = StringVar(self.root)
        self.dailye_var = StringVar(self.root)
        self.goal_var = StringVar(self.root)
        self.gnote_var = StringVar(self.root)

    def prepare_app_prompts(self):
        # a prompt for name input
        self.name_prompt = "Please enter your name below"

        # a prompt for income
        self.monthlyi_prompt = "Please enter your monthly income"

        # a promt for savings
        self.savings_prompt = "Please enter your current amount saved"

        #a prompt for expense
        self.monthlye_prompt='Please enter your repetive monthly expense amount'
        self.monthlyetype_prompt='Please enter the industry it was spent on'
        self.dailye_prompt='Please enter your average daily expense amount'
        
        #a prompt for goal
        self.goal_prompt ='Please enter your financial goal'
        self.gnote_prompt ='Please enter a note for your goal(optional)'

    def prepare_app_widgets(self):
        # widget to hold the name prompt
        self.name_prompt_widget = Label(self.root,
                    font = "Verdana 10 bold", 
                    text=self.name_prompt)

        # widget to hold the name prompt
        self.monthlyi_prompt_widget = Label(self.root,
                    font = "Verdana 9", 
                    text=self.monthlyi_prompt)

        # widget to hold the name prompt
        self.savings_prompt_widget = Label(self.root,
                    font = "Verdana 9 ", 
                    text=self.savings_prompt)

        #expense widget
        self.monthlye_prompt_widget= Label(self.root,
                font='Verdana 9',
                text=self.monthlye_prompt)

        self.monthlyetype_prompt_widget= Label(self.root,
                font='Verdana 9',
                text=self.monthlyetype_prompt)

        self.dailye_prompt_widget= Label(self.root,
                font='Verdana 9',
                text=self.dailye_prompt)

        self.goal_prompt_widget= Label(self.root,
                font='Verdana 9',
                text=self.goal_prompt)

        self.gnote_prompt_widget= Label(self.root,
                font='Verdana 9',
                text=self.gnote_prompt)
                

        msg = "Welcome {0}. Please provide the requested info below to get started!"\
                .format(self.name_var.get())

        self.welcome_prompt_widget = Label(self.root,
                font = "Verdana 11 bold", 
                text=msg)

    def prepare_logo_and_buttons(self):
        self.logo = ImageTk.PhotoImage(Image.open("final_logo.jpg"))  
        self.logo_img = Label(self.root, image=self.logo)
        self.countdownB=Button(self.root, text='Countdown', font=' Verdana 10 bold',background='royal blue', foreground='white', anchor=W)
        self.graphB=Button(self.root, text='graph',font=' Verdana 10 bold',background='royal blue', foreground='white', anchor=E)
        self.name_enter_button = Button(root, text='Enter',font=' Verdana 10 bold',background='royal blue', foreground='white', command=self.load_input_widgets)
        self.back_name_enter_button = Button(root, font="Verdana 10 bold", text='Back',background='royal blue', foreground='white', command=self.load_namep)
        self.last_page_button = Button(root, font='Verdana 10 bold' ,text='Submit',background='royal blue', foreground='white', command=self.load_results)

    def bind_widgets_to_vars(self):
        self.name_input_widget = Entry(root, width=30, textvariable=self.name_var)
        self.savings_input_widget = Entry(root, width=30, textvariable=self.savings_var)
        self.monthlyi_input_widget = Entry(root, width=30, textvariable=self.monthlyi_var)
        self.monthlye_input_widget = Entry(root, width=30, textvariable=self.monthlye_var)
        self.monthlyetype_input_widget = Entry(root, width=30, textvariable=self.monthlyetype_var)
        self.dailye_input_widget = Entry(root, width=30, textvariable=self.dailye_var)
        self.goal_input_widget = Entry(root, width=30, textvariable=self.goal_var)
        self.gnote_input_widget = Entry(root, width=30, textvariable=self.gnote_var)

    def launch_app(self):
        self.prepare_app_vars()
        self.prepare_app_prompts()
        self.prepare_app_widgets()
        self.prepare_logo_and_buttons()
        self.bind_widgets_to_vars()

        self.logo_img.pack(anchor=N)
        self.load_namep()
        self.root.mainloop()

    def selection(self):
        self.name_prompt_widget.forget() 
        self.savings_prompt_widget.forget()
        self.monthlyi_prompt_widget.forget()
        self.monthlye_prompt_widget.forget()
        self.monthlyetype_prompt_widget.forget() 
        self.dailye_prompt_widget.forget()
        self.goal_prompt_widget.forget() 
        self.gnote_prompt_widget.forget()
        
        self.name_input_widget.forget() 
        self.savings_input_widget.forget()
        self.monthlyi_input_widget.forget()
        self.monthlye_input_widget.forget() 
        self.monthlyetype_input_widget.forget() 
        self.dailye_input_widget.forget() 
        self.goal_input_widget.forget() 
        self.gnote_input_widget.forget()
        self.last_page_button.forget()
        #
        if str(self.monthlyi_var.get()).isalpha():
            messagebox.showerror("Error", "Please enter numerical values")
        elif str(self.monthlye_var.get()).isalpha():
            messagebox.showerror("Error", "Please enter numerical values")
        elif str(self.savings_var.get()).isalpha():
            messagebox.showerror("Error", "Please enter numerical values")
        elif str(self.dailye_var.get()).isalpha():
            messagebox.showerror("Error", "Please enter numerical values")
        elif str(self.goal_var.get()).isalpha():
            messagebox.showerror("Error", "Please enter numerical values")
        else:
            print(self.monthlyi_var.get())
            self.update_welcome_message(self.monthlyi_var.get())
            print(self.monthlye_var.get())
            self.update_welcome_message(self.monthlye_var.get())
            print(self.savings_var.get())
            self.update_welcome_message(self.savings.get())
            print(self.dailye.get())
            self.update_welcome_message(self.dailye.get())
            print(self.goal_var.get())
            self.update_welcome_message(self.goal.get())



        
        self.msg='Please choose one of the options to continue'
        self.welcome_prompt_widget['text']=self.msg
        
        self.back_name_enter_button['command']=self.load_income_savings_widget
        self.countdownB['command']=self.count
        self.graphB['command']=self.graph
        self.countdownB.pack(pady=10,
                ipady = 10,
                ipadx = 10,)
        self.graphB.pack(pady=10,
                ipady = 10,
                ipadx = 10,
                after=self.countdownB,)

        self.int_savings_var=float(self.savings_var.get())
        self.int_monthlyi_var=float(self.monthlyi_var.get())
        self.int_monthlye_var=float(self.monthlye_var.get())
        self.int_dailye_var=float(self.dailye_var.get())
        self.int_goal_var=float(self.goal_var.get())


    def count(self):            
        self.last_page_button.forget()        
        self.savings_var.get()
        self.monthlyi_var.get()
        self.monthlye_var.get()
        self.monthlyetype_var.get()
        self.dailye_var.get()
        self.goal_var.get()
        self.gnote_var.get()
        self.countdownB.forget()
        self.graphB.forget()

       
        
        self.back_name_enter_button['command']=self.selection
        self.back_name_enter_button['anchor']= anchor=SW

        self.monthly_expense_t = (self.int_dailye_var*30) + self.int_monthlye_var
        self.monthly_net = self.int_monthlyi_var - self.monthly_expense_t
        self.goal_final = self.int_goal_var - self.int_savings_var
        self.eta = self.goal_final/self.monthly_net
        
        print(self.eta)
        self.etag = self.eta * 60 * 60 * 24 * 30.4
        self.etag2 = float(round(int(self.etag)))
        print(self.etag)
        print(self.etag2)

        self.count()

    def graph(self):
        

        self.last_page_button.forget()
        self.countdownB.forget()
        self.graphB.forget()

        self.back_name_enter_button['command']=self.selection
        self.back_name_enter_button['anchor']= anchor=SW

        self.mi_percent=self.int_monthlyi_var/((self.int_monthlyi_var)+(self.int_monthlye_var)+(self.int_dailye_var))*100
        self.me_percent=self.int_monthlye_var/((self.int_monthlyi_var)+(self.int_monthlye_var)+(self.int_dailye_var))*100
        self.de_percent=self.int_dailye_var/((self.int_monthlyi_var)+(self.int_monthlye_var)+(self.int_dailye_var))*100
        

        labels = 'Income', 'Monthly expense', 'Daily Expense'
        sizes = [self.mi_percent, self.me_percent, self.de_percent]
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        #explode = (0.1, 0, 0, 0)  # explode 1st slice
 
        # Plot
        plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')
        plt.show()

        self.graph()

    def load_results(self):
        global name_prompt_widget 
        global savings_prompt_widget 
        global monthlyi_prompt_widget
        global monthlye_prompt_widget 
        global monthlyetype_prompt_widget 
        global dailye_prompt_widget 
        global goal_prompt_widget 
        global gnote_prompt_widget
        #I have been strugging with the passing of variables and creating new windows with this
            
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
        str1=str(self.monthlyi_var.get())
        str2=str(self.savings_var.get())
        str3=str(self.monthlye_var.get())
        str4=str(self.monthlyetype_var.get())
        str5=str(self.dailye_var.get())
        str6=str(self.goal_var.get())
        str7=str(self.gnote_var.get())
        header = "{0:30},{1:30},{2:30},{3:30},{4:30},{5:30},{6:30}"\
                .format(str1, str2, str3, str4, str5, str6, str7)
        text_file.write(header+'\n')
        text_file.close()
        self.selection()
            

    def load_income_savings_widget(self):
        self.countdownB.forget()
        self.graphB.forget()

        self.welcome_prompt_widget.pack(pady=15,             
            ipady = 5,
            ipadx = 5,
            after=self.logo_img, 
            anchor=N, )

        self.monthlyi_prompt_widget.pack(pady=5,             
            ipady = 2,
            ipadx = 5,
            after=self.welcome_prompt_widget, 
            anchor=N, )
        self.monthlyi_input_widget.pack()

        self.savings_prompt_widget.pack(pady=5,             
            ipady = 2,
            ipadx = 5,
            after=self.monthlyi_input_widget, 
            anchor=N, )
        self.savings_input_widget.pack()

        self.monthlye_prompt_widget.pack(pady=5,             
            ipady = 2,
            ipadx = 5,
            after=self.savings_input_widget, 
            anchor=N, )
        self.monthlye_input_widget.pack()

        self.monthlyetype_prompt_widget.pack(pady=5,             
            ipady = 2,
            ipadx = 5,
            after=self.monthlye_input_widget, 
            anchor=N, )
        self.monthlyetype_input_widget.pack()

        self.dailye_prompt_widget.pack(pady=5,             
            ipady = 2,
            ipadx = 5,
            after=self.monthlyetype_input_widget, 
            anchor=N, )
        self.dailye_input_widget.pack()

        self.goal_prompt_widget.pack(pady=5,             
            ipady = 2,
            ipadx = 5,
            after=self.dailye_input_widget, 
            anchor=N, )
        self.goal_input_widget.pack()

        self.gnote_prompt_widget.pack(pady=5,             
            ipady = 2,
            ipadx = 5,
            after=self.goal_input_widget, 
            anchor=N, )
        self.gnote_input_widget.pack()
        
        self.last_page_button.pack(anchor=SE)
        self.back_name_enter_button.pack(anchor=SW)
# validation of name not being number
    def load_input_widgets(self):
        if str(self.name_var.get()).isnumeric():
            messagebox.showerror("Error", "Please enter characters")
        else:
            print(self.name_var.get())
            self.update_welcome_message(self.name_var.get())

            # clear screen and load next page
            self.name_input_widget.pack_forget()
            self.name_enter_button.pack_forget()
            self.name_prompt_widget.pack_forget()
            
            self.load_income_savings_widget()

    def update_welcome_message(self, str1):
        msg = "Welcome {0}. Please provide the requested info below to get started!"\
                .format(str1)

        self.welcome_prompt_widget = Label(self.root,
                font = "Verdana 11 bold", 
                text=msg)

    def load_namep(self):
        self.monthlyi_input_widget.pack_forget()
        self.monthlyi_prompt_widget.pack_forget()
        self.savings_input_widget.pack_forget()
        self.savings_prompt_widget.pack_forget()
        self.back_name_enter_button.pack_forget()
        self.last_page_button.pack_forget()
        self.welcome_prompt_widget.pack_forget()
        self.name_prompt_widget.forget()
        self.name_input_widget.forget()
        self.monthlye_input_widget.pack_forget()
        self.monthlye_prompt_widget.pack_forget()
        self.monthlyetype_input_widget.pack_forget()
        self.monthlyetype_prompt_widget.pack_forget()
        self.dailye_input_widget.pack_forget()
        self.dailye_prompt_widget.pack_forget()
        self.goal_input_widget.pack_forget()
        self.goal_prompt_widget.pack_forget()
        self.gnote_input_widget.pack_forget()
        self.gnote_prompt_widget.pack_forget()

        self.name_prompt_widget.pack(pady=35,             
                ipady = 5,
                ipadx = 5,
                after=self.logo_img, 
                anchor=N, )

        self.name_input_widget.pack()
        self.name_enter_button.pack(pady=10,
                    ipady = 10,
                    ipadx = 10,
                    after=self.name_input_widget, 
                    anchor=N, )



if __name__ == "__main__":
    app = FinanceApp(root)
    app.launch_app()

