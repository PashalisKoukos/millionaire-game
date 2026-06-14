# Who Wants to Be a Millionaire?

A fully featured **Who Wants to Be a Millionaire** quiz game built entirely with Python and Tkinter — no external libraries needed. Answer 15 questions correctly and walk away with **$1,000,000!**

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python) ![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange) ![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 Table of Contents

- [Features](#-features)
- [How to run](#-how-to-run)
- [How to play](#-how-to-play)
- [Lifelines](#-lifelines)
- [Prize Ladder](#-prize-ladder)
- [Project Structure](#-project-structure)
- [License](#-license)

---

## Features

- 15 trivia questions across 5 difficulty levels
- Prize ladder climbing up to **$1,000,000**
- 3 lifelines: **50-50**, **Audience Poll**, **Phone a Friend**
- Safe zones at questions 5 and 10 — guaranteed money
- Stop at any time and keep your current prize
- Full graphical interface built with Tkinter
- In-game rules and external rules link
- Error handling for unexpected crashes

---

## How to run

### Requirements
- Python **3.10** or higher
- Tkinter — comes bundled with Python on **Windows** and **macOS**

### On Linux, install Tkinter separately:
```bash
sudo apt install python3-tk
```

### Run the game:
```bash
python millionaire_gui.py
```

No `pip install` needed — the game uses only Python's standard library.

---

## 🎮 How to play

1. Launch the game — a welcome screen will appear with the rules
2. Press **Start!** to begin
3. Read each question carefully and select one of the four answers (A, B, C, D)
4. Use a **lifeline** if you're unsure — you only have 3 total, so spend them wisely
5. Press **Submit your answer** to confirm your choice
6. If correct, you move on to the next question and win the prize money
7. You can press **Stop** at any time to quit and keep your current winnings
8. Answer all 15 questions correctly to win **$1,000,000!**

### Important rules:
- A wrong answer before **question 5** → you leave with **nothing**
- A wrong answer between questions **5 and 10** → you keep the **question 5 prize**
- A wrong answer after **question 10** → you keep the **question 10 prize**
- Stopping early before question 5 → you leave with **nothing**

---

## Lifelines

You have **3 lifelines** available throughout the entire game. Each can only be used once.

### 50-50
Two wrong answers are removed at random, leaving only the correct answer and one wrong one. The round restarts with just two choices.

### Audience Poll
The virtual audience votes on what they think the correct answer is. Results are shown as percentages — the audience is usually right, but not always!

### Phone a Friend
You get **45 seconds** to "call a friend". A countdown timer starts and a message reminds you to return to your question once time is up.

---

##  Prize Ladder

| # | Question | Prize | |
|---|----------|-------|-|
| 1 | Easiest | $100 | |
| 2 | | $200 | |
| 3 | | $300 | |
| 4 | | $500 | |
| 5 | | $1,000 | ✅ Safe zone |
| 6 | Medium | $2,000 | |
| 7 | | $4,000 | |
| 8 | | $8,000 | |
| 9 | | $16,000 | |
| 10 | | $32,000 | ✅ Safe zone |
| 11 | Hard | $64,000 | |
| 12 | | $125,000 | |
| 13 | | $250,000 | |
| 14 | | $500,000 | |
| 15 | Hardest | $1,000,000 | 🏆 |

✅ = Guaranteed money if you answer wrong after this point
🏆 = You win the game!

---

## 🗂️ Project Structure

```
millionaire-game/
│
├── millionaire_gui.py   # entire game — data, logic, and GUI
└── README.md            # this file
```

### Class overview

| Class | Role |
|-------|------|
| `WelcomeScreen` | Opening window with rules and Start button |
| `Game` | Central controller — tracks round index and remaining lifelines |
| `RoundWindow` | Builds and manages each question window |
| `HelpWindow` | Lifeline selection popup |
| `FiftyFiftyLifeline` | Removes two wrong answers |
| `AudienceLifeline` | Simulates audience vote |
| `PhoneLifeline` | Opens 45-second countdown phone window |
