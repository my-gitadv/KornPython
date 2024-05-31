# KornPython


hand = []
def toNum(z):
    if z == 'A':
        return '1'
    elif z == '1':
        return '10'
    elif z == 'J':
        return '11'
    elif z == 'Q':
        return '12'
    else:
        return '13'

def draw():
    try:
        top = deck.pop(-1)
    except: 
        print("No card left")
    else:
        for i in range(len(hand)):
            x = hand[i][0]
            y = top[0]

            if x in ['1','A','J','Q','K']:
                x = toNum(x)
            if y in ['1','A','J','Q','K']:
                y = toNum(y)
            
            if int(x) >= int(y):
                hand.insert(i,top)
                print("Top =", top)
                break
        else:
            hand.append(top)

        print("Number of remaining cards =", len(deck))
        return top
