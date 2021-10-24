
print("\nWelcome to Python Roullette! Reds, Blacks, Uppers, Lowers, Odds, Evens = 2XBet; 0G and 00G = 35XBet. Here is the Wheel: ")

import random
wheel = ['00G', '27R', '10B', '25R', '29B', '12R', '8B', '19R', '31B',
'18R', '6B', '21R', '33B', '16R', '4B', '23R', '35B', '14R', '2B', '0G', '28B',
'9R', '26B', '30R', '11B', '7R', '20B', '32R', '17B', '5R', '22B', '34R', '15B', '3R', '24B', '36R', '13B', '1R']

for chunk in wheel:
    print(chunk, end=' ')

print('\n\nYou have $2000 to start!  Min Bet $10, Max Bet $2000')

red = ['27R', '25R', '12R', '19R', '18R', '21R', '16R', '23R', '14R', '9R', '30R', '7R', '32R', '5R', '34R', '3R', '36R', '1R']
black = ['10B', '29B', '8B', '31B', '6B', '33B', '4B', '35B', '2B', '28B', '26B', '11B', '20B', '17B', '22B', '15B', '24B', '13B']
green1 = ['00G']
green2 = ['0G']
odds = ['27R', '25R', '19R', '21R', '23R', '9R', '7R', '5R', '3R', '1R', '29B', '31B', '33B', '35B', '11B', '17B', '15B', '13B']
evens = ['12R', '18R', '16R', '14R', '30R', '32R', '34R', '36R', '10B', '8B', '6B', '4B', '2B', '28B', '26B', '20B', '22B', '24B']
uppers = ['27R', '25R', '19R', '21R', '23R', '30R', '32R', '34R', '36R', '29B', '31B', '33B', '35B', '28B', '26B', '20B', '22B', '24B']
lowers = ['12R', '18R', '16R', '14R', '9R', '7R', '5R', '3R', '1R', '10B', '8B', '6B', '4B', '2B', '11B', '17B', '15B', '13B']

w = 2000
choice6 = 9

print(' ')
SpinHistory = []

while True:
    Spin1 = random.choice(wheel)
    choice1 = input('\nWould you like to spin the Roullette Wheel or Make a Bet? (1=spin, 2=bet): ')
    choice1 = int(choice1)
    choice6 = 9
    if choice1 == 1:
        SpinHistory.append(Spin1)
        for fart in SpinHistory:
            print(fart, end=' ')
    elif choice1 == 2:
        choice2 = input('\nHow much would you like to bet? (10-2000 use increments of 10): ')
        choice2 = int(choice2)
        choice3 = input('\nPlace Your Bet: 1=Blacks, 2=Reds, 3=odds, 4=evens, 5=uppers, 6=lowers, 7=0G, 8=00G: ')
        choice3 = int(choice3)
        w = w-choice2
        print('Total Amount Remaining: ' + str(w))
        choice4 = input('\nWould you like to add another bet or spin? (1=spin, 2=bet): ')
        choice4 = int(choice4)
        if choice4 == 2:
            choice5 = input('\nHow much would you like to bet? (10-2000 use increments of 10): ')
            choice5 = int(choice5)
            choice6 = input('\nPlace Your Bet: 1=Blacks, 2=Reds, 3=odds, 4=evens, 5=uppers, 6=lowers, 7=0G, 8=00G: ')
            choice6 = int(choice6)
            w = w-choice5
            print('Total Amount Remaining: ' + str(w))

        print("\nLet's Spin The Wheel!: ")
        SpinHistory.append(Spin1)
        for fart in SpinHistory:
            print(fart, end=' ')
        if choice3 == 1 and Spin1 in black:
            print('\nYOU WIN! ')
            w = w + 2*choice2
            print('\nTotal Amount Remaining: ' + str(w))
        if choice3 == 2 and Spin1 in red:
            print('\nYOU WIN! ')
            w = w + 2*choice2
            print('\nTotal Amount Remaining: ' + str(w))
        if choice3 == 3 and Spin1 in odds:
            print('\nYOU WIN! ')
            w = w + 2*choice2
            print('\nTotal Amount Remaining: ' + str(w))
        if choice3 == 4 and Spin1 in evens:
            print('\nYOU WIN! ')
            w = w + 2*choice2
            print('\nTotal Amount Remaining: ' + str(w))
        if choice3 == 5 and Spin1 in uppers:
            print('\nYOU WIN! ')
            w = w + 2*choice2
            print('\nTotal Amount Remaining: ' + str(w))
        if choice3 == 6 and Spin1 in lowers:
            print('\nYOU WIN! ')
            w = w + 2*choice2
            print('\nTotal Amount Remaining: ' + str(w))
        if choice3 == 7 and Spin1 in green2:
            print('\nYOU WIN! ')
            w = w + 35*choice2
            print('\nTotal Amount Remaining: ' + str(w))
        if choice3 == 8 and Spin1 in green1:
            print('\nYOU WIN! ')
            w = w + 35*choice2
            print('\nTotal Amount Remaining: ' + str(w))

        if choice6 == 1 and Spin1 in black:
            print('\nYou WIN! ')
            w = w + 2*choice5
            print('\nTotal Amount Remaining: ' + str(w))
        if choice6 == 2 and Spin1 in red:
            print('\nYou WIN! ')
            w = w + 2*choice5
            print('\nTotal Amount Remaining: ' + str(w))
        if choice6 == 3 and Spin1 in odds:
            print('\nYou WIN! ')
            w = w + 2*choice5
            print('\nTotal Amount Remaining: ' + str(w))
        if choice6 == 4 and Spin1 in evens:
            print('\nYou WIN! ')
            w = w + 2*choice5
            print('\nTotal Amount Remaining: ' + str(w))
        if choice6 == 5 and Spin1 in uppers:
            print('\nYou WIN! ')
            w = w + 2*choice5
            print('\nTotal Amount Remaining: ' + str(w))
        if choice6 == 6 and Spin1 in lowers:
            print('\nYou WIN! ')
            w = w + 2*choice5
            print('\nTotal Amount Remaining: ' + str(w))
        if choice6 == 7 and Spin1 in green2:
            print('\nYou WIN! ')
            w = w + 35*choice5
            print('\nTotal Amount Remaining: ' + str(w))
        if choice6 == 8 and Spin1 in green1:
            print('\nYou WIN! ')
            w = w + 35*choice5
            print('\nTotal Amount Remaining: ' + str(w))






    else:
        print('\nPlease enter 1 for Spin or 2 for Bet: ')
