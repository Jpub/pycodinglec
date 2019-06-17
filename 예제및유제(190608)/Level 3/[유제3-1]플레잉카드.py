suit = ['♠', '♣', '♡', '◇']
denomination = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
all_cards = [i+j for i in suit for j in denomination]
print(all_cards)

