#Problem J3 - S1: Keeping Score - 2001 (SirNooby)
cards = input() + "E"
card_count = 0
suit = 0
suit_total = 0
total = 0

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
card_values = {"A":4, "K":3, "Q":2, "J":1}

print("Cards Dealt     Points")
print("Clubs", end=" ")

for i in range(1, len(cards)):
    if cards[i] in ["C", "D", "H", "S", "E"]:
        
        if card_count == 0:
            suit_total += 3
        elif card_count == 1:
            suit_total += 2
        elif card_count == 2:
            suit_total += 1

        print(suit_total, end=" ")
        total += suit_total
        suit_total = 0
        card_count = 0

        print("")

        if cards[i] != "E":
            suit += 1
            print(suits[suit], end=" ")
        else:
            print("Total", total, end=" ")

    else:
        print(cards[i], end=" ")
        card_count += 1
        if cards[i] in card_values:
            suit_total += card_values[cards[i]]