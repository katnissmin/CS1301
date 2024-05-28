"""
Georgia Institute of Technology - CS1301
HW01 - Functions & Expressions
"""
#########################################

"""
Function Name: tasteOfTech()
Parameters: N/A
Returns: None
"""

def tasteOfTech():
    name = input("What is your first name? ")
    tin = float(input("How much did you spend at Tin Drum? "))
    waffle = float(input("How much did you spend at Waffle House? "))
    buffalo = float(input("How much did you spend at Buffalo Wild Wings? "))

    print("Congratulations {}! You spent ${} in total and earned {} DOGE.".format(name, round((tin + waffle + buffalo), 2), round(14.57 * (tin + waffle + buffalo), 2)))


#########################################

"""
Function Name: shoppingMoney()
Parameters: N/A
Returns: None
"""

def shoppingMoney():
    income = round(float(input("How much is your monthly income? ")), 2)
    foodhouse = round((income - 700 - 320), 2)
    save = round((foodhouse * 0.6), 2)
    spend = round((foodhouse * 0.4), 2)
    print("You can save ${} and spend the remaining ${} on anything this month.".format(save, spend))


#########################################

"""
Function Name: houseParty()
Parameters: N/A
Returns: None
"""

def houseParty():
    nugget = int(input("How many chicken nuggets will each guest eat? "))
    onion = int(input("How many onion rings will each guest eat? "))
    donut = int(input("How many donuts will each guest eat? "))
    cookie = int(input("How many cookies will each guest eat? "))
    guests = int(input("How many guests are you expecting at the party? "))

    print("You need to buy {} chicken nuggets, {} onion rings, {} donuts and {} cookies for {} guests.".format(
        nugget * guests, onion * guests, donut * guests, cookie * guests, guests))


#########################################

"""
Function Name: spareTime()
Parameters: N/A
Returns: None
"""

#(have 16 hours to use)

#16*7 = 112 hours per week
#take XX creds
#study XX * 3 creds

#free 112-XX-XX*3 hours a week
#free (112-XX-XX*3)/7 hrs a day

def spareTime():
    credits = int(input("How many credits are you taking? "))
    free_time = 16 * 7 - credits - credits * 3

    free_hour = free_time / 7

    import math
    result = math.modf(free_hour)

    hour = int(result[1])
    mins = round(60 * result[0], 1)

    print("You have {} hours and {} minutes per day to spare for other activities.".format(hour, mins))


#########################################

"""
Function Name: ratsNight()
Parameters: N/A
Returns: None
"""

def ratsNight():
    video = int(input("How many slots would you like to book for video games? "))
    trivia = int(input("How many slots would you like to book for trivia time? "))
    arts = int(input("How many slots would you like to book for arts/crafts? "))

    time1 = video * 30 + trivia * 10 + arts * 45
    time2 = time1 / 60


    import math
    result = math.modf(time2)

    hourss = int(result[1])
    minss = round((60 * result[0]))

    print("You will spend {} hours and {} minutes at Rats Night.".format(hourss, minss))

