

print(' ')
import random
#print( "Here is a full deck of Cards Created In Python: "  )
print(' ')
deck = []
for suit in ['\u2663', '\u2660', '\u2665', '\u2666']:
    for rank in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
        deck.append(rank+suit)
#for card in deck:
#    print(card, end=' ')

print("\n\nLet Me Shuffle The Cards For You: " )
print(' ')

random.shuffle(deck)
for card in deck:
    print(card, end=' ')
print("\n\n\nNow Let Me Cut The Deck Down To 21 Cards and Deal 3 Stacks: ")
twentyone_card_deck = []
for card in range(0,21):
    twentyone_card_deck.append(deck[card])
for card in twentyone_card_deck:
    print(card, end=' ')

group_1 = []
group_2 = []
group_3 = []

for card in range(20,21):
    group_1.append(twentyone_card_deck[card])
for card in range(19,20):
    group_2.append(twentyone_card_deck[card])
for card in range(18,19):
    group_3.append(twentyone_card_deck[card])
for card in range(17,18):
    group_1.append(twentyone_card_deck[card])
for card in range(16,17):
    group_2.append(twentyone_card_deck[card])
for card in range(15,16):
    group_3.append(twentyone_card_deck[card])
for card in range(14,15):
    group_1.append(twentyone_card_deck[card])
for card in range(13,14):
    group_2.append(twentyone_card_deck[card])
for card in range(12,13):
    group_3.append(twentyone_card_deck[card])
for card in range(11,12):
    group_1.append(twentyone_card_deck[card])
for card in range(10,11):
    group_2.append(twentyone_card_deck[card])
for card in range(9,10):
    group_3.append(twentyone_card_deck[card])
for card in range(8,9):
    group_1.append(twentyone_card_deck[card])
for card in range(7,8):
    group_2.append(twentyone_card_deck[card])
for card in range(6,7):
    group_3.append(twentyone_card_deck[card])
for card in range(5,6):
    group_1.append(twentyone_card_deck[card])
for card in range(4,5):
    group_2.append(twentyone_card_deck[card])
for card in range(3,4):
    group_3.append(twentyone_card_deck[card])
for card in range(2,3):
    group_1.append(twentyone_card_deck[card])
for card in range(1,2):
    group_2.append(twentyone_card_deck[card])
for card in range(0,1):
    group_3.append(twentyone_card_deck[card])




print("\n ")
print("Stack 1: ")
for card in group_1:
    print(card, end=' ')
print("\n\nStack 2: ")
for card in group_2:
    print(card, end=' ')
print("\n\nStack 3: ")
for card in group_3:
    print(card, end=' ')
print("\n")
stack_pick_1 = input("Please Choose ANY CARD and Remember It In Your Mind and Only Tell Me Which Stack Your Card Is In: (1, 2, or 3): ")

stack_pick_1 = int(stack_pick_1)

if stack_pick_1 == 1:
    twenty_card_deck_2 = group_2 + group_1 + group_3
elif stack_pick_1 == 2:
    twenty_card_deck_2 = group_1 + group_2 + group_3
elif stack_pick_1 == 3:
    twenty_card_deck_2 = group_2 + group_3 + group_1
else:
    twenty_card_deck_2 = "Wrong Input"


print("\n\n\nI've Shuffled the Cards in a Magic Way, Can You Guess Which Stack Your Card Is In Now? ")
print(" ")

print("Stack 1:" + '\u25AF' + '\u25AF' + '\u25AF' + '\u25AF' + '\u25AF' + '\u25AF' + '\u25AF')
print("Stack 2:" + '\u25AF' + '\u25AF' + '\u25AF' + '\u25AF' + '\u25AF' + '\u25AF' + '\u25AF')
print("Stack 3:" + '\u25AF' + '\u25AF' + '\u25AF' + '\u25AF' + '\u25AF' + '\u25AF' + '\u25AF')


group_1a = []
group_2a = []
group_3a = []


for card in range(20,21):
    group_1a.append(twenty_card_deck_2[card])
for card in range(19,20):
    group_2a.append(twenty_card_deck_2[card])
for card in range(18,19):
    group_3a.append(twenty_card_deck_2[card])
for card in range(17,18):
    group_1a.append(twenty_card_deck_2[card])
for card in range(16,17):
    group_2a.append(twenty_card_deck_2[card])
for card in range(15,16):
    group_3a.append(twenty_card_deck_2[card])
