import os
import pygame as pg  # Use lower case 'pg' for convention
import ChessEngine

WIDTH = HEIGHT = 400
DIMENSION = 8
SQ_SIZE = HEIGHT // DIMENSION  # Use floor division for integer size
MAX_FPS = 15
IMAGES = {}


def load_images():
    # unique list of piece image names used by the engine
    pieces = ["wp", "bp", "bR", "bN", "bB", "bQ", "bK", "wR", "wN", "wB", "wQ", "wK"]
    # Build absolute path to the Images directory relative to this file
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, "Images")
    for piece in pieces:
        image_path = os.path.join(images_dir, f"{piece}.png")
        try:
            image = pg.image.load(image_path)
            IMAGES[piece] = pg.transform.scale(image, (SQ_SIZE, SQ_SIZE))
        except Exception as e:
            # Print full path and the exception to make debugging easier
            print(f"Error loading image: {image_path} -> {e}")

    # Consider adding default placeholder image for missing pi


def main():
    pg.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("Chess Game")  # Set window caption

    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    gs = ChessEngine.GameState()
    print(gs.board)

    load_images()
    running = True
    sqSelected = ()  # no square is selected, it is a tuple means it store row and col (x,y)
    playerClicks = []  # keeps track of players click these are two tuples [(x,y),(x,y)]
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            # Handle other game events (e.g., mouse clicks for piece movement)
            elif event.type == pg.MOUSEBUTTONDOWN:
                location = pg.mouse.get_pos()
                row = location[1] // SQ_SIZE
                col = location[0] // SQ_SIZE
                if sqSelected == (row, col):  # it means that user wants to de select
                    sqSelected = ()  # Resetting the sqSelected
                    playerClicks = []  # Resetting the playerClicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected)
                if len(playerClicks) == 2:
                    move = ChessEngine.move(playerClicks[0], playerClicks[1], gs.board)
                    gs.makeMove(move)
                    sqSelected = ()
                    playerClicks = []


        clock.tick(MAX_FPS)
        draw_game_state(screen, gs)
        pg.display.flip()


def draw_game_state(screen, gs):
    draw_board(screen)
    draw_pieces(screen, gs.board)


def draw_board(screen):
    colors = [pg.Color("white"), pg.Color("gray")]  # Use American spelling for color
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            pg.draw.rect(screen, color, pg.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def draw_pieces(screen, board):
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            piece = board[row][col]
            # engine represents empty squares as "--"
            if piece != "--":
                image = IMAGES.get(piece)
                if image:  # Check if image is loaded
                    screen.blit(image, (col * SQ_SIZE, row * SQ_SIZE))
if __name__ == "__main__":
    main()