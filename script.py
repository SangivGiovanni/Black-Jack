from DeckClass import Deck
from HandClass import Hand

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
         'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True
first = True

while True:

    print('Welcome to BlackJack')

    # Set the hands and deck
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Set player chips
    from ChipsClass import Chips

    if first:
        player_chips = Chips()
    else:
        pass

    # prompt player to make bet
    from GameplayFunctions import take_bet
    from GameplayFunctions import hit
    from GameplayFunctions import show_all
    from GameplayFunctions import show_some
    from GameplayFunctions import player_busts
    from GameplayFunctions import player_wins
    from GameplayFunctions import dealer_busts
    from GameplayFunctions import dealer_wins
    from GameplayFunctions import push

    take_bet(player_chips)

    # show cards but keep one dealer card hidden
    show_some(player_hand, dealer_hand)

    while playing:

        # promt player to hit or stand
        while True:
            x = input('Hit or Stand? Enter h or s ')

            if x[0].lower() == 'h':
                hit(deck, player_hand)
            elif x[0].lower() == 's':
                print("player stands, dealer's turn")
                playing = False
            else:
                print("sorry, I did not understand that")
                continue
            break
        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            player_chips.lose_bet()
            playing = False

    # If player hasnt busted, play dealer hand until dealer hand is greater than player hand
    if player_hand.value <= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        # different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
            player_chips.win_bet()
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
            player_chips.lose_bet()
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
            player_chips.win_bet()
        else:
            push(player_hand, dealer_hand)

    # inform player of chips total
    print('\n Player total chips are: {}'.format(player_chips.total))
    first = False

    if player_chips.total == 0:
        print('Game Over')
        break
    else:
        pass

    # Ask to play again
    new_game = input("Would you like to play again?")

    if new_game[0].lower() == 'y':
        playing = True
    else:
        print('Thank you for playing!')
        break