for card in range(14,15):
    group_1a.append(twenty_card_deck_2[card])
for card in range(13,14):
    group_2a.append(twenty_card_deck_2[card])
for card in range(12,13):
    group_3a.append(twenty_card_deck_2[card])
for card in range(11,12):
    group_1a.append(twenty_card_deck_2[card])
for card in range(10,11):
    group_2a.append(twenty_card_deck_2[card])
for card in range(9,10):
    group_3a.append(twenty_card_deck_2[card])
for card in range(8,9):
    group_1a.append(twenty_card_deck_2[card])
for card in range(7,8):
    group_2a.append(twenty_card_deck_2[card])
for card in range(6,7):
    group_3a.append(twenty_card_deck_2[card])
for card in range(5,6):
    group_1a.append(twenty_card_deck_2[card])
for card in range(4,5):
    group_2a.append(twenty_card_deck_2[card])
for card in range(3,4):
    group_3a.append(twenty_card_deck_2[card])
for card in range(2,3):
    group_1a.append(twenty_card_deck_2[card])
for card in range(1,2):
    group_2a.append(twenty_card_deck_2[card])
for card in range(0,1):
    group_3a.append(twenty_card_deck_2[card])


#print("\n ")
#print("Stack 1: ")
#for card in group_1a:
#    print(card, end=' ')
#print("\nStack 2: ")
#for card in group_2a:
#    print(card, end=' ')
#print("\nStack 3: ")
#for card in group_3a:
#    print(card, end=' ')









stack_pick_2 = input("\n\nPlease Choose a Stack!: (1, 2, or 3) ")

stack_pick_2 = int(stack_pick_2)

if stack_pick_2 == 1:
    print("\nStack 1:")
    for card in group_1a:
        print(card, end=' ')
elif stack_pick_2 == 2:
    print("\nStack 2:")
    for card in group_2a:
        print(card, end=' ')
elif stack_pick_2 == 3:
    print("\nStack 3:")
    for card in group_3a:
        print(card, end=' ')
else:
    print("Wrong Inputz")


stack_confirm_1 = input("\n\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): ")
stack_confirm_1 = int(stack_confirm_1)

if stack_confirm_1 == 1 and stack_pick_2 == 1 and stack_pick_1 == 1:
    print("\nVery Good Guess! I think I can guess your card!")
    print("\nIs This Your Card?")
    print(group_1a[4])
    card_confirm_1 = input("\nPlease Choose 1: for Yes or 2: for No (1 or 2): ")
    card_confirm_1 = int(card_confirm_1)
    if card_confirm_1 == 1:
        print("\nGreat!  Thanks For Playing Python Magic Cards! ")
    else:
        print("\nIs This Your Card? ")
        print(group_1a[3])
        card_confirm_2 = input("\nPlease Choose 1: for Yes or 2: for No (1 or 2):")
        card_confirm_2 = int(card_confirm_2)
        print("\nThank You For Playing Python Magic Card Game!")

if stack_confirm_1 == 2 and stack_pick_2 == 1 and stack_pick_1 == 1:
    print("\nOoops! Your Card is Not In Stack 1! Let's Check Stack 2! ")
    for card in group_2a:
        print(card, end=' ')
    stack_confirm_2 = input("\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): ")
    stack_confirm_2 = int(stack_confirm_2)
    if stack_confirm_2 == 1:
        print("\nVery Good! It may take me more than 1 guess, but I think I can guess your card!")
        print("\nIs This Your Card?")
        print(group_2a[3])
        card_confirm_3 = input("\nPlease Choose 1: for Yes or 2: for No (1 or 2): ")
        card_confirm_3 = int(card_confirm_3)
        if card_confirm_3 == 1:
            print("\nGreat!  Thanks For Playing Python Magic Cards! ")
        if card_confirm_3 == 2:
            print("\nOoops!  Is This Your Card?")
            print(group_2a[4])
            card_confirm_4 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_4 = int(card_confirm_4)
            if card_confirm_4 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_4 == 2:
                print( "\nOoops Again!  Is This Your Card?"  )
                print(group_2a[2])
                card_confirm_5 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_5 = int(card_confirm_5)
                if card_confirm_5 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                if card_confirm_5 == 2:
                    print("\nSorry! I FAILED!")
                else:
                    print("\n Wrong Input")
    if stack_confirm_2 == 2:
        print( "\nOoops! Your Card is Not In Stack 2! Let's Check Stack 3! "  )
        for card in group_3a:
            print(card, end=' ')
        stack_confirm_3 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
        stack_confirm_3 = int(stack_confirm_3)
        if stack_confirm_3 == 1:
            print( "\nVery Good! I think I can guess your card!")
            print("\nIs This Your Card?"  )
            print(group_3a[3])
            card_confirm_6 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_6 = int(card_confirm_6)
            if card_confirm_6 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_6 == 2:
                print( "\nOoops!  Is This Your Card?"  )
                print(group_3a[2])
                card_confirm_7 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_7 = int(card_confirm_7)
                if card_confirm_7 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                if card_confirm_7 == 2:
                    print("\nSorry! I FAILED!")
            else:
                print("\nWrong Input!")
        else:
            print("\nWrong Input Or Your Card Must Have Disappeared!")
    else:
        print("\n ")

