import time
print('welcome to this app')
print('*******************')
print()
print('So we are gonna ask for your financial goal and then you can give us your estimated daily income and expense,')
print('then we can return your estimated time to reach your goal')
print()
#goal=int(input('how much would you like to save? £'))
#inc=int(input('Okay, what is your aveage daily income? £'))
#exp=int(input('Nice, and finally whats your average daily epenses? £'))
    
#save=(inc - exp)
#print('You could have £',save, 'a day')
#eta=int(goal/save)
food=0
fun=0
travel=0




def income():
            
                global initiali=int(input('Enter your initial savings £'))
                array[0][0]=initiali


                global monthlyi= input(int('Enter your monthly income £'))
                array[0][1]=monthlyi
            
               

def expense():

           
				global monthlye=  int(input('what is your your monthly repeptive expense? £')
                monthlye_type= input(' what industry sector was its spent on (food/travel/fun)')
                array[2][0]= monthlye
                if monthlye_type==fun:
                    array[4][1]=monthlye
                elif monthlye_type==travel:
                    array[5][1]=monthlye
                elif monthlye_type==food:
                    array[6][1]=monthlye
            
                global dailye=input(int('Enter your estimated daily average expense'))
                array[1][0]=dailye

               
            
def goal():
            global g1=int(input('enter your financial goal/ amount wanting to save'))
            g_note=input(str('enter  a note/ remonder for this goal'))
            array[3][0]=g1
            array[3][1]=g_note
def initial():

    income()
    expense()
	goal()
    

		
initial()

monthly_expense_t= (dailye*30)+monthlye
monthly_net=monthlyi-monthy_expense_t
goal_final=g1-initiali
eta=goal_final/monthly_net
print(eta)

# income-[initial,monthly],expense[daily,nothing],[monthly,nothing],goal[amount,note], type[fun,0],[travel,0],[food,0]]
array=[ [0,0],
        [0,0],
        [0,0],
        [0,0],
        [fun,0],
        [travel,0],
        [food,0]     ];
