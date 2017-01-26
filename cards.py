import random

class Card(object):
	suit_names =  ["Diamonds","Clubs","Hearts","Spades"]
	rank_levels = [1,2,3,4,5,6,7,8,9,10,11,12,13]
	faces = {1:"Ace",11:"Jack",12:"Queen",13:"King"}

	def __init__(self, suit=0,rank=2):
		self.suit = self.suit_names[suit]
		if rank in self.faces: # self.rank handles printed representation
			self.rank = self.faces[rank]
		else:
			self.rank = rank
		self.rank_num = rank # To handle winning comparison 

	def __str__(self):
		return "{} of {}".format(self.rank,self.suit)

class Deck(object):
	def __init__(self): # Don't need any input to create a deck of cards
		# This working depends on Card class existing above
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card) # appends in a sorted order

	def __str__(self):
		total = []
		for card in self.cards:
			total.append(card.__str__())
		# shows up in whatever order the cards are in
		return "\n".join(total) # returns a multi-line string listing each card

	def pop_card(self, i=-1):
		# removes and returns a card from the Deck
		# default is the last card in the Deck
		return self.cards.pop(i) # this card is no longer in the deck -- taken off

	def shuffle(self):
		random.shuffle(self.cards)

	def replace_card(self, card):
		card_strs = [] #forming an empty list
		for c in self.cards: #each card in self.cards (the initial list)
			card_strs.append(c.__str__()) # appends the string that represents that card
		if card.__str__() not in card_strs: #if the string representing this card is not in this list already, 
			self.cards.append(card) #add it to the list

	def sort_cards(self):
		# Basically, remake the deck in a sorted way
		# This is assuming you cannot have more than the normal 52 cars in a deck
		self.cards = []
		for suit in range(4):
			for rank in range(1,14):
				card = Card(suit,rank)
				self.cards.append(card)

def play_war_game():
	player1 = Deck()
	player2 = Deck()

	p1_score = 0
	p2_score = 0

	player1.shuffle()
	player2.shuffle()

	print("\n*** BEGIN THE GAME ***\n")
	for i in range(52):
		p1_card = player1.pop_card()
		p2_card = player2.pop_card()

		print("Player 1 plays", p1_card,"& Player 2 plays", p2_card)

		if p1_card.rank_num > p2_card.rank_num:
			print("Player 1 wins a point!")
			p1_score += 1
		elif p1_card.rank_num < p2_card.rank_num:
			print("Player 2 wins a point!")
			p2_score += 1
		else:
			print("Tie. Next turn.")

	if p1_score > p2_score:
		return "Player1", p1_score, p2_score
	elif p2_score > p1_score:
		return "Player2", p1_score, p2_score
	else:
		return "Tie", p1_score, p2_score

if __name__ == "__main__":
	result = play_war_game()
	print("""\n\n******\nTOTAL SCORES:\nPlayer 1: {}\nPlayer 2: {}\n\n""".format(result[1],result[2]))
	if result[0] != "Tie":
		print(result[0], "wins")
	else:
		print("TIE!")


###########

###########


# What are the class variables in the Card class? Why are they class variables?
#Sweet_names, rank_levels, faces
#They are class variables because these are always the same no matter what card you have (whatever instance of the class you are in). These are things that
#  stay stagnant throgh the class.

# What are the instance variables in the Card class? Why are they instance variables and not class variables?
#self.suit, self.rank, self.rank_num
# Instance variables will vary by card so that is why it is an instance variable, it is specific to the instance

# How many instance variables does each instance of Deck have?
# 1

# How many methods does the Deck class have?
# 6 instance variables

# What does the replace_card method in the Card class do? Explain.
# It is replacing the card with the rank and suit of the card as string, and if the card suit and rank is not in the list, it will add it. 

# What's happening in lines 70-72?
# Cards are being removed from the deck, simulating drawing cards.

# What's happening in lines 76-83?
# It is comparing the cards that are drawn by both players. It compares the ranks and whosever rank is higher, that player will win, 
# and if there is no winner, then it states that there is a tie. Points are accumulated for each player by 1 for each win.

# What type of value is in the player1 variable? the player2 variable?
# Instance of class Deck that contains card objects. It's the deck that represents each player 

# What determines which player wins the game of War?
# Line 85-90, and also the last if statement seeing if there is a true winner.
# What type of value does the play_war_game function return?
# It returns a tuple of the winner, and both players scores