#
#
#

if stack_confirm_1 == 1 and stack_pick_2 == 2 and stack_pick_1 == 2:
    print( "\nVery Good Guess! It may take a few guesses, but I think I can guess your card!")
    print("\nIs This Your Card?"  )
    print(group_2a[3])
    card_confirm_1 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
    card_confirm_1 = int(card_confirm_1)
    if card_confirm_1 == 1:
        print("\nGreat!  Thanks For Playing Python Magic Cards! ")
    if card_confirm_1 == 2:
        print( "\nIs This Your Card? "  )
        print(group_2a[2])
        card_confirm_2 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2):"  )
        card_confirm_2 = int(card_confirm_2)
        if card_confirm_2 == 1:
            print( "\nThank You For Playing Python Magic Card Game!"  )
        elif card_confirm_2 == 2:
            print( "\nIs This Your Card? "  )
            print(group_2a[4])
            card_confirm_3 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2):"  )
            card_confirm_3 = int(card_confirm_3)
            if card_confirm_3 == 1:
                print( "\nThank You For Playing Python Magic Card Game!"  )
            else: print("\nWrong Input E or Maybe Your Card Disappeared!?")
        else:
            print("\nWrong Input A - Maybe Your Card Disappeared!?")
    else:
        print("\naaaaaaaa")


if stack_confirm_1 == 2 and stack_pick_2 == 2 and stack_pick_1 == 2:
    print( "\nOoops! Your Card is Not In Stack 2! Let's Check Stack 1! "  )
    for card in group_1a:
        print(card, end=' ')
    stack_confirm_2 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
    stack_confirm_2 = int(stack_confirm_2)
    if stack_confirm_2 == 1:
        print( "\nVery Good! I think I can guess your card!")
        print("\nIs This Your Card?"  )
        print(group_1a[3])
        card_confirm_3 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
        card_confirm_3 = int(card_confirm_3)
        if card_confirm_3 == 1:
            print("\nGreat!  Thanks For Playing Python Magic Cards! ")
        if card_confirm_3 == 2:
            print( "\nOoops!  Is This Your Card?"  )
            print(group_1a[4])
            card_confirm_4 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_4 = int(card_confirm_4)
            if card_confirm_4 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_4 == 2:
                print( "\nOoops Again!  Maybe Your Card Disappeared?"  )
        else:
            print("\n ")


    if stack_confirm_2 == 2:
        print( "\nOoops! Your Card is Not In Stack 1! Let's Check Stack 3! "  )
        for card in group_3a:
            print(card, end=' ')
        stack_confirm_3 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
        stack_confirm_3 = int(stack_confirm_3)
        if stack_confirm_3 == 1:
            print( "\nVery Good! I think I can guess your card!")
            print("\nIs This Your Card?"  )
            print(group_3a[3])
            card_confirm_6 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_6 = int(card_confirm_6)
            if card_confirm_6 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_6 == 2:
                print( "\nOoops!  Is This Your Card?"  )
                print(group_3a[2])
                card_confirm_7 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_7 = int(card_confirm_7)
                if card_confirm_7 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                elif card_confirm_7 == 2:
                    print("\nSorry! I FAILED! Maybe Your Card Disappeared in the Computer!")
                else:
                    print("Wrong Input! D")
            else:
                print("\n ")
        else:
            print("\nWrong Input Or Your Card Must Have Disappeared!")
    else:
        print("\n ")


#
#
#

