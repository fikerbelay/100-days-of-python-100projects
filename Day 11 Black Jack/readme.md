♠️ Blackjack Casino 🃏

A fully-featured Blackjack game with a modern GUI interface, built with Python and Tkinter. Experience the thrill of the casino with realistic gameplay, beautiful card graphics, and smooth animations.

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Tkinter](https://img.shields.io/badge/tkinter-GUI-orange.svg)

🎯 Features

###  Gameplay
- **Full Blackjack Rules**: Hit, Stand, Deal, and New Round functionality
- **Smart Dealer AI**: Dealer hits on 16, stands on 17
- **Ace Handling**: Automatic conversion of Ace from 11 to 1 when needed
- **Blackjack Detection**: Instant win detection with 3:2 payout
- **Betting System**: Place bets from $25 to $200 or custom amounts

###  Visual Design
- **Casino Theme**: Professional green felt background with gold accents
- **Card Graphics**: Dynamically generated playing cards with proper suits
- **Responsive Layout**: Adapts to different screen sizes
- **Interactive Buttons**: Visual feedback for all game actions
- **Result Popups**: Smooth notifications in the top-right corner with slide-in animations

###  User Experience
- **Intuitive Controls**: Simple click-based gameplay
- **Quick Bets**: One-click betting with preset amounts
- **Real-time Updates**: Instant score and balance updates
- **Win/Loss Animations**: Visual feedback for game results
- **Keyboard Shortcuts**: Escape key to close popups

##  Project Structure

```
blackjack/
├── main.py              # Entry point and package manager
├── gui.py               # Main GUI interface with popup system
├── game_logic.py        # Core game logic and rules
├── card_utils.py        # Card and deck classes
├── constants.py         # Game constants (suits, ranks, values)
├── cards/               # Dynamically generated card images
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

##  Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Quick Start

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/blackjack-casino.git
cd blackjack-casino
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install Pillow
```

3. **Run the game:**
```bash
python main.py
```

## 🎯 How to Play

### Basic Rules
1. **Objective**: Get a hand value closer to 21 than the dealer without going over
2. **Card Values**: 
   - Number cards: Face value (2-10)
   - Face cards (J, Q, K): 10 points
   - Ace: 11 points (or 1 point if 11 would bust)

### Game Flow
1. **Place Your Bet**: Enter an amount or use quick bet buttons ($25, $50, $100, $200)
2. **Click DEAL**: Two cards are dealt to you and the dealer
3. **Your Turn**: 
   - **HIT**: Take another card
   - **STAND**: Keep your current hand
4. **Dealer's Turn**: Dealer automatically plays (hits on 16, stands on 17)
5. **Results**: Win, lose, or push (tie) with visual feedback

### Winning Payouts
- **Standard Win**: 2x your bet
- **Blackjack**: 2.5x your bet (3:2 payout)
- **Push (Tie)**: Bet returned
- **Loss**: Bet lost

### Controls
- **DEAL**: Start a new round with current bet
- **HIT**: Take another card
- **STAND**: Keep your hand and let dealer play
- **NEW**: Start a new round after game over
- **Quick Bets**: $25, $50, $100, $200
- **Custom Bet**: Enter any amount in the bet field

s comprehensive and covers everything from installation to gameplay. You can customize the email and GitHub URL at the bottom to your own! 🎰 
