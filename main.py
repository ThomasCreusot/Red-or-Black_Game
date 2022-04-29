from unicodedata import name
import random

DEFAULT_PANACHE_FACTOR = 2
POINTS_ROUND_1 = 1
POINTS_ROUND_2 = 2
POINTS_ROUND_3 = 3
POINTS_ROUND_4 = 4

COLORS_STCC = ("Spade", "Club", "Heart", "Diamond")
RANKS = (1,2,3,4,5,6,7,8,9,10,11,12,13)

deck_of_cards = []
players = []

colors_stcc_to_colors_RBG_correspondance = {
    "Spade" : "Black",
    "Club" : "Black",
    "Heart" : "Red",
    "Diamond": "Red"
}

rank_to_values_correspondance = {
    1 : "Ace",
    2 : "2",
    3 : "3",
    4 : "4",
    5 : "5",
    6 : "6",
    7 : "7",
    8 : "8",
    9 : "9",
    10 : "10",
    11 : "Jack",
    12 : "Queen",
    13 : "King"
}


class Cards:
    """Reprensents a card of the game"""

    def __init__(self, color_stcc, color_rgb, rank, value) -> None:
        self.color_stcc = color_stcc
        self.color_rgb = color_rgb
        self.rank = rank
        self.value = value


class Player:
    """Represents a player"""

    def __init__(self, name) -> None:
        """Initialization of details related to the player"""
        self.name = name
        self.points = 0
        self.hand = []

    def pick_a_card(self):
        """The player picks a card in the deck of card"""
        #picked_card = random.choice(deck_of_cards) 
        random_number = random.randint(0,len(deck_of_cards))
        #picked_card = deck_of_cards[1] --> il me sort bien "black" si je fais un "print(picked_card.color_rgb)"
        self.picked_card = deck_of_cards[random_number]
        print("You picked the card {0} of {1}".format(self.picked_card.value, self.picked_card.color_stcc))
        self.hand.append(self.picked_card)
        #print(self.hand)
        del deck_of_cards[random_number] #retirer un élément d'une liste à partir de sa position au lieu de sa valeur 



    def answering(self):
        """The player answers to the question asked by the program"""
        pass
        #parameters: question from program
        #output: answer from player


    def with_or_without_panache(self):
        """The player choses if he/she activates the 'panache' option"""
        pass
        self.panache = False
        answer_panache = input("With panache ? Yes/No")
        if answer_panache == "Yes":
            self.panache = True
            print("Okaaaaaaay, with panache ! congrats for the bravery !")
        else:
            print("Ok, without panache...      ...cautious gamer")


    def give_points(self, player_receiving_points, points_for_the_current_round):
        """The player gives points to another player or him/her-self"""

        if self.panache == True:
            panache_factor = DEFAULT_PANACHE_FACTOR
        else:
            panache_factor = 1

        number_of_points = points_for_the_current_round * panache_factor
        player_receiving_points.points += number_of_points
        return number_of_points

    def win(self, points_of_the_round):
        print("Congrats, you won this round !")
        name_of_player_receiving_points = input("You are allowed to give {0} points (x {1} if you played wih panache) to another player, who do you chose among TO BE DONE ?".format(POINTS_ROUND_1, DEFAULT_PANACHE_FACTOR))
        
        for player_receiving_points_round in players:
            if player_receiving_points_round.name == name_of_player_receiving_points:
                number_of_points = self.give_points(player_receiving_points_round, points_of_the_round)

        print("Player {0} gave {1} points to player {2}".format(self.name, number_of_points, player_receiving_points_round.name))

    def lose(self, points_of_the_round):
        print("Ouch ! you lose this round... Good luck for the next one !")
        
        number_of_points = self.give_points(self, points_of_the_round)
        print("PLayer {0} takes the {1} points".format(self.name, number_of_points))



def cards_deck_initialization():
    """Creates a deck of 52 cards"""

    for color_stcc in COLORS_STCC:
        for rank in RANKS:
            value = rank_to_values_correspondance[rank]
            color_rgb = colors_stcc_to_colors_RBG_correspondance[color_stcc]
            card = Cards(color_stcc, color_rgb, rank, value) 
            deck_of_cards.append(card)