if stack_confirm_1 == 1 and stack_pick_2 == 3 and stack_pick_1 == 3:
    print( "\nVery Good Guess! I think I can guess your card!")
    print("\nIs This Your Card?"  )
    print(group_3a[3])
    card_confirm_1 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
    card_confirm_1 = int(card_confirm_1)
    if card_confirm_1 == 1:
        print("\nGreat!  Thanks For Playing Python Magic Cards! ")
    else:
        print( "\nIs This Your Card? "  )
        print(group_3a[2])
        card_confirm_2 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2):"  )
        card_confirm_2 = int(card_confirm_2)
        print( "\nThank You For Playing Python Magic Card Game!"  )

if stack_confirm_1 == 2 and stack_pick_2 == 3 and stack_pick_1 == 3:
    print( "\nOoops! Your Card is Not In Stack 3! Let's Check Stack 2! "  )
    for card in group_2a:
        print(card, end=' ')
    stack_confirm_2 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
    stack_confirm_2 = int(stack_confirm_2)
    if stack_confirm_2 == 1:
        print( "\nVery Good! It may take me more than 1 guess, but I think I can guess your card!")
        print("\nIs This Your Card?"  )
        print(group_2a[3])
        card_confirm_3 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
        card_confirm_3 = int(card_confirm_3)
        if card_confirm_3 == 1:
            print("\nGreat!  Thanks For Playing Python Magic Cards! ")
        if card_confirm_3 == 2:
            print( "\nOoops!  Is This Your Card?"  )
            print(group_2a[4])
            card_confirm_4 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_4 = int(card_confirm_4)
            if card_confirm_4 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_4 == 2:
                print( "\nOoops Again!  Is This Your Card?"  )
                print(group_2a[2])
                card_confirm_5 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_5 = int(card_confirm_5)
                if card_confirm_5 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                elif card_confirm_5 == 2:
                    print("\nSorry! I FAILED!")
                else:
                    print("\n Wrong Input")
    if stack_confirm_2 == 2:
        print( "\nOoops! Your Card is Not In Stack 2! Let's Check Stack 1! "  )
        for card in group_1a:
            print(card, end=' ')
        stack_confirm_3 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
        stack_confirm_3 = int(stack_confirm_3)
        if stack_confirm_3 == 1:
            print( "\nVery Good! I think I can guess your card!")
            print("\nIs This Your Card?"  )
            print(group_1a[3])
            card_confirm_6 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_6 = int(card_confirm_6)
            if card_confirm_6 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_6 == 2:
                print( "\nOoops!  Is This Your Card?"  )
                print(group_1a[4])
                card_confirm_7 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_7 = int(card_confirm_7)
                if card_confirm_7 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                elif card_confirm_7 == 2:
                    print("\nSorry! I FAILED!")
            else:
                print("\nWrong Input!")
        else:
            print("\nWrong Input Or Your Card Must Have Disappeared!")
    else:
        print("\n ")


#
#
#


if stack_confirm_1 == 1 and stack_pick_2 == 2 and stack_pick_1 == 1:
    print( "\nVery Good Guess! It may take a few guesses, but I think I can guess your card!")
    print("\nIs This Your Card?"  )
    print(group_2a[3])
    card_confirm_1 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
    card_confirm_1 = int(card_confirm_1)
    if card_confirm_1 == 1:
        print("\nGreat!  Thanks For Playing Python Magic Cards! ")
    if card_confirm_1 == 2:
        print( "\nIs This Your Card? "  )
        print(group_2a[2])
        card_confirm_2 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2):"  )
        card_confirm_2 = int(card_confirm_2)
        if card_confirm_2 == 1:
            print( "\nThank You For Playing Python Magic Card Game!"  )
        elif card_confirm_2 == 2:
            print( "\nIs This Your Card? "  )
            print(group_2a[4])
            card_confirm_3 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2):"  )
            card_confirm_3 = int(card_confirm_3)
            if card_confirm_3 == 1:
                print( "\nThank You For Playing Python Magic Card Game!"  )
            else: print("\nWrong Input E or Maybe Your Card Disappeared!?")
        else:
            print("\nWrong Input A - Maybe Your Card Disappeared!?")
    else:
        print("\naaaaaaaa")


