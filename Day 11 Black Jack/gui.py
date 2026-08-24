# gui.py
import tkinter as tk
from tkinter import messagebox
import os
from PIL import Image, ImageTk, ImageDraw, ImageFont
from game_logic import BlackjackGame
from constants import SUITS, RANKS


class QuickResultPopup:
    """A quick popup that appears in the top-right corner"""

    def __init__(self, parent, result_type, message, bet_amount):
        self.parent = parent
        self.result_type = result_type
        self.message = message
        self.bet_amount = bet_amount

        # Create popup window
        self.window = tk.Toplevel(parent)
        self.window.overrideredirect(True)  # Remove window decorations

        # Get parent window position
        parent_x = parent.winfo_x()
        parent_y = parent.winfo_y()
        parent_width = parent.winfo_width()

        # Set popup size
        width = 320
        height = 140

        # Position in top-right corner (with some padding)
        padding = 20
        x = parent_x + parent_width - width - padding
        y = parent_y + padding

        self.window.geometry(f"{width}x{height}+{x}+{y}")
        self.window.configure(bg='#1a472a')

        # Add a subtle border
        self.window.config(highlightbackground='#ffd700', highlightcolor='#ffd700', highlightthickness=2)

        # Set result colors
        if result_type in ["WIN", "BLACKJACK"]:
            icon = ""
            color = "#00ff00"
            bg_color = "#0a3d0a"
        elif result_type == "LOSE":
            icon = ""
            color = "#ff4444"
            bg_color = "#3d0a0a"
        elif result_type == "BUST":
            icon = ""
            color = "#ff6600"
            bg_color = "#3d1a0a"
        else:  # PUSH
            icon = ""
            color = "#ffd700"
            bg_color = "#1a1a0a"

        # Content frame with background color
        content_frame = tk.Frame(self.window, bg=bg_color)
        content_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=3)

        # Horizontal layout for compact popup
        top_frame = tk.Frame(content_frame, bg=bg_color)
        top_frame.pack(fill=tk.X, pady=(10, 2))

        # Icon (left)
        icon_label = tk.Label(
            top_frame,
            text=icon,
            font=('Arial', 32),
            bg=bg_color,
            fg=color
        )
        icon_label.pack(side=tk.LEFT, padx=(15, 10))

        # Message (right of icon)
        msg_label = tk.Label(
            top_frame,
            text=message,
            font=('Arial', 14, 'bold'),
            bg=bg_color,
            fg=color,
            wraplength=180
        )
        msg_label.pack(side=tk.LEFT, padx=5)

        # Bet amount (bottom)
        if result_type in ["WIN", "BLACKJACK", "LOSE", "BUST"]:
            if result_type in ["WIN", "BLACKJACK"]:
                bet_text = f"+${bet_amount} Won! 🎯"
                bet_color = "#00ff00"
            else:
                bet_text = f"-${bet_amount} Lost! 💸"
                bet_color = "#ff4444"

            bet_label = tk.Label(
                content_frame,
                text=bet_text,
                font=('Arial', 12, 'bold'),
                bg=bg_color,
                fg=bet_color
            )
            bet_label.pack(pady=(2, 10))

        # Make window appear on top
        self.window.attributes('-topmost', True)
        self.window.focus_force()

        # Auto-close after 1.5 seconds
        self.window.after(1500, self.fade_and_close)

        # Click to close faster
        self.window.bind('<Button-1>', lambda e: self.close())
        content_frame.bind('<Button-1>', lambda e: self.close())
        icon_label.bind('<Button-1>', lambda e: self.close())
        msg_label.bind('<Button-1>', lambda e: self.close())

        # Start with a slide-in animation from right
        self.animate_slide_in()

    def animate_slide_in(self):
        """Slide-in animation from the right"""
        try:
            # Get current position
            current_x = self.window.winfo_x()
            parent_width = self.parent.winfo_width()
            parent_x = self.parent.winfo_x()

            # Calculate target position (top-right)
            target_x = parent_x + parent_width - self.window.winfo_width() - 20

            # If not at target yet, move right
            if current_x < target_x:
                new_x = min(current_x + 30, target_x)
                self.window.geometry(f"+{new_x}+{self.window.winfo_y()}")
                self.window.after(20, self.animate_slide_in)
        except:
            pass

    def fade_and_close(self):
        """Fade out and close"""
        self.fade_step(1.0)

    def fade_step(self, opacity):
        """Step down opacity"""
        if opacity > 0.1:
            opacity -= 0.1
            try:
                self.window.attributes('-alpha', opacity)
                self.window.after(50, lambda: self.fade_step(opacity))
            except:
                self.close()
        else:
            self.close()

    def close(self):
        """Close the popup"""
        try:
            self.window.destroy()
        except:
            pass


