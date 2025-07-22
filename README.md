# Tic Tac Toe AI using MiniMax Algorithm
- Refer to `tictactoe.py` for a basic CLI version of the algorithm.
- Refer to `tictactoe2.py` for a version complete with UI.

# 🤖 Tic Tac Toe with AI (Minimax Algorithm)

This project is a fully functional **Tic Tac Toe game** built using **Python** and **Pygame**, where a human plays against an unbeatable **AI powered by the Minimax algorithm**.

## 🎮 Gameplay Overview

- 2-player mode: You (player 1 - circles) vs AI (player 2 - crosses)
- The AI uses the **Minimax algorithm** to make the best possible move every turn
- You can restart the game anytime by pressing the **`R` key**
- Green = You win, Red = AI wins, Gray = Draw

## 📦 Features

- Clean GUI built with `pygame`
- AI uses a recursive **Minimax** strategy
- Detects wins in all directions (rows, columns, diagonals)
- Highlights winner with color-coded symbols
- Resets with a single key press (`R`)

## 🧠 AI Strategy: Minimax

- **Maximizing player (AI)**: tries to maximize score
- **Minimizing player (You)**: tries to minimize score
- Scores:

  - Win for AI: `+∞`
  - Win for Player: `-∞`
  - Draw: `0`
- The AI always plays optimally and is unbeatable

## 🖼️ Game UI

- 3x3 grid window
- Circle = Human player (white)
- Cross = AI (white/red)
- Color changes to indicate result:

  - **Green** → You win
  - **Red** → AI wins
  - **Gray** → Draw

## 📂 File Structure

```
tictactoe2.py      # Main game logic and UI
README.md              # This file
```

## 🔧 Requirements

- Python 3.6+
- Pygame

### Install dependencies:

```bash
pip install pygame
```

## ▶️ Running the Game

```bash
python tictactoe2.py
```

Use your mouse to click a square and make a move. Press **`R`** to restart at any time.

## 🧪 Example

```
You click a square → Circle appears
AI plays immediately → Cross appears
Game ends:
- Green shapes if you win
- Red shapes if AI wins
- Gray shapes if it's a draw
```

## **Demo**:
- The player always plays first. 
<img width="365" height="408" alt="image" src="https://github.com/user-attachments/assets/7c39e206-2e7d-4f6b-ae42-4805cdb80307" />
<br>

- If the player loses the board becomes red.

<img width="373" height="407" alt="image" src="https://github.com/user-attachments/assets/5070a960-3eb2-471b-b238-3d717696a94e" />

## 📃 License

This project is released under the [MIT License](LICENSE). Feel free to modify and share!
