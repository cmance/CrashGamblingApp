import random

def high_low_game():
    # Create a deck of cards
    deck = list(range(1, 14)) * 4  # Each card value appears 4 times (one for each suit)
    random.shuffle(deck)

    # Initial card
    current_card = deck.pop()
    print(f"Current card: {current_card}")

    while True:
        # Prompt the player for their guess
        guess = input("Will the next card be higher (H) or lower (L)? ").upper()

        # Draw the next card
        next_card = deck.pop()
        print(f"Next card: {next_card}")

        # Compare the values
        if next_card > current_card:
            result = "H"
        elif next_card < current_card:
            result = "L"
        else:
            result = "E"  # Equal value

        # Determine if the player guessed correctly
        if guess == result:
            print("Correct!")
        else:
            print("Incorrect!")
            # print(f"The card was {next_card}")
            break

        # Update the current card
        current_card = next_card

        # Check if the deck is empty
        if not deck:
            print("No more cards to draw.")
            break

        # Prompt for the next round
        print(f"\nCurrent card: {current_card}")

# Start the game
high_low_game()