# Game actions


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet? "))
        except:
            print("sorry please provide an integer")
        else:
            if chips.bet > chips.total:
                print("sorry your bet can't exceed {} ".format(chips.total))
            else:
                break


def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_aces()

def hit_or_stand(deck, hand):
    global playing

    while True:
        x = input('Hit or Stand? Enter h or s ')

        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("player stands, dealer's turn")
            playing = False
        else:
            print("sorry, I did not understand that")
            continue
        break


# Display Cards

def show_some(player,dealer):

    print('dealer hand: ')
    print('one card hidden')
    print(dealer.cards[1])
    print('\n')
    print('players hand: ')
    for card in player.cards:
        print(card)

def show_all(player, dealer):

    print('dealer hand: ')
    for card in dealer.cards:
        print(card)
    print('\n')
    print('player hand: ')
    for card in player.cards:
        print(card)

# Game outcomes

def player_busts(player, dealer, chips):
    print("bust player")

def player_wins(player,dealer,chips):
    print("player wins")

def dealer_busts(player,dealer,chips):
    print('player wins')

def dealer_wins(player,dealer,chips):
    print('dealer wins')

def push(player,dealer):
    print('tie')