if stack_confirm_1 == 2 and stack_pick_2 == 2 and stack_pick_1 == 1:
    print( "\nOoops! Your Card is Not In Stack 2! Let's Check Stack 1! "  )
    for card in group_1a:
        print(card, end=' ')
    stack_confirm_2 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
    stack_confirm_2 = int(stack_confirm_2)
    if stack_confirm_2 == 1:
        print( "\nVery Good! I think I can guess your card!")
        print("\nIs This Your Card?"  )
        print(group_1a[3])
        card_confirm_3 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
        card_confirm_3 = int(card_confirm_3)
        if card_confirm_3 == 1:
            print("\nGreat!  Thanks For Playing Python Magic Cards! ")
        if card_confirm_3 == 2:
            print( "\nOoops!  Is This Your Card?"  )
            print(group_1a[4])
            card_confirm_4 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_4 = int(card_confirm_4)
            if card_confirm_4 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_4 == 2:
                print( "\nOoops Again!  Maybe Your Card Disappeared?"  )
        else:
            print("\nWrong Input B")


    if stack_confirm_2 == 2:
        print( "\nOoops! Your Card is Not In Stack 1! Let's Check Stack 3! "  )
        for card in group_3a:
            print(card, end=' ')
        stack_confirm_3 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
        stack_confirm_3 = int(stack_confirm_3)
        if stack_confirm_3 == 1:
            print( "\nVery Good! I think I can guess your card!")
            print("\nIs This Your Card?"  )
            print(group_3a[3])
            card_confirm_6 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_6 = int(card_confirm_6)
            if card_confirm_6 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_6 == 2:
                print( "\nOoops!  Is This Your Card?"  )
                print(group_3a[2])
                card_confirm_7 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_7 = int(card_confirm_7)
                if card_confirm_7 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                elif card_confirm_7 == 2:
                    print("\nSorry! I FAILED! Maybe Your Card Disappeared in the Computer!")
                else:
                    print("Wrong Input! D")
            else:
                print("\nWrong Input! C")
        else:
            print("\nWrong Input Or Your Card Must Have Disappeared!")
    else:
        print("\n ")


#
#
#


if stack_confirm_1 == 1 and stack_pick_2 == 3 and stack_pick_1 == 1:
    print( "\nVery Good Guess! I think I can guess your card!")
    print("\nIs This Your Card?"  )
    print(group_3a[3])
    card_confirm_1 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
    card_confirm_1 = int(card_confirm_1)
    if card_confirm_1 == 1:
        print("\nGreat!  Thanks For Playing Python Magic Cards! ")
    else:
        print( "\nIs This Your Card? "  )
        print(group_3a[2])
        card_confirm_2 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2):"  )
        card_confirm_2 = int(card_confirm_2)
        print( "\nThank You For Playing Python Magic Card Game!"  )

if stack_confirm_1 == 2 and stack_pick_2 == 3 and stack_pick_1 == 1:
    print( "\nOoops! Your Card is Not In Stack 3! Let's Check Stack 2! "  )
    for card in group_2a:
        print(card, end=' ')
    stack_confirm_2 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
    stack_confirm_2 = int(stack_confirm_2)
    if stack_confirm_2 == 1:
        print( "\nVery Good! It may take me more than 1 guess, but I think I can guess your card!")
        print("\nIs This Your Card?"  )
        print(group_2a[3])
        card_confirm_3 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
        card_confirm_3 = int(card_confirm_3)
        if card_confirm_3 == 1:
            print("\nGreat!  Thanks For Playing Python Magic Cards! ")
        if card_confirm_3 == 2:
            print( "\nOoops!  Is This Your Card?"  )
            print(group_2a[4])
            card_confirm_4 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_4 = int(card_confirm_4)
            if card_confirm_4 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_4 == 2:
                print( "\nOoops Again!  Is This Your Card?"  )
                print(group_2a[2])
                card_confirm_5 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_5 = int(card_confirm_5)
                if card_confirm_5 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                elif card_confirm_5 == 2:
                    print("\nSorry! I FAILED!")
                else:
                    print("\n Wrong Input")
    if stack_confirm_2 == 2:
        print( "\nOoops! Your Card is Not In Stack 2! Let's Check Stack 1! "  )
        for card in group_1a:
            print(card, end=' ')
        stack_confirm_3 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
        stack_confirm_3 = int(stack_confirm_3)
        if stack_confirm_3 == 1:
            print( "\nVery Good! I think I can guess your card!")
            print("\nIs This Your Card?"  )
            print(group_1a[3])
            card_confirm_6 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_6 = int(card_confirm_6)
            if card_confirm_6 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_6 == 2:
                print( "\nOoops!  Is This Your Card?"  )
                print(group_1a[4])
                card_confirm_7 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_7 = int(card_confirm_7)
                if card_confirm_7 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                elif card_confirm_7 == 2:
                    print("\nSorry! I FAILED!")
            else:
                print("\nWrong Input!")
        else:
            print("\nWrong Input Or Your Card Must Have Disappeared!")
    else:
        print("\n ")

