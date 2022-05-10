from unicodedata import name
import random

"""
NEXT STEP : To secure: e.g. : user should answer only a number when asked how
many playersare playing.; e.g. : user should play with CaPiTals caracters.

NEXT STEP : separate the code in different parts (e.g. : ModelVueControler)
NEXT STEP : code round_5 : pyramid
 __________________________________________________________________________
|============================= RED OR BLACK ===============================|
|= Red or black is a card game that is played in turns. At each turn,     =|
|= each player must answer a question ("Red or Black?", "Plus or Minus?,  =|
|= etc.) and choses if its answer is accompanied by the mention "panache" =|
|= which doubles the number of points in game.                            =|
|= For each question, if the player did not provide the good answer,      =|
|= he/she wins points; if the player was right, he/she gives points to    =|
|= another player.                                                        =|
|= The aim of the game is to get as few points as possible.               =|
|==========================================================================|
"""


DEFAULT_NO_PANACHE_FACTOR, DEFAULT_PANACHE_FACTOR = 1, 2

POINTS_ROUND_1, POINTS_ROUND_2, POINTS_ROUND_3, POINTS_ROUND_4 = 1, 2, 3, 4

COLORS_STCC = ("Spade", "Club", "Heart", "Diamond")
RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)

deck_of_cards = []
players = []
players_names = []

colors_stcc_to_colors_RBG_correspondance = {
    "Spade": "Black",
    "Club": "Black",
    "Heart": "Red",
    "Diamond": "Red"
}

