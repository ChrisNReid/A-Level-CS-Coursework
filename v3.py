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

def initial():

    enter1=input(' If you would like to enter your income (enter i)/ your expenses (enter e)/ your financial goal (enter g)')
    if enter1==('i'):
        income()
    elif enter1==e:
        expense()
    elif enter1==g:
        goal()
    else:
        print('Please select one of the options')
        initial()


        def income():
            inc1=input('Would you like to enter either a unique (enter u) or monthly income( enter m)')
            if inc1==u:
                uniquei= input(int('Enter your unique income £'))

            elif inc1==m:
                monthlyi= input(int('Enter your monthly income £'))
            else:
                print('Please enter a specified option')
                income()

        def expense():
            exp1=input('Would you like to enter either a unique expense(enter u) or monthly expense( enter m) or a daily expense(d)')
            if exp1==u:
                uniquee= input(int('Enter your unique expense £'))

            elif exp1==m:
                monthlye= input(int('Enter your monthly income £'))
                monthlye_type= input(' what industry sector was its pent on (food/travel/fun)')
                if monthly3_type==fun:
                    fun=fun+monthlye
                elif monthly3_type==travel:
                    travel=travel+monthlye
                elif monthly3_type==food:
                    food=food+monthlye
                elif exp1==d:
                    dailye=input(int('Enter your estimated daily average expense'))
                else:
                    print('Please enter a specified option')
                    expense()
        def goal():
            g1=int(input('enter your financial goal/ amount wanting to save'))
            g_note=input(str('enter  a note/ remonder for this goal'))
initial()