#
#
#




if stack_confirm_1 == 1 and stack_pick_2 == 1 and stack_pick_1 == 2:
    print( "\nVery Good Guess! I think I can guess your card!")
    print("\nIs This Your Card?"  )
    print(group_1a[4])
    card_confirm_1 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
    card_confirm_1 = int(card_confirm_1)
    if card_confirm_1 == 1:
        print("\nGreat!  Thanks For Playing Python Magic Cards! ")
    else:
        print( "\nIs This Your Card? "  )
        print(group_1a[3])
        card_confirm_2 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2):"  )
        card_confirm_2 = int(card_confirm_2)
        print( "\nThank You For Playing Python Magic Card Game!"  )

if stack_confirm_1 == 2 and stack_pick_2 == 1 and stack_pick_1 == 2:
    print( "\nOoops! Your Card is Not In Stack 1! Let's Check Stack 2! "  )
    for card in group_2a:
        print(card, end=' ')
    stack_confirm_2 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
    stack_confirm_2 = int(stack_confirm_2)
    if stack_confirm_2 == 1:
        print( "\nVery Good! It may take me more than 1 guess, but I think I can guess your card!")
        print("\nIs This Your Card?"  )
        print(group_2a[3])
        card_confirm_3 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
        card_confirm_3 = int(card_confirm_3)
        if card_confirm_3 == 1:
            print("\nGreat!  Thanks For Playing Python Magic Cards! ")
        if card_confirm_3 == 2:
            print( "\nOoops!  Is This Your Card?"  )
            print(group_2a[4])
            card_confirm_4 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_4 = int(card_confirm_4)
            if card_confirm_4 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_4 == 2:
                print( "\nOoops Again!  Is This Your Card?"  )
                print(group_2a[2])
                card_confirm_5 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_5 = int(card_confirm_5)
                if card_confirm_5 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                if card_confirm_5 == 2:
                    print("\nSorry! I FAILED!")
                else:
                    print("\n ")
    if stack_confirm_2 == 2:
        print( "\nOoops! Your Card is Not In Stack 2! Let's Check Stack 3! "  )
        for card in group_3a:
            print(card, end=' ')
        stack_confirm_3 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
        stack_confirm_3 = int(stack_confirm_3)
        if stack_confirm_3 == 1:
            print( "\nVery Good! I think I can guess your card!")
            print("\nIs This Your Card?"  )
            print(group_3a[3])
            card_confirm_6 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_6 = int(card_confirm_6)
            if card_confirm_6 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_6 == 2:
                print( "\nOoops!  Is This Your Card?"  )
                print(group_3a[2])
                card_confirm_7 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_7 = int(card_confirm_7)
                if card_confirm_7 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                if card_confirm_7 == 2:
                    print("\nSorry! I FAILED!")
            else:
                print("\nWrong Input!")
        else:
            print("\nWrong Input Or Your Card Must Have Disappeared!")
    else:
        print("\n  ")

#
#
#

if stack_confirm_1 == 1 and stack_pick_2 == 3 and stack_pick_1 == 2:
    print( "\nVery Good Guess! I think I can guess your card!")
    print("\nIs This Your Card?"  )
    print(group_3a[3])
    card_confirm_1 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
    card_confirm_1 = int(card_confirm_1)
    if card_confirm_1 == 1:
        print("\nGreat!  Thanks For Playing Python Magic Cards! ")
    else:
        print( "\nIs This Your Card? "  )
        print(group_3a[2])
        card_confirm_2 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2):"  )
        card_confirm_2 = int(card_confirm_2)
        print( "\nThank You For Playing Python Magic Card Game!"  )

