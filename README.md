# ♟️ Chess (Pygame)

A lightweight **2D chess game** built with [pygame](https://www.pygame.org/).
Play locally against a simple engine or use it as a base for your own chess experiments.

## ✨ Features

* Interactive **2D chessboard** with piece images
* Click-to-move controls
* Basic move logic & game state tracking (`ChessEngine.py`)
* Works out-of-the-box with `pygame`

## 📦 Requirements

* **Python 3.10+** (tested up to 3.13)
* **pygame ≥ 2.6.1**

Install pygame:

```bash
python -m pip install pygame
```

Or in a virtual environment:

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip pygame
```

## ▶️ Run the game

From the project root:

```bash
python Chess/ChessMain.py
```

Or with an absolute path (Windows example):

```powershell
& C:/Users/BILAL/AppData/Local/Programs/Python/Python313/python.exe c:/Users/BILAL/Documents/GitHub/Chess/Chess/ChessMain.py
```

✅ Images are loaded relative to `ChessMain.py`, so the game runs regardless of your working directory.

## 📂 Project structure

```
Chess/
  ChessMain.py        # GUI & main loop
  ChessEngine.py      # Game state & move logic
  Images/             # Piece images (wp.png, bR.png, ...)
```

## 🛠 Troubleshooting

* **`ModuleNotFoundError: No module named 'Chess'`**
  → Already fixed (now uses `import ChessEngine`).

* **Image load errors**
  → Ensure `Chess/Images/` has all piece PNGs. Errors will print full paths to help debug.

* **No window / pygame crash**
  → Confirm you’re using the same Python environment where `pygame` is installed.

## 🚧 Roadmap

**Short-term**

* Full legal moves (castling, en passant, promotion)
* Undo/redo & move history
* Move highlighting

**Medium-term**

* Stronger engine (minimax + alpha-beta)
* FEN/PGN save & load
* Chess clocks

**Long-term**

* Online multiplayer
* Packaged builds (PyInstaller)
* CI & unit tests

## 🤝 Contributing

Contributions welcome! Open an **issue** or **draft PR** before big changes.

