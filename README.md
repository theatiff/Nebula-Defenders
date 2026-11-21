# 🚀 Nebula Defenders
 
A fast, retro-style arcade shooter made with **Python** and **Pygame**.
Defend your fleet against waves of alien orbs, manta-bats and crystals, and shoot down the golden bonus ship for extra points.
 
## Features
- Three alien types worth different points (100 / 200 / 300)
- Golden bonus ship that flies across the top for 500 points
- Destructible shields
- 3 lives, score and saved best score
- Scrolling starfield background
- Original sprites, sound effects and music
## Requirements
- Python 3.9 or newer
- Pygame
## Installation
```bash
git clone https://github.com/YOUR-USERNAME/nebula-defenders.git
cd nebula-defenders
pip install pygame
```
 
## Run
```bash
python main.py
```
 
## Controls
| Key | Action |
|-----|--------|
| ← / → | Move ship |
| Space | Shoot (also restarts after Game Over) |
 
## Project structure
```
main.py        game loop, drawing, background
game.py        game rules, collisions, score
alien.py       aliens and bonus ship
spaceship.py   player ship
laser.py       projectiles
obstacle.py    shields
Graphics/      sprites
Sounds/        sound effects and music
Font/          Monogram font
tools/         script that generated the sprites and sounds
```
 
## Credits
- Sprites, sound effects and music: created for this project (see `tools/make_assets.py`).
  
  
## License
Released under the MIT License. See [LICENSE](LICENSE).
 
