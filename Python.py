import re
import time
price=[]


def Total_Price(cost,seat,fare,age):
    Total_Price=(cost+seat+fare)*age

    return Total_Price

def User_destination():
    User_destination=str.upper(input('Choose a destinaton and trip length. Fare choices are displayed below:\n (C1)Cairn One Way - 250\n (C2) Cairn Return - 400\n\n (S1)Sydney One Way - 420\n (S2)Sydney Return - 575\n\n (P1)Perth One Way - 510\n (P2)Perth Return - 700:\n'))

    while User_destination != 'C1' and User_destination != 'C2' and User_destination != 'S1' and User_destination != 'S2' and User_destination != 'P1' and User_destination != 'P2':
        User_destination = str.upper(input('Sorry, You should entry S1, S2, C1, C2, P1 or P2, Please entry again: \n'))
    if User_destination=='C1':
        print('You are going to order Cairn One Way. Costing is 250.\n')
        userchoose='Carin One way'

    elif User_destination=='C2':
        print('You are going to order Cairn Return. Costing is 400.\n')
        userchoose = 'Cairn Return'

    elif User_destination=='S1':
        userchoose = 'Sydney One Way'
        print('You are going to order Sydney One Way. Costing is 420.\n')

    elif User_destination=='S2':
        print('You are going to order Sydney Return. Costing is 575.\n')
        userchoose = 'Sydney Return'

    elif User_destination=='P1':
        print('You are going to order Perth One Way. Costing is 510.\n')
        userchoose = 'Perth One Way'

    elif User_destination=='P2':
        print('You are going to order Perth Return. Costing is 700.\n')
        userchoose = 'Perth Return'

    return userchoose

def destination(userchoose):

    User_destination=userchoose
    cost=0
    if User_destination =='Carin One way':
        cost=250

    elif User_destination =='Cairn Return':
        cost=400

    elif User_destination=='Sydney One Way':
        cost=420

    elif User_destination=='Sydney Return':
        cost=575

    elif User_destination=='Perth One Way':
        cost=510

    elif User_destination=='Perth Return':
        cost=700

    return cost


def User_fare():
    User_fare=str.upper(input(' (B)usiness - 275\n (E)conomy - 25 \n (F)rugal - 0 \n'))
    while User_fare != 'B' and User_fare != 'E' and User_fare != 'F':
        User_fare = str.upper(input('Sorry, You should entry B, E or F, Please entry again: \n'))

    if User_fare=='B':
        print('You are going to order Business Fare. Costing is 275.\n')
        userfare='Business Fare'
    elif User_fare=='E':
        print('You are going to order Economy Fare. Costing is 25.\n')
        userfare='Economy Fare'
    elif User_fare=='F':
        print('You are going to order Frugal Fare. Costing is 0.\n')
        userfare='Frugal Fare'
    return userfare

def costfare(userfare):
    User_fare=userfare
    fare=0
    if User_fare=='Business Fare':
        fare=275
    elif User_fare=='Economy Fare':
        fare=25
    elif User_fare=='Frugal Fare':
        fare=0
    return fare


def User_seat():
    User_seat=str.upper(input(' (W)indow - 75\n (A)isle - 50\n (M)idle - 25\n'))

    while User_seat != 'W' and User_seat !='A' and User_seat != 'M':
        User_seat = str.upper(input('Sorry, You should entry W, A, or M, Please entry again:\n'))

    if User_seat=='W':
        print('You are going to order Window seat. Seat costing is 75.\n')
        userseat='Window seat'
    elif User_seat=='A':
        print('You are going to order Aisle seat. Seat costing is 50.\n')
        userseat = 'Aisle seat'
    elif User_seat=='M':
        print('You are going to order Midle seat. Seat costing is 25.\n')
        userseat = 'Midle seat'
    return userseat

def costseat(userseat):
    User_seat=userseat
    seat=0
    if User_seat=='Window seat':
        seat=75
    elif User_seat=='Aisle seat':
        seat=50
    elif User_seat=='Midle seat':
        seat=25
    return seat

