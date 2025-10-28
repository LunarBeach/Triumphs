#defining card class

class Card:
    def __init__(self, rank, trick_power, suit, score_value, name=None): 
        self.rank = rank
        self.trick_power = trick_power
        self.suit = suit
        self.score_value = score_value
        self.name = None or (rank if suit =='trump' else f'{rank} of {suit}')

    def __repr__(self):
        return self.name
    
# define minor arcana suits

suits = ('Batons', 'Cups', 'Swords', 'Coins')

# define face card ranks

faces = ('Page', 'Knight', 'Queen', 'King')

# define major arcana 

trumps = [
    'The Magician',
    'The Popess',
    'The Empress',
    'The Emperor',
    'The Pope',
    'The Lovers',
    'The Chariot',
    'Justice',
    'The Hermit',
    'The Wheel of Fortune',
    'Fortitude',
    'The Hanged Man',
    'Death',
    'Temperance',
    'The Devil',
    'The Tower',
    'The Star',
    'The Moon',
    'The Sun',
    'Judgement',
    'The World',
    'The Fool'
]

import random

# dictionaries for storing a cards scoring value based on whether it is pip, face, or trump 

pip_score = {i: 1 for i in range(1, 11)}
face_score = {'Page':2, 'Knight':3, 'Queen':4, 'King':5}
trump_score = {
    'The Magician':4,
    'The Popess':0,
    'The Empress':0,
    'The Emperor':0,
    'The Pope':0,
    'The Lovers':0,
    'The Chariot':0,
    'Justice':0,
    'The Hermit':0,
    'The Wheel of Fortune':0,
    'Fortitude':0,
    'The Hanged Man':0,
    'Death':0,
    'Temperance':0,
    'The Devil':0,
    'The Tower':0,
    'The Star':0,
    'The Moon':0,
    'The Sun':0,
    'Judgement':0,
    'The World':4,
    'The Fool':4
}

# dictionaries for assigning the cards ranks 
pip_ranks = {i: i for i in range(1,11)}
face_trick_power = {'Page':11, 'Knight':12, 'Queen':13, 'King':14}

# creating the cards and adding them into an ordered list 

# build pip cards 

def create_pip_cards():
    cards = []
    for suit in suits:
        for rank in range(1,11):
            cards.append(
                Card(
                    rank= rank,
                    trick_power=rank,
                    suit=suit,
                    score_value = 1
                )
            )
    return cards 

# create a tuple for the pip cards 

pip_cards = tuple(create_pip_cards())

# build face cards 

def create_face_cards():
    cards = []
    for suit in suits:
        for face in faces:
            cards.append(
                Card(
                    rank= face,
                    trick_power=face_trick_power[face],
                    suit=suit,
                    score_value=face_score[face],
                )
            )
    return cards

# build the trump cards

def create_trump_cards():
    cards = []
    for index, trump in enumerate(trumps):
        trick_power = index +14
        cards.append(
            Card(
                rank=trump,
                trick_power=trick_power,
                suit='trump',
                score_value=trump_score[trump]
            )
        )
    return cards



from add_bonus_cards import get_bonus_cards

# function to combine the pip, face, trumps, and any bonus cards into a deck 

def build_deck() -> list:
    Deck = []
    Deck.extend(create_pip_cards())
    Deck.extend(create_face_cards())
    Deck.extend(create_trump_cards())
    Deck.extend(get_bonus_cards())
    return Deck


# the game_deck is declared here as a new list containing new_deck, essentially a copy, but the game deck will go on to be shuffled, and have cards added or removed from it as they are dealt. 
# For example, prior to the cards being dealt the game_deck will get the Bonus cards randomly added into it for instant win prizes 
game_deck = build_deck()

# function to shuffle the game deck
def shuffle_deck(deck: list) -> list:
    random.shuffle(deck)
    return deck

# shuffle the game deck
game_deck = shuffle_deck(game_deck)
