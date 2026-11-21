# 🚀 NEBULA DEFENDERS

**NEBULA DEFENDERS** is a space shooter arcade game developed using Python and Pygame. Take control of a spaceship, defend against waves of alien invaders, destroy enemy ships, and earn points to beat your highest score.

## 🎮 Game Overview

Protect your spaceship from incoming alien attacks. Move left and right, fire lasers, and destroy enemies before they reach you.

Watch out for the mysterious bonus ship. Destroying it gives you extra points!

## ✨ Features

- 🚀 Player-controlled spaceship.
- 👾 Multiple types of alien enemies.
- 🔫 Laser shooting mechanics.
- 🛸 Mystery ship with bonus points.
- 🛡️ Destructible protective obstacles.
- ❤️ Three lives per game.
- ⭐ Score and high-score tracking.
- 🎵 Background music and sound effects.
- 🌌 Animated starfield background.
- 🔄 Restart option after Game Over.

## 🕹️ Controls

| Key | Action |
|---|---|
| ← Left Arrow | Move spaceship left |
| → Right Arrow | Move spaceship right |
| Space | Fire lasers |
| Space | Restart after Game Over |

## 🛠️ Technologies Used

- **Python** – Main programming language.
- **Pygame** – Game development library.
- **Random** – Random enemy and mystery ship behavior.

## 📁 Project Structure

```text
NEBULA_DEFENDERS/
│
├── Font/
│   └── monogram.ttf
│
├── Graphics/
│   ├── alien_1.png
│   ├── alien_2.png
│   ├── alien_3.png
│   ├── spaceship.png
│   └── mystery.png
│
├── Sounds/
│   ├── laser.wav
│   ├── explosion.wav
│   └── music.wav
│
├── tools/
│   └── make_assets.py
│
├── main.py
├── game.py
├── spaceship.py
├── alien.py
├── laser.py
├── obstacle.py
├── highscore.txt
├── requirements.txt
├── LICENSE
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/theatiff/NEBULA_DEFENDERS.git
```

### 2. Navigate to the Project Folder

```bash
cd NEBULA_DEFENDERS
```

### 3. Install Dependencies

```bash
pip install pygame
```

### 4. Run the Game

```bash
python main.py
```

## 🏆 Scoring System

- Destroying alien enemies earns points based on their type.
- Destroying the mystery ship awards **500 points**.
- Your best score is saved in `highscore.txt`.

## 🎯 Objective

Survive as long as possible, destroy alien invaders, protect your spaceship, and achieve the highest score!

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Credits

- Game graphics, sound effects, and music were created for this project.
- Font: Monogram by datagoblin (CC0 / Public Domain).

---

**Developed by ORCUS**

⭐ If you enjoy the game, consider giving this repository a star!
