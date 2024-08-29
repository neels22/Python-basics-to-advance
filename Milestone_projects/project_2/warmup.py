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

    def deal_one(self):

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



import pdb
game_on = True
round_num = 0
while game_on:
    
    round_num += 1
    print(f"Round {round_num}")
    
    # Check to see if a player is out of cards:
    if len(player_one.all_cards) == 0:
        print("Player One out of cards! Game Over")
        print("Player Two Wins!")
        game_on = False
        break
        
    if len(player_two.all_cards) == 0:
        print("Player Two out of cards! Game Over")
        print("Player One Wins!")
        game_on = False
        break
    
    # Otherwise, the game is still on!
    
    # Start a new round and reset current cards "on the table"
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    at_war = True
    while at_war:


        if player_one_cards[-1].value > player_two_cards[-1].value:

            # Player One gets the cards
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            
            
            # No Longer at "war" , time for next round
            at_war = False
        
        # Player Two Has higher Card
        elif player_one_cards[-1].value < player_two_cards[-1].value:

            # Player Two gets the cards
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)
            
            # No Longer at "war" , time for next round
            at_war = False

        else:
            print('WAR!')
            # This occurs when the cards are equal.
            # We'll grab another card each and continue the current war.
            
            # First check to see if player has enough cards
            
            # Check to see if a player is out of cards:
            if len(player_one.all_cards) < 5:
                print("Player One unable to play war! Game Over at War")
                print("Player Two Wins! Player One Loses!")
                game_on = False
                break

            elif len(player_two.all_cards) < 5:
                print("Player Two unable to play war! Game Over at War")
                print("Player One Wins! Player One Loses!")
                game_on = False
                break
            # Otherwise, we're still at war, so we'll add the next cards
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())