def User_age():
    User_age=input("Please entry your age in here:\n")
    while not re.findall("^[0-9]+$", User_age):
        User_age = input('Only can entry valid number for you age ：\n')
    return User_age

def agechoose(realage):

    realage=int(realage)
    if realage<16:
        print('You age is',realage,'Your age are under the 16 years old. Half price.\n')
        age=0.5
    else:
        print('You age is',realage,'Your age are beyand the 16 years old. Normal price. \n')
        age=1
    return age

def User_book(total,Total_price,destination):
    print('Calculating fare..\n')
    time.sleep(1)
    print('Calculating fare.\n')
    time.sleep(1)
    print(total, '\n')
    print('There are total price:',price[len(price)-1], 'Thanks so much you can choose our Tropical Airlines.')
    User_book = str.upper(input('Do you want to book one more time? (Y)ES or (N)O \n'))
    while User_book!='Y' and User_book!='N':
        User_book = str.upper(input('Sorry, You should entry correct letter, Please entry again! \n'))
    if User_book == 'Y':
        print('Right now, the Total price: ',Total_price)
        main()
    elif User_book == 'N':
        print('Total price: ',sum(price))
        print('Thank you for visiting Tropical Airlines')

    return User_book

def calculater(Username):
    userchoose=User_destination()
    cost=destination(userchoose)
    userfare=User_fare()
    fare=costfare(userfare)
    if fare ==0:
        print('Sorry, you cannot choose seat.\n')
        realage = User_age()
        age = agechoose(realage)
        Total_price = Total_Price(cost,0, fare,age,)
        price.append(Total_price)
        total = 'Ticket for(Frugal): ' + Username + '\n' + userchoose + ': ' + str(cost) + '\n' + userfare + ': ' + str(fare) + '\n' + 'Age:' + str(realage)
    else:
        userseat=User_seat()
        seat=costseat(userseat)
        realage = User_age()
        age = agechoose(realage)
        Total_price = Total_Price(cost, seat, fare, age)
        price.append(Total_price)
        total = 'Ticket for: ' + Username + '\n' + userchoose + ': ' + str(cost) + '\n' + userseat + ': ' + str(
            seat) + '\n' + userfare + ': ' + str(fare) + '\n' + 'Age:' + str(realage)


    User_book(total,Total_price,destination)
    return total

def rechoose(Username):
    User_choose = str.upper((input('Its purchase for yourself or another person(Y or N)?\n')))
    while User_choose!='Y' and User_choose!='N':
        User_choose = str.upper((input('Please entry correct letters. Try again! \n')))

    if User_choose == 'N':
        Username = input('Can you write down another person name:\n')
        print(' Welcome to the ordering systems', Username)
    elif User_choose == 'Y':
        print('Welcome to Tropical Airlines online sevices again', Username)
    return Username

def menu():
    print('Welcome to Tropical Airlines online services.')
    Username=input('Please put into your name: \n')
    print( ' Welcome to the ordering systems', Username,'\n')

    return Username
#--------------------------------------------------------------------------------------
def main():
    Username=menu()
    print('*****************MENU*********************')
    User_choose=str.upper(input('(I)nformation, (O)rder ticket, (E)xit : \n'))
    while User_choose!='E' and User_choose!='O' and User_choose!='I':
        User_choose = str.upper(input('Sorry, you should entry I(i), O(o) or E(e), Please entry again.\n'))

    if User_choose=='I':
            print('Thank you for choosing Tropical Airlines for your air travel needs. You will be asked questions regarding what type of ticket you would like to purchase as well as destination information. We also offer 50% discounted fares for children.\n')
            Username = rechoose(Username)
            calculater(Username)
    elif User_choose=='O':
                    Username = rechoose(Username)
                    calculater(Username)
    elif User_choose=='E':
        print('Thank you for visiting Tropical Airlines.')

    return Username

main()