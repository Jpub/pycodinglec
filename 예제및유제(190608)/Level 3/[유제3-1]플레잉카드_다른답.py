suit = ['♠', '♣', '♡', '◇']
denomination = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
all_cards = []
for i in suit:
    for j in denomination:
        all_cards.append(i+j)
print(all_cards)

