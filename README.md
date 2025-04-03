# Asteroids
A simple **asteroid spawning system** built with **Pygame**. Asteroids appear from random edges of the screen and move dynamically across the play area.

## 🎮 Features
- **Sprite-based physics** for smooth movement
- **Modular structure** for easy modifications

## ️ Installation
### ️⃣ Clone the Repository
```sh
git clone https://github.com/TheBearguy/asteroids 
cd asteroids
```

### ️⃣ Install Dependencies
Python, then install Pygame:
```sh
pip install pygame
```

### ⃣ Run the Game
```sh
python main.py
```

## Project Structure
```
📦 asteroid-game
├── asteroid_field.py   # Handles asteroid spawning
├── asteroid.py         # Defines asteroid behavior
├── constants.py        # Stores game settings
├── main.py             # Main game loop
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
```

You can tweak the settings inside `constants.py`, such as:
```python
ASTEROID_SPAWN_RATE = 1.5  # Base spawn rate (seconds)
ASTEROID_MAX_RADIUS = 50   # Maximum asteroid size
ASTEROID_MIN_RADIUS = 20   # Minimum asteroid size
SCREEN_WIDTH = 800         # Screen width
SCREEN_HEIGHT = 600        # Screen height
```
---

