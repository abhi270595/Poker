from deuces import Card

class Player:
	"""
    Class representing a player. 
	Attributes:
	1. Name of the Player - self.name
	2. Position where the player is sitting - self.position
	3. Buy-In money for the player - self.money
	4. Hand of the player in a particular game - self.hand
    """
	
	def __init__(self, name, position):
		self.name = name
		self.position = int ( position )
		
	def get_player_name(self):
		return self.name
		
	def get_player_position(self):
		return self.position
		
	def _check_non_empty_string(self, string):
		if string and not string.isspace():
			return True
		else:
			return False
		
	def set_player_hand(self, first_card_name, second_card_name):
		if not self._check_non_empty_string(first_card_name):
			raise ValueError('First card name cannot be empty')
			return
			
		if not self._check_non_empty_string(second_card_name):
			raise ValueError('Second card name cannot be empty')
			return
			
		self.hand = [
			Card.new( first_card_name.strip() ),
			Card.new( second_card_name.strip() )
			]
			
	def get_player_hand(self):
		try:
			return self.hand
		except NameError:
			raise NameError('Player does not have any cards in their hand')
			return []
			
	def set_player_money(self, money):
		self.money = int( money )
		
	def get_player_money(self):
		try:
			return self.money
		except NameError:
			raise NameError('Player does not have any money')
			return []