# creating a card game 

# card class deck class player class game logic


from random import shuffle

suits = ('Diamonds','Spades','Hearts','Clubs')
ranks = ('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')
values = {
    'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,
    'ten':10,'jack':11,'queen':12,'king':13,'ace':14
}

class card:

    def __init__(self,suit,rank) :

        self.suit = suit
        self.rank = rank
        self.value= values[rank]

    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'



class deck:

    def __init__(self) -> None:
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                
                created_card = card(suit,rank)
                self.all_cards.append( created_card )



    def shuffle_cards(self):

        shuffle(self.all_cards)

    def play_one_card(self):

        return self.all_cards.pop()





class player:

    def __init__(self,name) -> None:
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self) -> str:
        return f"player  {self.name} has {len(self.all_cards)} cards"





player_one = player('One')
player_two = player('Two')

new_deck = deck()
new_deck.shuffle_cards()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())



round_num = 0
war_count = 0

game_on = True
while game_on :
    pass