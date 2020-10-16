import time
import tkinter
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
array=[ [0,0],
        [0,0],
        [0,0],
        [0,0],
        [fun,0],
        [travel,0],
        [food,0]     ];



def income(array):
    
    initiali=int(input('Enter your initial savings £'))
    array[0][0]=initiali


    monthlyi=int(input('Enter your monthly income £'))
    array[0][1]=monthlyi
    return (array, initiali, monthlyi)
               

def expense(array):
   
    monthlye=int(input('what is your your monthly repeptive expense? £'))
    monthlye_type=input('what industry sector was its spent on (food/travel/fun)')
    array[2][0]= monthlye
    if monthlye_type==fun:
        array[4][1]=monthlye
    elif monthlye_type==travel:
        array[5][1]=monthlye
    elif monthlye_type==food:
        array[6][1]=monthlye

    dailye=int(input('Enter your estimated daily average expense '))
    array[1][0]=dailye
    return (array, monthlye, dailye)
               
            
def goal(array):
    
    g1=int(input('enter your financial goal/ amount wanting to save '))
    g_note=input(str('enter  a note/ remonder for this goal '))
    array[3][0]=g1
    array[3][1]=g_note
    return (array, g1)
def initial(array):
    (array, initiali, monthlyi)=income(array)
    (array, monthlye, dailye)=expense(array)
    (array,g1)=goal(array)
    return (array, initiali, monthlyi, monthlye, dailye, g1)

		
(array, initiali, monthlyi, monthlye, dailye, g1)=initial(array)

monthly_expense_t=(dailye*30)+monthlye
monthly_net=monthlyi-monthly_expense_t
goal_final=g1-initiali
eta=goal_final/monthly_net
print('it will take ',eta, ' months to reach our goal')

# income-[initial,monthly],expense[daily,nothing],[monthly,nothing],goal[amount,note], type[fun,0],[travel,0],[food,0]]

