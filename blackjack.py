import sys, random


#unicode characters for card suits
HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)


def get_deck():
    """
    generates the deck of 52 cards
    returns list of tuples, each containing a card value and suit
    """

    deck = []

    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for card in range(2,11):
            deck.append((str(card), suit))
        for card in ("J", "Q", "K", "A"):
            deck.append((card, suit))

    random.shuffle(deck)
    return deck


def get_bet(max_bet):
    """
    max_bet: int, the maximum amount the player can bet

    checks to make sure bet is valid and return player's bet as an int
    """

    while True:
        print("------")
        bet = input(f"Place your bet (1-{max_bet}) or type 'QUIT': ")
        bet = bet.lower().strip()

        if bet == "quit":
            sys.exit()
        else:
            try:
                bet = int(bet)
            except ValueError:
                print("Invalid bet!")
            else:
                if 1 <= bet <= max_bet:
                    break
                else:
                    print("Invalid bet!")            
    
    return bet


def get_hand_value(cards):
    """
    cards: list of tuples (rank + suit) representing cards currently in the hand

    returns total value of cards
    also pick best option for variable cards (ace 1 or 11)
    """

    value = 0
    aces = 0

    for card in cards:
        rank = card[0]
        if rank == "A":
            aces += 1
        elif rank in ("K", "Q", "J"):
            value += 10
        else:
            value += int(rank)

    value += aces
    for i in range(aces):
        if value + 10 <= 21:
            value += 10

    return value


def display_cards(cards):
    """
    cards: list of tuples (rank + suit) representing cards currentlly in the hand

    prints a visual display of the cards given to the function
    """

    rows = ["", "", "", "", ""]

    for card in cards:
        rows[0] += " ___  "
        if card == "backside":
            rows[1] += "|## | "
            rows[2] += "|###| "
            rows[3] += "|_##| "
        else:
            rank, suit = card
            rows[1] += f"|{rank.ljust(2)} | "
            rows[2] += f"| {suit} | "
            rows[3] += f"|_{rank.rjust(2, '_')}| "

    for row in rows:
        print(row)


def display_hands(dealer, player, show_dealer):
    """
    dealer: list of tuples, representing dealer's current hand
    player: list of tuples, representing player's current hand
    show_dealer: bool, whether or not to hide dealer's hand

    shows value and representation of current hands
    """

    print("------")
    if show_dealer:
        print("DEALER: ", get_hand_value(dealer))
        display_cards(dealer)

    else:
        print("DEALER: ???")
        display_cards(["backside"] + dealer[1:])

    print("PLAYER: ", get_hand_value(player))
    display_cards(player)


def choose_move():
    """
    returns selected move (H for hit, or S for stand)
    """

    while True:
        print("------")
        move = input("Would you like to (H)it or (S)tand?: ").lower()
        
        if move in ("h", "s"):
            return move
        else:
            print("Invalid move!")


def main():
    """
    Main game loop
    Player and dealer receive an initial hand of 2 cards each
    Player is able to make bets and hit or stand in each round
    Dealer hits on less than 17
    """

    money = 5000

    print("Welcome to Blackjack! Try to get to 21 without going over!")

    #handle player's actions
    while True:
        if money <= 0:
            print("You're out of money!")
            print("Thanks for playing!")
            sys.exit()

        print("------")
        print(f"Available money: {money}")
        bet = get_bet(money)

        #generate and shuffle deck, deal starting hands
        deck = get_deck() 
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        while True:
            display_hands(dealer_hand, player_hand, False)

            if get_hand_value(player_hand) > 21:
                break

            move = choose_move()
            if move == "s":
                break
            elif move == "h":
                player_hand.append(deck.pop())

        #handle dealer's actions
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17:
                print("Dealer hits...")
                dealer_hand.append(deck.pop())
                display_hands(dealer_hand, player_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break
            
        input("Press Enter to continue...")

        display_hands(dealer_hand, player_hand, True)

        player_score = get_hand_value(player_hand)
        dealer_score = get_hand_value(dealer_hand)

        if dealer_score > 21:
            print(f"Dealer busts! You win ${bet}!")
            money += bet
        elif (player_score > 21) or (player_score < dealer_score):
            print("You lost!")
            money -= bet
        elif player_score > dealer_score:
            print(f"You won ${bet}!")
            money += bet
        elif player_score == dealer_score:
            print("It's a tie!")

        input("Press Enter to continue...")
        print()


if __name__ == "__main__":
    main()