class BlackjackGUI:
    def __init__(self, root):
        print("=" * 50)
        print("INITIALIZING BLACKJACK GUI")
        print("=" * 50)

        self.root = root
        self.root.title("♠️ Blackjack Casino ♠️")

        # Get screen dimensions
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Set window size with padding
        window_width = min(1100, screen_width - 100)
        window_height = min(800, screen_height - 100)

        # Calculate center position
        x = max(0, (screen_width - window_width) // 2)
        y = max(0, (screen_height - window_height) // 2)

        print(f"Screen: {screen_width}x{screen_height}")
        print(f"Window: {window_width}x{window_height}")
        print(f"Position: {x}, {y}")

        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.configure(bg='#1a472a')
        self.root.resizable(True, True)
        self.root.minsize(800, 600)

        # Ensure standard window decorations
        self.root.overrideredirect(False)

        # Show window
        self.root.deiconify()
        self.root.lift()
        self.root.focus_force()
        self.root.attributes('-topmost', True)
        self.root.after(200, lambda: self.root.attributes('-topmost', False))

        self.root.update()
        self.root.update_idletasks()

        # Initialize game
        print("1. Creating game instance...")
        self.game = BlackjackGame()
        self.card_images = {}
        self.back_image = None
        self.popup = None

        # Create card images
        print("2. Creating card images...")
        self.create_card_images()

        # Setup UI
        print("3. Setting up UI...")
        self.setup_ui()

        # Initial display
        print("4. Updating display...")
        self.update_display()
        self.update_buttons()

        self.root.update()
        self.root.update_idletasks()

        self.root.lift()
        self.root.focus_force()

        print("5. GUI Initialization Complete!")
        print("=" * 50)

    def create_card_images(self):
        """Create all card images dynamically"""
        try:
            print("   Creating card images...")

            if not os.path.exists('cards'):
                print("   Creating cards directory...")
                os.makedirs('cards')

            screen_width = self.root.winfo_screenwidth()
            card_size = 80 if screen_width < 1200 else 100

            for suit in SUITS:
                for rank in RANKS:
                    img = Image.new('RGB', (card_size, int(card_size * 1.4)), 'white')
                    draw = ImageDraw.Draw(img)
                    draw.rectangle([(2, 2), (card_size - 2, int(card_size * 1.4) - 2)], outline='black', width=2)
                    color = 'red' if suit in ['♥', '♦'] else 'black'

                    try:
                        font_size = max(12, card_size // 5)
                        big_font_size = max(20, card_size // 2)
                        font = ImageFont.truetype("arial.ttf", font_size)
                        big_font = ImageFont.truetype("arial.ttf", big_font_size)
                    except:
                        font = ImageFont.load_default()
                        big_font = ImageFont.load_default()

                    draw.text((card_size // 10, card_size // 10), f"{rank}", fill=color, font=font)
                    draw.text((card_size // 10, card_size // 10 + font_size + 5), f"{suit}", fill=color, font=font)
                    draw.text((card_size - card_size // 4, card_size - font_size - 15), f"{rank}", fill=color,
                              font=font)
                    draw.text((card_size - card_size // 4, card_size - 10), f"{suit}", fill=color, font=font)
                    draw.text((card_size // 3, card_size // 3), f"{suit}", fill=color, font=big_font)

                    filename = f"cards/{rank}_{suit}.png"
                    img.save(filename)

                    img = Image.open(filename)
                    img = img.resize((card_size, int(card_size * 1.4)), Image.Resampling.LANCZOS)
                    self.card_images[f"{rank}{suit}"] = ImageTk.PhotoImage(img)

            print(f"   Created all card images (size: {card_size})")

            # Create back of card
            img = Image.new('RGB', (card_size, int(card_size * 1.4)), '#2c3e50')
            draw = ImageDraw.Draw(img)

            for i in range(0, card_size, 20):
                draw.line([(i, 0), (i, int(card_size * 1.4))], fill='#34495e', width=1)
            for i in range(0, int(card_size * 1.4), 20):
                draw.line([(0, i), (card_size, i)], fill='#34495e', width=1)

            draw.rectangle([(2, 2), (card_size - 2, int(card_size * 1.4) - 2)], outline='#95a5a6', width=2)

            try:
                font = ImageFont.truetype("arial.ttf", card_size // 3)
            except:
                font = ImageFont.load_default()
            draw.text((card_size // 4, card_size // 3), "♠", fill='#95a5a6', font=font)

            img.save("cards/back.png")
            img = Image.open("cards/back.png")
            img = img.resize((card_size, int(card_size * 1.4)), Image.Resampling.LANCZOS)
            self.back_image = ImageTk.PhotoImage(img)
            print("   Back of card created successfully")

        except Exception as e:
            print(f"ERROR in create_card_images: {e}")

    def setup_ui(self):
        """Setup the GUI layout"""
        print("   Setting up UI elements...")

        main_container = tk.Frame(self.root, bg='#1a472a')
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Title
        title_frame = tk.Frame(main_container, bg='#1a472a')
        title_frame.pack(fill=tk.X, pady=5)

        font_size = 24 if self.root.winfo_screenwidth() < 1200 else 32

        tk.Label(
            title_frame,
            text="♠️ BLACKJACK CASINO ♠️",
            font=('Arial', font_size, 'bold'),
            fg='#ffd700',
            bg='#1a472a'
        ).pack()

        # Info frame
        info_frame = tk.Frame(main_container, bg='#1a472a')
        info_frame.pack(fill=tk.X, pady=5)

        font_size = 14 if self.root.winfo_screenwidth() < 1200 else 18

        self.balance_label = tk.Label(
            info_frame,
            text=f"💰 Balance: ${self.game.balance}",
            font=('Arial', font_size),
            fg='white',
            bg='#1a472a'
        )
        self.balance_label.pack(side=tk.LEFT, padx=10)

        self.bet_label = tk.Label(
            info_frame,
            text="",
            font=('Arial', font_size),
            fg='#ffd700',
            bg='#1a472a'
        )
        self.bet_label.pack(side=tk.LEFT, padx=10)

        # Game area
        game_area = tk.Frame(main_container, bg='#1a472a')
        game_area.pack(fill=tk.BOTH, expand=True, pady=5)

        # Dealer section
        dealer_section = tk.Frame(game_area, bg='#1a472a')
        dealer_section.pack(fill=tk.X, pady=5)

        tk.Label(
            dealer_section,
            text="DEALER",
            font=('Arial', 14, 'bold'),
            fg='white',
            bg='#1a472a'
        ).pack()

        self.dealer_cards_frame = tk.Frame(dealer_section, bg='#1a472a')
        self.dealer_cards_frame.pack(pady=5)

        self.dealer_score_label = tk.Label(
            dealer_section,
            text="",
            font=('Arial', 12),
            fg='white',
            bg='#1a472a'
        )
        self.dealer_score_label.pack()

        # Separator
        tk.Frame(game_area, height=2, bg='#ffd700').pack(fill=tk.X, pady=5, padx=20)

        # Player section
        player_section = tk.Frame(game_area, bg='#1a472a')
        player_section.pack(fill=tk.X, pady=5)

        tk.Label(
            player_section,
            text="PLAYER",
            font=('Arial', 14, 'bold'),
            fg='white',
            bg='#1a472a'
        ).pack()

        self.player_cards_frame = tk.Frame(player_section, bg='#1a472a')
        self.player_cards_frame.pack(pady=5)

        self.player_score_label = tk.Label(
            player_section,
            text="",
            font=('Arial', 12),
            fg='white',
            bg='#1a472a'
        )
        self.player_score_label.pack()

        # Control section
        control_section = tk.Frame(main_container, bg='#1a472a')
        control_section.pack(fill=tk.X, pady=5)

        # Betting controls
        bet_frame = tk.Frame(control_section, bg='#1a472a')
        bet_frame.pack(pady=5)

        tk.Label(
            bet_frame,
            text="Bet Amount: $",
            font=('Arial', 12),
            fg='white',
            bg='#1a472a'
        ).pack(side=tk.LEFT, padx=5)

        self.bet_entry = tk.Entry(
            bet_frame,
            width=8,
            font=('Arial', 12),
            justify='center'
        )
        self.bet_entry.pack(side=tk.LEFT, padx=5)
        self.bet_entry.insert(0, "50")

        quick_bets = [25, 50, 100, 200]
        for amount in quick_bets:
            tk.Button(
                bet_frame,
                text=f"${amount}",
                font=('Arial', 9),
                bg='#2c3e50',
                fg='white',
                command=lambda a=amount: self.set_bet(a)
            ).pack(side=tk.LEFT, padx=2)

        # Action buttons
        button_frame = tk.Frame(control_section, bg='#1a472a')
        button_frame.pack(pady=5)

        self.deal_button = tk.Button(
            button_frame,
            text="🃏 DEAL",
            font=('Arial', 12, 'bold'),
            bg='#27ae60',
            fg='white',
            padx=15,
            pady=8,
            command=self.deal
        )
        self.deal_button.pack(side=tk.LEFT, padx=5)

        self.hit_button = tk.Button(
            button_frame,
            text="✋ HIT",
            font=('Arial', 12, 'bold'),
            bg='#2980b9',
            fg='white',
            padx=15,
            pady=8,
            command=self.hit
        )
        self.hit_button.pack(side=tk.LEFT, padx=5)

        self.stand_button = tk.Button(
            button_frame,
            text="✊ STAND",
            font=('Arial', 12, 'bold'),
            bg='#e67e22',
            fg='white',
            padx=15,
            pady=8,
            command=self.stand
        )
        self.stand_button.pack(side=tk.LEFT, padx=5)

        self.new_round_button = tk.Button(
            button_frame,
            text="🔄 NEW",
            font=('Arial', 12, 'bold'),
            bg='#8e44ad',
            fg='white',
            padx=15,
            pady=8,
            command=self.new_round
        )
        self.new_round_button.pack(side=tk.LEFT, padx=5)

        # Status label
        self.status_label = tk.Label(
            main_container,
            text="💰 Place your bet and click DEAL!",
            font=('Arial', 12, 'italic'),
            fg='#ffd700',
            bg='#1a472a'
        )
        self.status_label.pack(pady=5)

        print("   UI Setup complete!")

    def set_bet(self, amount):
        """Quick set bet amount"""
        self.bet_entry.delete(0, tk.END)
        self.bet_entry.insert(0, str(amount))

    def update_buttons(self):
        """Update button states based on game state"""
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

    def show_result_popup(self, result_type, message, bet_amount):
        """Show a quick popup with the result in top-right corner"""
        if self.popup:
            try:
                self.popup.close()
            except:
                pass

        # Show the popup
        self.popup = QuickResultPopup(
            self.root,
            result_type,
            message,
            bet_amount
        )

        # Also update the status label
        self.status_label.config(text=message, fg='#ffd700')

    def deal(self):
        """Handle deal button click"""
        try:
            print("DEAL button clicked!")
            bet_amount = int(self.bet_entry.get())
            print(f"   Bet amount: ${bet_amount}")

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
                self.show_result_popup(result["result"], result["message"], self.game.bet)
                self.update_buttons()

            print(f"   Deal complete. Game state: {self.game.game_state}")
        except ValueError:
            messagebox.showwarning("Invalid Bet", "Please enter a valid number!")
        except Exception as e:
            print(f"ERROR in deal: {e}")

    def hit(self):
        """Handle hit button click"""
        result = self.game.hit()
        self.update_display()
        self.update_balance()

        if result:
            self.update_display(show_all=True)
            self.show_result_popup(result["result"], result["message"], self.game.bet)
            self.update_buttons()

    def stand(self):
        """Handle stand button click"""
        result = self.game.stand()
        self.update_display(show_all=True)
        self.update_balance()

        if result:
            self.show_result_popup(result["result"], result["message"], self.game.bet)
            self.update_buttons()

    def new_round(self):
        """Start a new round"""
        self.game.reset()
        self.update_display()
        self.update_buttons()
        self.update_balance()
        self.status_label.config(text="💰 Place your bet and click DEAL!", fg='#ffd700')

    def update_display(self, show_all=False):
        """Update the card display"""
        state = self.game.get_game_state()

        # Clear frames
        for widget in self.dealer_cards_frame.winfo_children():
            widget.destroy()
        for widget in self.player_cards_frame.winfo_children():
            widget.destroy()

        # Display dealer cards
        dealer_hand = state["dealer_hand"]
        if dealer_hand:
            for i, card in enumerate(dealer_hand):
                if i == 0 and not show_all and state["state"] == "PLAYER_TURN":
                    if self.back_image:
                        img_label = tk.Label(
                            self.dealer_cards_frame,
                            image=self.back_image,
                            bg='#1a472a'
                        )
                    else:
                        img_label = tk.Label(
                            self.dealer_cards_frame,
                            text="??",
                            font=('Arial', 14),
                            bg='#2c3e50',
                            fg='white',
                            width=6,
                            height=4,
                            relief='solid'
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
                            font=('Arial', 12),
                            bg='white',
                            width=6,
                            height=4,
                            relief='solid'
                        )
                img_label.pack(side=tk.LEFT, padx=2)

        # Display player cards
        player_hand = state["player_hand"]
        if player_hand:
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
                        font=('Arial', 12),
                        bg='white',
                        width=6,
                        height=4,
                        relief='solid'
                    )
                img_label.pack(side=tk.LEFT, padx=2)

        # Update scores
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
        """Update balance display"""
        state = self.game.get_game_state()
        self.balance_label.config(text=f"💰 Balance: ${state['balance']}")

        if state['bet'] > 0:
            self.bet_label.config(text=f"💵 Bet: ${state['bet']}")
        else:
            self.bet_label.config(text="")

        if state['balance'] <= 0:
            self.status_label.config(text="💔 You're out of money! Game Over!", fg='#ff0000')
            messagebox.showinfo("Game Over", "You're out of money! Game Over!")


def run_gui():
    """Create and run the GUI"""
    try:
        print("Starting GUI...")
        root = tk.Tk()
        print("Root window created")

        root.overrideredirect(False)
        root.update_idletasks()

        app = BlackjackGUI(root)
        print("App created, starting mainloop...")

        root.deiconify()
        root.lift()
        root.focus_force()
        root.attributes('-topmost', True)
        root.after(300, lambda: root.attributes('-topmost', False))

        root.update()
        root.update_idletasks()

        root.mainloop()

    except Exception as e:
        print(f"FATAL ERROR in run_gui: {e}")
        import traceback
        traceback.print_exc()
        input("Press Enter to exit...")


if __name__ == "__main__":
    run_gui()