from tkinter import *
from PIL import ImageTk,Image  
from tkinter import messagebox


# root - base frame
root = Tk()






# widget to hold the logo
# trying to add a a seperate background for the area with the logo
#f1=Frame(root,width=800,height=100,bg= 'blue')
#f1.pack()
logo = ImageTk.PhotoImage(Image.open("final_logo.jpg"))  
logo_img = Label(root, image=logo)

countdownB=Button(root, text='Countdown', anchor=W)
graphB=Button(root, text='graph',anchor=E)

name_input_widget = Entry(root, width=30, textvariable=name_var)
savings_input_widget = Entry(root, width=30, textvariable=savings_var)
monthlyi_input_widget = Entry(root, width=30, textvariable=monthlyi_var)
monthlye_input_widget = Entry(root, width=30, textvariable=monthlye_var)
monthlyetype_input_widget = Entry(root, width=30, textvariable=monthlyetype_var)
dailye_input_widget = Entry(root, width=30, textvariable=dailye_var)
goal_input_widget = Entry(root, width=30, textvariable=goal_var)
gnote_input_widget = Entry(root, width=30, textvariable=gnote_var)


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
        self.monthlye_var= StringVar(self.root)
        self.monthlyetype_var= StringVar(self.root)
        self.dailye_var= StringVar(self.root)
        self.goal_var= StringVar(self.root)
        self.gnote_var= StringVar(self.root)

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
        self.goal_prompt='Please enter your financial goal'
        self.gnote_prompt='Please enter a note for your goal(optional)'

    def prepare_app_widgets(self):
        # widget to hold the name prompt
        name_prompt_widget = Label(self.root,
                    font = "Verdana 10 bold", 
                    text=self.name_prompt)

        # widget to hold the name prompt
        monthlyi_prompt_widget = Label(self.root,
                    font = "Verdana 9", 
                    text=self.monthlyi_prompt)

        # widget to hold the name prompt
        savings_prompt_widget = Label(self.root,
                    font = "Verdana 9 ", 
                    text=self.savings_prompt)

        #expense widget
        monthlye_prompt_widget= Label(self.root,
                font='Verdana 9',
                text=self.monthlye_prompt)

        monthlyetype_prompt_widget= Label(self.root,
                font='Verdana 9',
                text=self.monthlyetype_prompt)

        dailye_prompt_widget= Label(self.root,
                font='Verdana 9',
                text=self.dailye_prompt)

        goal_prompt_widget= Label(self.root,
                font='Verdana 9',
                text=self.goal_prompt)

        gnote_prompt_widget= Label(self.root,
                font='Verdana 9',
                text=self.gnote_prompt)
                

        msg = "Welcome {0}. Please provide the requested info below to get started!"\
                .format(self.name_var.get())

        welcome_prompt_widget = Label(self.root,
                font = "Verdana 11 bold", 
                text=msg)
        

    def launch_app(self):
        self.prepare_app_vars()
        self.prepare_app_prompts()
        self.logo_img.pack(anchor=N)
        self.load_namep()
        self.root.mainloop()

if __name__ == "__main__":
    app = FinanceApp(root)
    app.launch_app()

