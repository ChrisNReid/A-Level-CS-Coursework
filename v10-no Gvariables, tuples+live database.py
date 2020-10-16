



import time
import tkinter
print('welcome to this app')
print('*******************')
print()
print('So we are gonna ask for your financial goal and then you can give us your estimated daily income and expense,')
print('then we can return your estimated time to reach your goal')
print()

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
    
    initiali=float(input('Enter your initial savings £'))
    array[0][0]=initiali


    monthlyi=float(input('Enter your monthly income £'))
    array[0][1]=monthlyi
    return (array, initiali, monthlyi)
               

def expense(array):
   
    monthlye=int(input('what is your your monthly repeptive expense? £'))
    monthlye_type=str(input('what industry sector was its spent on (food/travel/fun)'))
    array[2][0]= monthlye
    if monthlye_type=='fun':
        array[4][1]=monthlye
    elif monthlye_type=='travel':
        array[5][1]=monthlye
    elif monthlye_type=='food':
        array[6][1]=monthlye
    else:
        print('please enter one of the option')

    dailye=int(input('Enter your estimated daily average expense £'))
    array[1][0]=dailye
    return (array, monthlye, dailye)
               
            
def goal(array):
    
    g1=int(input('enter your financial goal/ amount wanting to save £'))
    g_note=str(input('enter  a note/ reminder for this goal '))
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



def rec(n):
    time.sleep(.5)
    print(n)
    if n>0:
        rec(n-1)
rec(5)

etag=eta*60*60*24*30.4
etag2=int(round(float(etag)))

 
if eta<=0:
    print('it will take ',eta, ' months to reach our goal, meaning your are loosing money.')
    print(' try and fix this by reducing your monthy and daily exesnes')
else:
    print('it will take ',eta, ' months to reach our goal')
    import time
    boom=etag2
    while boom >0:
        time.sleep(1)
        print(boom , 'seconds till goal is reached')
        boom -=1
print('Goal Reached, check your bank balance ;)')
    

# income-[initial,monthly],expense[daily,nothing],[monthly,nothing],goal[amount,note], type[fun,0],[travel,0],[food,0]]