def players_initialization():
    """Asks how many players for the party"""
    """Asks names of players and save them in a table"""

    number_of_players = int(input("How many players for this party ?")) #il faut que ce soit un chiffre
    players_names=[]

    for i in range(1, number_of_players+1):
        player_name = input("Dear player {0} whats is your name ?".format(i))
        players_names.append(player_name)
        player = Player(player_name)
        players.append(player)

    
    


def round_1(player):
    """Asks 'Red or Black', Asks with or without Panache, pick a card and determines if the player wins or distribute points"""

    print("")

    """Questions"""
    print("Welcome {0} ! Red or Black ?".format(player.name))
    answer_round_1 = input()
    
    player.with_or_without_panache()
    
    """Pick a card"""
    player.pick_a_card()
    #print(player.picked_card.color_rgb) OK

    """Determination if the player wins or loses"""
    if answer_round_1 == player.picked_card.color_rgb:
        player.win(POINTS_ROUND_1)

    elif answer_round_1 != player.picked_card.color_rgb:
        player.lose(POINTS_ROUND_1)

    else:
        print("Error about red or black answer")



def round_2(player):
    """Asks 'Plus or minus', Asks with or without Panache, pick a card and determines if the player wins or distribute points"""

    print("")

    """Questions"""
    print("{0} ! Plus or Minus ?".format(player.name))
    answer_round_2 = input()
    
    player.with_or_without_panache()
    
    """Pick a card"""
    player.pick_a_card()

    """Determination if the player wins or loses"""
    if answer_round_2 == "Plus":
        if player.hand[0].rank < player.hand[1].rank:
            player.win(POINTS_ROUND_2)
        else:
            player.lose(POINTS_ROUND_2)

    if answer_round_2 == "Minus":
        if player.hand[0].rank > player.hand[1].rank:
            player.win(POINTS_ROUND_2)
        else:
            player.lose(POINTS_ROUND_2)
 

def round_3(player):
    """Asks 'Inside or Outside', Asks with or without Panache, pick a card and determines if the player wins or distribute points"""

    print("")

    """Questions"""
    print("{0} ! Inside or Outside ?".format(player.name))
    answer_round_3 = input()
    
    player.with_or_without_panache()
    
    """Pick a card"""
    player.pick_a_card()

    """Determination if the player wins or loses"""
    if answer_round_3 == "Inside":
        if player.hand[0].rank < player.hand[2].rank < player.hand[1].rank or player.hand[1].rank < player.hand[2].rank < player.hand[0].rank :
            player.win(POINTS_ROUND_3)
        else:
            player.lose(POINTS_ROUND_3)

    if answer_round_3 == "Outside":
        if player.hand[2].rank < player.hand[0].rank and  player.hand[2].rank < player.hand[1].rank or player.hand[0].rank < player.hand[2].rank and  player.hand[1].rank < player.hand[2].rank :
            player.win(POINTS_ROUND_3)
        else:
            player.lose(POINTS_ROUND_3)


def round_4(player):
    """Asks 'Spade, Club, Heart, Diamond', Asks with or without Panache, pick a card and determines if the player wins or distribute points"""

    print("")

    """Questions"""
    print("{0} ! Spade, Club, Heart, Diamond ?".format(player.name))
    answer_round_4 = input()
    
    player.with_or_without_panache()
    
    """Pick a card"""
    player.pick_a_card()

    """Determination if the player wins or loses"""
    if answer_round_4 == player.picked_card.color_stcc:
        player.win(POINTS_ROUND_4)

    elif answer_round_4 != player.picked_card.color_stcc:
        player.lose(POINTS_ROUND_4)



def main():
    cards_deck_initialization()
    players_initialization()

    print("")
    print("ROUND 0Ooo0O0Oo0Oo0NE")
    for player in players:
        round_1(player)

    print("")
    print("ROUND TWOo0O0o0O0o000oOoo0OoO")
    for player in players:
        round_2(player)

    print("")
    print("ROUND THRRRREEEEEEE")
    for player in players:
        round_3(player)

    print("")
    print("ROUND FOOoOo0OOOo0OuURRRR")
    for player in players:
        round_4(player)

    print("=== TABLE OF SCORES ===")
    for player in players:
        print("=== Player {} got {} points ===".format(player.name, player.points))

    maxi_score = 1000
    winner_name =""
    for player in players:
        if player.points < maxi_score:
            maxi_score = player.points
            winner_name = player.name
    print("Winner is ...      {0} !".format(winner_name))

    print("")
    print("Know, please remember your cards : P")

    """for player in players:
            round_4(player)"""


main()