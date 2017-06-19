cards = (6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')
suits = ('+', '<3', '<>', '<-')
deck = {}
for i in suits:
	deck = deck.fromkeys(cards, i)
	print(deck)
