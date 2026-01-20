import random

def shuffle_deck() -> list[str]:
    """Randomises a given deck of cards.
 
    Args:
        N/A
 
    Returns:
        list[str]: with each 'card' in the deck being positionally random.
 
    Raises:
        N/A
 
    Examples:
        >>> shuffle_deck()
        8 of Hearts   2 of Clubs   4 of Diamonds   8 of Diamonds   5 of Hearts   

        Jack of Diamonds   King of Clubs   Queen of Diamonds   6 of Diamonds   8 of Clubs   

        5 of Diamonds   King of Hearts   Jack of Clubs   10 of Spades   Queen of Spades   

        3 of Hearts   5 of Spades   7 of Spades   2 of Diamonds   7 of Diamonds   

        2 of Spades   8 of Spades   4 of Hearts   7 of Clubs   10 of Clubs   

        2 of Hearts   9 of Clubs   Jack of Spades   3 of Clubs   Ace of Clubs   

        Ace of Diamonds   6 of Clubs   Jack of Hearts   10 of Hearts   King of Diamonds   

        9 of Spades   Ace of Hearts   4 of Clubs   6 of Spades   4 of Spades

        10 of Diamonds   3 of Diamonds   3 of Spades   9 of Hearts   7 of Hearts

        9 of Diamonds   King of Spades   5 of Clubs   Queen of Hearts   Ace of Spades

        6 of Hearts   Queen of Clubs
    """

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    nums = ["Queen", "King", "Jack", "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10]
    deck = []

    for suit in suits:
        for num in nums:
            card = str(str(num) + " of " + suit)
            deck.append(card)
    
    #The randonmisation utilises the Fisher-Yates algorithm, created in 1938, and made machine usable
    #in 1964. The source can be found in the link below:
    #Wikipedia. (2022). Fisher. [online] Available at: https://en.wikipedia.org/wiki/Fisher–Yates_shuffle
    
    for x in range(len(deck) - 1, 0, -1):
        
        random_card = random.randint(0, x)
        deck[x], deck[random_card] = deck[random_card], deck[x]
    
    return deck