rank_to_values_correspondance = {
    1: "Ace",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Jack",
    12: "Queen",
    13: "King"
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
        """Initialization the player"""
        self.name = name
        self.points = 0
        self.hand = []

    def pick_a_card(self):
        """The player picks a random card in the deck of card"""
        random_number = random.randint(0, len(deck_of_cards))
        self.picked_card = deck_of_cards[random_number]
        print("You picked the card {0} of {1}".format(self.picked_card.value, self.picked_card.color_stcc))
        print_a_card(self.picked_card.value, self.picked_card.color_stcc)
        self.hand.append(self.picked_card)
        del deck_of_cards[random_number]  #delete an element from a list with its position instead of its value


    def with_or_without_panache(self):
        """The player choses if he/she activates the 'panache' option"""
        self.panache = False
        answer_panache = input("With panache ? Yes/No")
        if answer_panache == "Yes":
            self.panache = True
            print("Okaaaaaaay, with panache ! congrats for the bravery !")
        else:
            print("Ok, without panache...      ...cautious gamer")

    def give_points(self, player_receiving_points, points_for_the_current_round):
        """The player gives points to another player or him/her-self"""
        if self.panache is True:
            panache_factor = DEFAULT_PANACHE_FACTOR
        else:
            panache_factor = DEFAULT_NO_PANACHE_FACTOR

        number_of_points = points_for_the_current_round * panache_factor
        player_receiving_points.points += number_of_points
        return number_of_points

    def win(self, points_of_the_round):
        """The player wins and then give points"""
        print("Congrats, you won this round !")
        name_of_player_receiving_points = input("You are allowed to give {0} point(s) (x {1} if you played wih panache) to another player, who do you chose among: {2} ?".format(POINTS_ROUND_1, DEFAULT_PANACHE_FACTOR, " / ".join(players_names)))
        for player_receiving_points_round in players:
            if player_receiving_points_round.name == name_of_player_receiving_points:
                number_of_points = self.give_points(player_receiving_points_round, points_of_the_round)

        print("Player {0} gave {1} points to player {2}".format(self.name, number_of_points, player_receiving_points_round.name))

    def lose(self, points_of_the_round):
        """The player loses and so receive points"""
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

    number_of_players = int(input("How many players for this party ?"))


    for i in range(1, number_of_players+1):
        player_name = input("Dear player {0} whats is your name ?".format(i))
        players_names.append(player_name)
        player = Player(player_name)
        players.append(player)


def round_1(player):
    """Asks 'Red or Black', Asks with or without Panache,
     pick a card and determines if the player wins or distribute points"""

    print("")

    """Questions"""
    print("Welcome {0} ! Red or Black ?".format(player.name))
    answer_round_1 = input()

    player.with_or_without_panache()

    """Pick a card"""
    player.pick_a_card()

    """Determination if the player wins or loses"""
    if answer_round_1 == player.picked_card.color_rgb:
        player.win(POINTS_ROUND_1)

    elif answer_round_1 != player.picked_card.color_rgb:
        player.lose(POINTS_ROUND_1)

    else:
        print("Error about red or black answer")


def round_2(player):
    """Asks 'Plus or minus', Asks with or without Panache,
     pick a card and determines if the player wins or distribute points"""

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
    """Asks 'Inside or Outside', Asks with or without Panache,
     pick a card and determines if the player wins or distribute points"""

    print("")

    """Questions"""
    print("{0} ! Inside or Outside ?".format(player.name))
    answer_round_3 = input()

    player.with_or_without_panache()

    """Pick a card"""
    player.pick_a_card()

    """Determination if the player wins or loses"""
    if answer_round_3 == "Inside":
        if player.hand[0].rank < player.hand[2].rank < player.hand[1].rank or player.hand[1].rank < player.hand[2].rank < player.hand[0].rank:
            player.win(POINTS_ROUND_3)
        else:
            player.lose(POINTS_ROUND_3)

    if answer_round_3 == "Outside":
        if player.hand[2].rank < player.hand[0].rank and player.hand[2].rank < player.hand[1].rank or player.hand[0].rank < player.hand[2].rank and player.hand[1].rank < player.hand[2].rank:
            player.win(POINTS_ROUND_3)
        else:
            player.lose(POINTS_ROUND_3)


def round_4(player):
    """Asks 'Spade, Club, Heart, Diamond', Asks with or without Panache,
     pick a card and determines if the player wins or distribute points"""

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

#ONGOING PROJECT: PRINT A CARD

spade_1 = " /  \ "
spade_2 = "/    \\"
spade_3 = "\/  \/"
spade_4 = " /__\ "

club_1 = "  /\  "
club_2 = "/\\\\//\\"
club_3 = "\//\\\\/"
club_4 = " /_\  "

heart_1 = " _  _ "
heart_2 = "/ \/ \\"
heart_3 = "\    /"
heart_4 = " \__/ "

diamond_1 = " /  \ "
diamond_2 = "/    \\"
diamond_3 = "\    /"
diamond_4 = " \__/ "

ace_1 = "   ****   "
ace_2 = "  ** **   "
ace_3 = " **  **   "
ace_4 = "     **   "
ace_5 = "     **   "
ace_6 = "     **   "
ace_7 = "    ****  "
ace_8 = "    ****  "
ace_9 = "          "

two_1 = "   ****   "
two_2 = "  ** **   "
two_3 = "  ** **   "
two_4 = "    **    "
two_5 = "   **     "
two_6 = "  **      "
two_7 = "  *****   "
two_8 = "  *****   "
two_9 = "          "

three_1 = "          "
three_2 = "  *****   "
three_3 = "  *****   "
three_4 = "     **   "
three_5 = "   ***    "
three_6 = "     **   "
three_7 = "  *****   "
three_8 = "  *****   "
three_9 = "          "

four_1 = "          "
four_2 = "    **    "
four_3 = "   **     "
four_4 = "  **      "
four_5 = " ** **    "
four_6 = " ******** "
four_7 = "    **    "
four_8 = "    **    "
four_9 = "          "

five_1 = "          "
five_2 = " ******   "
five_3 = " **       "
five_4 = " **       "
five_5 = " *******  "
five_6 = "      *** "
five_7 = "      **  "
five_8 = " ******   "
five_9 = "          "

six_1 = "     **   "
six_2 = "    **    "
six_3 = "   **     "
six_4 = "  ******  "
six_5 = " **    ** "
six_6 = "**      **"
six_7 = " **    ** "
six_8 = "  ******  "
six_9 = "          "


seven_1 = " ******** "
seven_2 = " ******** "
seven_3 = "      **  "
seven_4 = "     **   "
seven_5 = " ******** "
seven_6 = "   **     "
seven_7 = "  **      "
seven_8 = " **       "
seven_9 = "          "

eight_1 = "          "
eight_2 = "  ******  "
eight_3 = " **    ** "
eight_4 = " **    ** "
eight_5 = "  ******  "
eight_6 = " **    ** "
eight_7 = "**      **"
eight_8 = " **    ** "
eight_9 = "  ******  "

nine_1 = "          "
nine_2 = "  ******* "
nine_3 = " **    ** "
nine_4 = " **    ** "
nine_5 = "  ******* "
nine_6 = "       ** "
nine_7 = "  **   ** "
nine_8 = "  ******* "
nine_9 = "          "

ten_1 = "          "
ten_2 = "          "
ten_3 = "  /|      "
ten_4 = " / |  ____"
ten_5 = "   |  |  |"
ten_6 = "   |  |  |"
ten_7 = "  _|_ |__|"
ten_8 = "          "
ten_9 = "          "


jack_1 = "          "
jack_2 = "  ********"
jack_3 = "       ** "
jack_4 = "       ** "
jack_5 = "       ** "
jack_6 = " **    ** "
jack_7 = " **   **  "
jack_8 = "  *****   "
jack_9 = "          "

queen_1 = "          "
queen_2 = "  ******  "
queen_3 = " **    ** "
queen_4 = "**      **"
queen_5 = " ** \\ ** "
queen_6 = "  ******  "
queen_7 = "      \\  "
queen_8 = "          "
queen_9 = "          "

king_9 = "          "
king_9 = "  **  *** "
king_9 = "  **  **  "
king_9 = "  ** **   "
king_9 = "  ****    "
king_9 = "  ** **   "
king_9 = "  **  **  "
king_9 = "  **   ***"
king_9 = "          "

#--> A transformer en tableau
"""
MODEL
"________________________________"
"|   / \                   / \  |"
"|  /   \                 /   \ |"
"|  \   /                 \   / |"
"|   \_/                   \_/  |"
"|          "          "          |"
"|          "          "          |"
"|          "          "          |"
"|          "          "          |"
"|          "          "          |"
"|          "          "          |"
"|          "          "          |"
"|          "          "          |"
"|          "          "          |"
"|   / \                   / \  |"
"|  /   \                 /   \ |"
"|  \   /                 \   / |"
"|   \_/                   \_/  |"
"________________________________"
"""


def print_a_card(value, color_stcc):

    print("")
    """Top of the card"""
    print("________________________________")

    """Upper colors_stcc"""
    for i in range(1,5):
        print("| {0}                 {0}|".format(globals()[color_stcc.lower() + "_" + str(i)]))

    """Middle of the card: value of the card"""
    for j in range(1,10):
        print("|          {0}          |".format(globals()[value.lower() + "_" + str(j)]))

    """Lower colors_stcc"""
    for i in range(1,5):
        print("| {0}                 {0}|".format(globals()[color_stcc.lower() + "_" + str(i)]))

    """Bottom of the card"""
    print("________________________________")
    print("")

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
    winner_name = ""
    for player in players:
        if player.points < maxi_score:
            maxi_score = player.points
            winner_name = player.name
    print("Winner is ...      {0} !".format(winner_name))

    print("")
#    print("Know, please remember your cards : P")


main()
