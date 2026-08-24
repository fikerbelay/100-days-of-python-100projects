# game_logic.py - Fixed dealer_play method
from card_utils import Card, Deck


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = []
        self.dealer_hand = []
        self.balance = 1000
        self.bet = 0
        self.game_state = "BETTING"  # BETTING, PLAYER_TURN, DEALER_TURN, GAME_OVER

    def calculate_score(self, hand):
        score = 0
        aces = 0

        for card in hand:
            score += card.get_value()
            if card.rank == 'A':
                aces += 1

        while score > 21 and aces > 0:
            score -= 10
            aces -= 1

        return score

    def place_bet(self, amount):
        if amount <= 0:
            return False, "Bet must be positive!"
        if amount > self.balance:
            return False, f"Insufficient funds! You have ${self.balance}"

        self.bet = amount
        self.balance -= amount
        self.game_state = "PLAYER_TURN"
        return True, "Bet placed successfully!"

    def deal_cards(self):
        self.player_hand = []
        self.dealer_hand = []

        for _ in range(2):
            self.player_hand.append(self.deck.deal())
            self.dealer_hand.append(self.deck.deal())

        if self.calculate_score(self.player_hand) == 21:
            self.game_state = "GAME_OVER"
            return self.check_blackjack()

        self.game_state = "PLAYER_TURN"
        return None

    def hit(self):
        if self.game_state != "PLAYER_TURN":
            return None

        self.player_hand.append(self.deck.deal())
        player_score = self.calculate_score(self.player_hand)

        if player_score > 21:
            self.game_state = "GAME_OVER"
            return {"result": "BUST", "message": f"💥 BUST! You lose ${self.bet}!"}
        elif player_score == 21:
            return self.stand()

        return None

    def stand(self):
        if self.game_state != "PLAYER_TURN":
            return None

        self.game_state = "DEALER_TURN"
        result = self.dealer_play()
        self.game_state = "GAME_OVER"
        return result

    def dealer_play(self):
        dealer_score = self.calculate_score(self.dealer_hand)
        player_score = self.calculate_score(self.player_hand)

        # Dealer must hit on 16 or less
        while dealer_score < 17:
            self.dealer_hand.append(self.deck.deal())
            dealer_score = self.calculate_score(self.dealer_hand)

        # Determine winner
        if dealer_score > 21:
            winnings = self.bet * 2
            self.balance += winnings
            return {"result": "WIN", "message": f"🎉 Dealer BUST! You win ${self.bet}!", "winnings": winnings}
        elif dealer_score > player_score:
            return {"result": "LOSE", "message": f"😤 Dealer wins! You lose ${self.bet}!"}
        elif dealer_score < player_score:
            winnings = self.bet * 2
            self.balance += winnings
            return {"result": "WIN", "message": f"🎉 You win ${self.bet}!", "winnings": winnings}
        else:
            # Push (tie)
            self.balance += self.bet
            return {"result": "PUSH", "message": f"🤝 Push! Bet returned."}

    def check_blackjack(self):
        dealer_score = self.calculate_score(self.dealer_hand)

        if dealer_score == 21:
            self.balance += self.bet
            return {"result": "PUSH", "message": "🤝 Both have Blackjack! Push!"}
        else:
            winnings = int(self.bet * 2.5)
            self.balance += winnings
            return {"result": "BLACKJACK", "message": f"🎉 BLACKJACK! You win ${self.bet * 1.5}!", "winnings": winnings}

    def reset(self):
        self.player_hand = []
        self.dealer_hand = []
        self.bet = 0
        self.game_state = "BETTING"

        if len(self.deck.cards) < 10:
            self.deck = Deck()

    def get_game_state(self):
        return {
            "state": self.game_state,
            "player_hand": self.player_hand,
            "dealer_hand": self.dealer_hand,
            "player_score": self.calculate_score(self.player_hand) if self.player_hand else 0,
            "dealer_score": self.calculate_score(self.dealer_hand) if self.dealer_hand else 0,
            "balance": self.balance,
            "bet": self.bet
        }