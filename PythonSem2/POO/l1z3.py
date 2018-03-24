blotki = ['1','2','3','4','5','6','7','8','9','10']
figury = ['11','12','13','14'] #Jopek dama krol as
color = ["♠","♥","♦","♣"]
 


#////////////////////////////////////////////////////////////////////////////
import random
def randChoice(cardChoice):
    randomcards = []

    for i in range(5):
        while(True):
            temp =  random.choice(cardChoice) + " " + random.choice(color)
            if(randomcards.count(temp) == 0):
                randomcards.append(temp)
                break
        
    return randomcards

temp = randChoice(blotki)
print(randChoice(figury))
print(randChoice(blotki))


#/////////////////////////////////////////////////////////////////////////////
import re
def checkHand(hand):
    temp = 0
    #Poker/flush
    if (check_flush(hand)):
        if(check_straight(hand)):
            return 9
        temp = 6
    #Straight
    if(check_straight(hand)):
        if(temp<5): temp = 5
    #Multiple
    temp2 = check_multiple(hand)
    if(temp>temp2):
        return temp
    return temp2

def check_flush(hand):
    suits = [h.split()[1] for h in hand]
    if len(set(suits)) == 1:
      return True
    else:
      return False

def check_straight (hand):
    cards = [int(h.split()[0]) for h in hand]
    cards.sort()
    for i in range(1,5):
        if (cards[i] - cards[i-1] != 1):
            return False
    return True

def check_multiple (hand):
    cards = [int(h.split()[0]) for h in hand]
    types = set(cards)
    cardCount = []
    for card in types:
        cardCount.append(cards.count(card))
    length = len(cardCount)
    if(length == 5):
        return 1
    if(length == 4):
        return 2
    if(length == 3):
        if(cardCount.count(2)==2):
            return 3
        return 4
    if(length == 2):
        if(cardCount.count(2)==1):
            return 7
        return 8
count = 0
total = 10000
for i in range(total):
    blot = checkHand(randChoice(blotki))
    figu = checkHand(randChoice(figury))
    if(blot>1 and blot > figu):
        count += 1
print(count/total)
