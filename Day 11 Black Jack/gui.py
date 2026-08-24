import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk, ImageDraw, ImageFont
from game_logic import BlackjackGame
from constants import SUITS, RANKS


class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("♠️ Blackjack Casino ♠️")
        self.root.geometry("1100x900")
        self.root.configure(bg='#1a472a')
        self.root.resizable(False, False)

        # Initialize game
        self.game = BlackjackGame()
        self.card_images = {}
        self.back_image = None

        # Create card images
        self.create_card_images()

        # Setup UI
        self.setup_ui()

        # Initial display
        self.update_display()
        self.update_buttons()

    def create_card_images(self):
        """Create all card images dynamically"""
        if not os.path.exists('cards'):
            os.makedirs('cards')

        for suit in SUITS:
            for rank in RANKS:
                # Create image
                img = Image.new('RGB', (100, 140), 'white')
                draw = ImageDraw.Draw(img)

                # Draw border
                draw.rectangle([(2, 2), (98, 138)], outline='black', width=2)

                # Set color based on suit
                color = 'red' if suit in ['♥', '♦'] else 'black'

                try:
                    font = ImageFont.truetype("arial.ttf", 20)
                    big_font = ImageFont.truetype("arial.ttf", 50)
                except:
                    font = ImageFont.load_default()
                    big_font = ImageFont.load_default()

                # Top left
                draw.text((8, 8), f"{rank}", fill=color, font=font)
                draw.text((8, 30), f"{suit}", fill=color, font=font)

                # Bottom right
                draw.text((75, 95), f"{rank}", fill=color, font=font)
                draw.text((75, 117), f"{suit}", fill=color, font=font)

                # Center large suit
                draw.text((35, 45), f"{suit}", fill=color, font=big_font)

                filename = f"cards/{rank}_{suit}.png"
                img.save(filename)

                # Load for tkinter
                img = Image.open(filename)
                img = img.resize((100, 140), Image.Resampling.LANCZOS)
                self.card_images[f"{rank}{suit}"] = ImageTk.PhotoImage(img)

        # Create back of card
        img = Image.new('RGB', (100, 140), '#2c3e50')
        draw = ImageDraw.Draw(img)

        for i in range(0, 100, 20):
            draw.line([(i, 0), (i, 140)], fill='#34495e', width=1)
        for i in range(0, 140, 20):
            draw.line([(0, i), (100, i)], fill='#34495e', width=1)

        draw.rectangle([(2, 2), (98, 138)], outline='#95a5a6', width=2)

        try:
            font = ImageFont.truetype("arial.ttf", 30)
        except:
            font = ImageFont.load_default()
        draw.text((25, 55), "♠", fill='#95a5a6', font=font)

        img.save("cards/back.png")
        img = Image.open("cards/back.png")
        img = img.resize((100, 140), Image.Resampling.LANCZOS)
        self.back_image = ImageTk.PhotoImage(img)

    def setup_ui(self):
        """Setup the GUI layout"""
        # Title
        title_frame = tk.Frame(self.root, bg='#1a472a')
        title_frame.pack(pady=10)

        tk.Label(
            title_frame,
            text="♠️ BLACKJACK CASINO ♠️",
            font=('Arial', 32, 'bold'),
            fg='#ffd700',
            bg='#1a472a'
        ).pack()

        # Balance and bet display
        info_frame = tk.Frame(self.root, bg='#1a472a')
        info_frame.pack(pady=5)

        self.balance_label = tk.Label(
            info_frame,
            text=f"💰 Balance: ${self.game.balance}",
            font=('Arial', 18),
            fg='white',
            bg='#1a472a'
        )
        self.balance_label.pack(side=tk.LEFT, padx=20)

        self.bet_label = tk.Label(
            info_frame,
            text="",
            font=('Arial', 18),
            fg='#ffd700',
            bg='#1a472a'
        )
        self.bet_label.pack(side=tk.LEFT, padx=20)

        # Game area
        game_frame = tk.Frame(self.root, bg='#1a472a')
        game_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        # Dealer area
        dealer_frame = tk.Frame(game_frame, bg='#1a472a')
        dealer_frame.pack(pady=10)

        tk.Label(
            dealer_frame,
            text="DEALER",
            font=('Arial', 16, 'bold'),
            fg='white',
            bg='#1a472a'
        ).pack()

        self.dealer_cards_frame = tk.Frame(dealer_frame, bg='#1a472a')
        self.dealer_cards_frame.pack(pady=5)

        self.dealer_score_label = tk.Label(
            dealer_frame,
            text="",
            font=('Arial', 14),
            fg='white',
            bg='#1a472a'
        )
        self.dealer_score_label.pack()

        # Separator
        tk.Frame(game_frame, height=2, bg='#ffd700').pack(pady=20, fill=tk.X, padx=50)

        # Player area
        player_frame = tk.Frame(game_frame, bg='#1a472a')
        player_frame.pack(pady=10)

        tk.Label(
            player_frame,
            text="PLAYER",
            font=('Arial', 16, 'bold'),
            fg='white',
            bg='#1a472a'
        ).pack()

        self.player_cards_frame = tk.Frame(player_frame, bg='#1a472a')
        self.player_cards_frame.pack(pady=5)

        self.player_score_label = tk.Label(
            player_frame,
            text="",
            font=('Arial', 14),
            fg='white',
            bg='#1a472a'
        )
        self.player_score_label.pack()

        # Betting controls
        bet_frame = tk.Frame(self.root, bg='#1a472a')
        bet_frame.pack(pady=10)

        tk.Label(
            bet_frame,
            text="Bet Amount: $",
            font=('Arial', 14),
            fg='white',
            bg='#1a472a'
        ).pack(side=tk.LEFT, padx=5)

        self.bet_entry = tk.Entry(
            bet_frame,
            width=10,
            font=('Arial', 14),
            justify='center'
        )
        self.bet_entry.pack(side=tk.LEFT, padx=5)
        self.bet_entry.insert(0, "50")

        # Quick bet buttons
        quick_bets = [25, 50, 100, 200]
        for amount in quick_bets:
            tk.Button(
                bet_frame,
                text=f"${amount}",
                font=('Arial', 10),
                bg='#2c3e50',
                fg='white',
                command=lambda a=amount: self.set_bet(a)
            ).pack(side=tk.LEFT, padx=2)

        # Action buttons - always visible but state changes
        button_frame = tk.Frame(self.root, bg='#1a472a')
        button_frame.pack(pady=15)

        self.deal_button = tk.Button(
            button_frame,
            text="🃏 DEAL",
            font=('Arial', 16, 'bold'),
            bg='#27ae60',
            fg='white',
            padx=30,
            pady=10,
            command=self.deal
        )
        self.deal_button.pack(side=tk.LEFT, padx=10)

        self.hit_button = tk.Button(
            button_frame,
            text="✋ HIT",
            font=('Arial', 16, 'bold'),
            bg='#2980b9',
            fg='white',
            padx=30,
            pady=10,
            command=self.hit
        )
        self.hit_button.pack(side=tk.LEFT, padx=10)

        self.stand_button = tk.Button(
            button_frame,
            text="✊ STAND",
            font=('Arial', 16, 'bold'),
            bg='#e67e22',
            fg='white',
            padx=30,
            pady=10,
            command=self.stand
        )
        self.stand_button.pack(side=tk.LEFT, padx=10)

        self.new_round_button = tk.Button(
            button_frame,
            text="🔄 NEW ROUND",
            font=('Arial', 16, 'bold'),
            bg='#8e44ad',
            fg='white',
            padx=30,
            pady=10,
            command=self.new_round
        )
        self.new_round_button.pack(side=tk.LEFT, padx=10)

        # Status label
        self.status_label = tk.Label(
            self.root,
            text="💰 Place your bet and click DEAL!",
            font=('Arial', 14, 'italic'),
            fg='#ffd700',
            bg='#1a472a'
        )
        self.status_label.pack(pady=10)

    def set_bet(self, amount):
        """Quick set bet amount"""
        self.bet_entry.delete(0, tk.END)
        self.bet_entry.insert(0, str(amount))

    def update_buttons(self):
        state = self.game.game_state

        if state == "BETTING":
            self.deal_button.config(state='normal')
            self.hit_button.config(state='disabled')
            self.stand_button.config(state='disabled')
            self.new_round_button.config(state='disabled')
            self.bet_entry.config(state='normal')
        elif state == "PLAYER_TURN":
            self.deal_button.config(state='disabled')
            self.hit_button.config(state='normal')
            self.stand_button.config(state='normal')
            self.new_round_button.config(state='disabled')
            self.bet_entry.config(state='disabled')
        elif state == "GAME_OVER":
            self.deal_button.config(state='disabled')
            self.hit_button.config(state='disabled')
            self.stand_button.config(state='disabled')
            self.new_round_button.config(state='normal')
            self.bet_entry.config(state='disabled')
        elif state == "DEALER_TURN":
            self.deal_button.config(state='disabled')
            self.hit_button.config(state='disabled')
            self.stand_button.config(state='disabled')
            self.new_round_button.config(state='disabled')
            self.bet_entry.config(state='disabled')

    def deal(self):
        try:
            bet_amount = int(self.bet_entry.get())
        except ValueError:
            messagebox.showwarning("Invalid Bet", "Please enter a valid number!")
            return


        success, message = self.game.place_bet(bet_amount)
        if not success:
            messagebox.showwarning("Bet Error", message)
            return

        result = self.game.deal_cards()

        self.update_display()
        self.update_buttons()
        self.update_balance()

        if result:
            self.update_display(show_all=True)
            self.status_label.config(text=result["message"])
            self.update_buttons()

    def hit(self):
        result = self.game.hit()
        self.update_display()
        self.update_balance()

        if result:
            self.update_display(show_all=True)
            self.status_label.config(text=result["message"])
            self.update_buttons()

    def stand(self):
        result = self.game.stand()
        self.update_display(show_all=True)
        self.update_balance()

        if result:
            self.status_label.config(text=result["message"])
            self.update_buttons()

    def new_round(self):
        self.game.reset()
        self.update_display()
        self.update_buttons()
        self.update_balance()
        self.status_label.config(text="💰 Place your bet and click DEAL!")

    def update_display(self, show_all=False):
        state = self.game.get_game_state()

        for widget in self.dealer_cards_frame.winfo_children():
            widget.destroy()
        for widget in self.player_cards_frame.winfo_children():
            widget.destroy()

        dealer_hand = state["dealer_hand"]
        for i, card in enumerate(dealer_hand):
            if i == 0 and not show_all and state["state"] == "PLAYER_TURN":
                img_label = tk.Label(
                    self.dealer_cards_frame,
                    image=self.back_image,
                    bg='#1a472a'
                )
            else:
                key = f"{card.rank}{card.suit}"
                if key in self.card_images:
                    img_label = tk.Label(
                        self.dealer_cards_frame,
                        image=self.card_images[key],
                        bg='#1a472a'
                    )
                else:
                    img_label = tk.Label(
                        self.dealer_cards_frame,
                        text=str(card),
                        font=('Arial', 14),
                        bg='white',
                        width=10,
                        height=8,
                        relief='solid'
                    )
            img_label.pack(side=tk.LEFT, padx=2)

        player_hand = state["player_hand"]
        for card in player_hand:
            key = f"{card.rank}{card.suit}"
            if key in self.card_images:
                img_label = tk.Label(
                    self.player_cards_frame,
                    image=self.card_images[key],
                    bg='#1a472a'
                )
            else:
                img_label = tk.Label(
                    self.player_cards_frame,
                    text=str(card),
                    font=('Arial', 14),
                    bg='white',
                    width=10,
                    height=8,
                    relief='solid'
                )
            img_label.pack(side=tk.LEFT, padx=2)

        if state["player_hand"]:
            self.player_score_label.config(text=f"Score: {state['player_score']}")
        else:
            self.player_score_label.config(text="")

        if show_all or state["state"] != "PLAYER_TURN":
            if state["dealer_hand"]:
                self.dealer_score_label.config(text=f"Score: {state['dealer_score']}")
            else:
                self.dealer_score_label.config(text="")
        else:
            if state["dealer_hand"]:
                first_card_value = state["dealer_hand"][0].get_value()
                self.dealer_score_label.config(text=f"Score: {first_card_value} + ?")
            else:
                self.dealer_score_label.config(text="")

    def update_balance(self):
        state = self.game.get_game_state()
        self.balance_label.config(text=f"💰 Balance: ${state['balance']}")

        if state['bet'] > 0:
            self.bet_label.config(text=f"💵 Bet: ${state['bet']}")
        else:
            self.bet_label.config(text="")

        if state['balance'] <= 0:
            self.status_label.config(text="💔 You're out of money! Game Over!")
            messagebox.showinfo("Game Over", "You're out of money! Game Over!")


def run_gui():
    root = tk.Tk()
    app = BlackjackGUI(root)
    root.mainloop()