if stack_confirm_1 == 2 and stack_pick_2 == 3 and stack_pick_1 == 2:
    print( "\nOoops! Your Card is Not In Stack 3! Let's Check Stack 2! "  )
    for card in group_2a:
        print(card, end=' ')
    stack_confirm_2 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
    stack_confirm_2 = int(stack_confirm_2)
    if stack_confirm_2 == 1:
        print( "\nVery Good! It may take me more than 1 guess, but I think I can guess your card!")
        print("\nIs This Your Card?"  )
        print(group_2a[3])
        card_confirm_3 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
        card_confirm_3 = int(card_confirm_3)
        if card_confirm_3 == 1:
            print("\nGreat!  Thanks For Playing Python Magic Cards! ")
        if card_confirm_3 == 2:
            print( "\nOoops!  Is This Your Card?"  )
            print(group_2a[4])
            card_confirm_4 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_4 = int(card_confirm_4)
            if card_confirm_4 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_4 == 2:
                print( "\nOoops Again!  Is This Your Card?"  )
                print(group_2a[2])
                card_confirm_5 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_5 = int(card_confirm_5)
                if card_confirm_5 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                elif card_confirm_5 == 2:
                    print("\nSorry! I FAILED!")
                else:
                    print("\n Wrong Input")
    if stack_confirm_2 == 2:
        print( "\nOoops! Your Card is Not In Stack 2! Let's Check Stack 1! "  )
        for card in group_1a:
            print(card, end=' ')
        stack_confirm_3 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
        stack_confirm_3 = int(stack_confirm_3)
        if stack_confirm_3 == 1:
            print( "\nVery Good! I think I can guess your card!")
            print("\nIs This Your Card?"  )
            print(group_1a[3])
            card_confirm_6 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_6 = int(card_confirm_6)
            if card_confirm_6 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_6 == 2:
                print( "\nOoops!  Is This Your Card?"  )
                print(group_1a[4])
                card_confirm_7 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_7 = int(card_confirm_7)
                if card_confirm_7 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                elif card_confirm_7 == 2:
                    print("\nSorry! I FAILED!")
            else:
                print("\nWrong Input!")
        else:
            print("\nWrong Input Or Your Card Must Have Disappeared!")
    else:
        print("\n  ")

#
#
#

if stack_confirm_1 == 1 and stack_pick_2 == 1 and stack_pick_1 == 3:
    print( "\nVery Good Guess! I think I can guess your card!")
    print("\nIs This Your Card?"  )
    print(group_1a[4])
    card_confirm_1 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
    card_confirm_1 = int(card_confirm_1)
    if card_confirm_1 == 1:
        print("\nGreat!  Thanks For Playing Python Magic Cards! ")
    else:
        print( "\nIs This Your Card? "  )
        print(group_1a[3])
        card_confirm_2 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2):"  )
        card_confirm_2 = int(card_confirm_2)
        print( "\nThank You For Playing Python Magic Card Game!"  )

if stack_confirm_1 == 2 and stack_pick_2 == 1 and stack_pick_1 == 3:
    print( "\nOoops! Your Card is Not In Stack 1! Let's Check Stack 2! "  )
    for card in group_2a:
        print(card, end=' ')
    stack_confirm_2 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
    stack_confirm_2 = int(stack_confirm_2)
    if stack_confirm_2 == 1:
        print( "\nVery Good! It may take me more than 1 guess, but I think I can guess your card!")
        print("\nIs This Your Card?"  )
        print(group_2a[3])
        card_confirm_3 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
        card_confirm_3 = int(card_confirm_3)
        if card_confirm_3 == 1:
            print("\nGreat!  Thanks For Playing Python Magic Cards! ")
        if card_confirm_3 == 2:
            print( "\nOoops!  Is This Your Card?"  )
            print(group_2a[4])
            card_confirm_4 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_4 = int(card_confirm_4)
            if card_confirm_4 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_4 == 2:
                print( "\nOoops Again!  Is This Your Card?"  )
                print(group_2a[2])
                card_confirm_5 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_5 = int(card_confirm_5)
                if card_confirm_5 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                if card_confirm_5 == 2:
                    print("\nSorry! I FAILED!")
                else:
                    print("\n Wrong Input")
    if stack_confirm_2 == 2:
        print( "\nOoops! Your Card is Not In Stack 2! Let's Check Stack 3! "  )
        for card in group_3a:
            print(card, end=' ')
        stack_confirm_3 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
        stack_confirm_3 = int(stack_confirm_3)
        if stack_confirm_3 == 1:
            print( "\nVery Good! I think I can guess your card!")
            print("\nIs This Your Card?"  )
            print(group_3a[3])
            card_confirm_6 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_6 = int(card_confirm_6)
            if card_confirm_6 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_6 == 2:
                print( "\nOoops!  Is This Your Card?"  )
                print(group_3a[2])
                card_confirm_7 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_7 = int(card_confirm_7)
                if card_confirm_7 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                if card_confirm_7 == 2:
                    print("\nSorry! I FAILED!")
            else:
                print("\nWrong Input!")
        else:
            print("\nWrong Input Or Your Card Must Have Disappeared!")
    else:
        print("\nWrong Input!")


