from deuces import Card
from player import Player
from deuces import Evaluator

class Game:
	"""
    Class representing a poker game. 
	Attributes:
	1. All the players in the game - self.players
	2. Community Cards for the game - self.community_cards
    """
	
	MOVES = {
		'called': 'Our suggestion is that you should call',
		'folded': 'Our suggestion is that you should fold',
		'raised': 'Our suggestion is that you should raise',
		'checked': 'Our suggestion is that you should check',
		'timedout': 'You exceeded maximum time allotted for placing a bet'
	}
	
	def __init__( self, file_name ):
		# Parsing logs from a file
		logs = self.read_from_file( file_name )
		self.extract_players( logs )
		
		self.play( logs )
		
	def read_from_file( self, file_name ):
		read_file = open( file_name, 'r' )
		game_log = read_file.readlines()
		read_file.close()
		return game_log
		
	def new_players_joining( self, parse_log ):
		player_name = parse_log[1]
		self.players[player_name] = Player(parse_log[1], parse_log[2])
		#print self.players[player_name].get_player_name(), self.players[player_name].get_player_position()
		
	def getting_money(self, parse_log ):
		player_name = parse_log[1]
		# setting money for the player
		self.players[player_name].set_player_money(parse_log[3])
		#print self.players[player_name].get_player_money()
		
	def getting_hand_cards( self, parse_log ):
		player_name = parse_log[1]
		# setting hand for the player
		parse_cards = parse_log[4].split(" ")
		if len( parse_cards ) == 2:
			self.players[player_name].set_player_hand(parse_cards[0], parse_cards[1])
		else:
			raise ValueError('Invalid hand for a Poker game')
		#print self.players[player_name].get_player_hand()
		
	def getting_community_cards( self, parse_log ):
		if parse_log[1] == "FLOP":
			self.community_cards = []
		cards = parse_log[2].split(" ")
		for card in cards:
			self.community_cards.append( Card.new( card.strip() ) )
		#print self.community_cards;
		
	def extract_players( self, logs ):
		self.players = {}
		# Looping through all the logs line by line
		for log in logs:
			parse_log = log.split(",")
			parse_log = map(str.strip, parse_log)
			if parse_log[0] == 'TAKE SEAT':
				self.new_players_joining( parse_log )
				
	def play( self, logs ):
		prompt_text = "Select a Player by number --->\n"
		player_id = 1
		input_to_player = {}
		evaluator = Evaluator()
		self.community_cards = []
		
		for player in self.players:
			input_to_player[player_id] = player
			prompt_text = prompt_text + str( player_id ) + " for " + player + "(Player " + str( player_id ) + ")\n"
			player_id = player_id + 1
			
		player_id = input( prompt_text )
		# Looping through all the logs line by line
		for log in logs:
			parse_log = log.split(",")
			parse_log = map(str.strip, parse_log)
			if parse_log[0] == 'TAKE SEAT':
				parse_log = parse_log[0 : len( parse_log ) - 1]
			elif parse_log[0] == 'GAME STARTED':
				print parse_log[0]
				continue
			elif parse_log[0] == 'HOLE CARD':
				self.getting_money( parse_log )
				self.getting_hand_cards( parse_log )
			elif parse_log[0] == 'COMMUNITY CARD':
				self.getting_community_cards( parse_log )
			# Removing the time stamp
			elif parse_log[0] == 'USER TURN':
				parse_log = parse_log[0 : len( parse_log ) - 1]
			# Telling the user what kind of hand they posses
			if parse_log[0] == 'USER TURN' and parse_log[1] == input_to_player[player_id] and len( self.community_cards ) > 2 :
				hand = self.players[parse_log[1]].get_player_hand()
				board = self.community_cards
				hand_strength = evaluator.evaluate(board, hand)
				rank_class = evaluator.get_rank_class(hand_strength)
				print ">>>> " + parse_log[1] + ' you have "' + evaluator.class_to_string(rank_class) + '"'
			# Checking with the user for the suggestion currently only 'y' is accepted
			if parse_log[0] == 'USER TURN' and parse_log[1] == input_to_player[player_id]:
				suggestion_text = Game.MOVES[parse_log[2]]
				if len( parse_log ) >= 4 and not parse_log[2] == 'timedout':
					suggestion_text = suggestion_text + " " + parse_log[3] + " chips"
				while raw_input( ">>>> " + suggestion_text + " for this betting round. Do you agree? Input y or n." ) == "n":
					print "Please try again."
	
			print ", ".join( parse_log )
			
		hands = []
		for player in self.players:
			hands.append( self.players[player].get_player_hand() )
		board = self.community_cards
		print "\n\n\n\n\n"
		evaluator.hand_summary( board, hands )