#
#
#
#


if stack_confirm_1 == 1 and stack_pick_2 == 2 and stack_pick_1 == 3:
    print( "\nVery Good Guess! It may take a few guesses, but I think I can guess your card!")
    print("\nIs This Your Card?"  )
    print(group_2a[3])
    card_confirm_1 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
    card_confirm_1 = int(card_confirm_1)
    if card_confirm_1 == 1:
        print("\nGreat!  Thanks For Playing Python Magic Cards! ")
    if card_confirm_1 == 2:
        print( "\nIs This Your Card? "  )
        print(group_2a[2])
        card_confirm_2 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2):"  )
        card_confirm_2 = int(card_confirm_2)
        if card_confirm_2 == 1:
            print( "\nThank You For Playing Python Magic Card Game!"  )
        elif card_confirm_2 == 2:
            print( "\nIs This Your Card? "  )
            print(group_2a[4])
            card_confirm_3 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2):"  )
            card_confirm_3 = int(card_confirm_3)
            if card_confirm_3 == 1:
                print( "\nThank You For Playing Python Magic Card Game!"  )
            else: print("\nWrong Input E or Maybe Your Card Disappeared!?")
        else:
            print("\nWrong Input A - Maybe Your Card Disappeared!?")
    else:
        print("\naaaaaaaa")


if stack_confirm_1 == 2 and stack_pick_2 == 2 and stack_pick_1 == 3:
    print( "\nOoops! Your Card is Not In Stack 2! Let's Check Stack 1! "  )
    for card in group_1a:
        print(card, end=' ')
    stack_confirm_2 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
    stack_confirm_2 = int(stack_confirm_2)
    if stack_confirm_2 == 1:
        print( "\nVery Good! I think I can guess your card!")
        print("\nIs This Your Card?"  )
        print(group_1a[3])
        card_confirm_3 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
        card_confirm_3 = int(card_confirm_3)
        if card_confirm_3 == 1:
            print("\nGreat!  Thanks For Playing Python Magic Cards! ")
        if card_confirm_3 == 2:
            print( "\nOoops!  Is This Your Card?"  )
            print(group_1a[4])
            card_confirm_4 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_4 = int(card_confirm_4)
            if card_confirm_4 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_4 == 2:
                print( "\nOoops Again!  Maybe Your Card Disappeared?"  )
        else:
            print("\nWrong Input B")


    if stack_confirm_2 == 2:
        print( "\nOoops! Your Card is Not In Stack 1! Let's Check Stack 3! "  )
        for card in group_3a:
            print(card, end=' ')
        stack_confirm_3 = input( "\nDo You See Your Card In This Group? 1 for Yes or 2 for No: (1 or 2): "  )
        stack_confirm_3 = int(stack_confirm_3)
        if stack_confirm_3 == 1:
            print( "\nVery Good! I think I can guess your card!")
            print("\nIs This Your Card?"  )
            print(group_3a[3])
            card_confirm_6 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
            card_confirm_6 = int(card_confirm_6)
            if card_confirm_6 == 1:
                print("\nGreat!  Thanks For Playing Python Magic Cards! ")
            if card_confirm_6 == 2:
                print( "\nOoops!  Is This Your Card?"  )
                print(group_3a[2])
                card_confirm_7 = input( "\nPlease Choose 1: for Yes or 2: for No (1 or 2): "  )
                card_confirm_7 = int(card_confirm_7)
                if card_confirm_7 == 1:
                    print("\nGreat!  Thanks For Playing Python Magic Cards! ")
                elif card_confirm_7 == 2:
                    print("\nSorry! I FAILED! Maybe Your Card Disappeared in the Computer!")
                else:
                    print("Wrong Input! D")
            else:
                print("\nWrong Input! C")
        else:
            print("\nWrong Input Or Your Card Must Have Disappeared!")
    else:
        print("\n ")







else:
    print(" ")
