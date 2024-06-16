# This is Main Driver File This is Responsible for Show Game State and handing inputs.
import pygame as p
from Chess import ChessEngine

WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT / DIMENSION
MAX_FPS = 15
IMAGES = {}


def loadImages():
    pieces = ["wp", "bp", "bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR", "wR", "wN", "wB", "wQ", "wK", "wB", "wN",
              "wR"]
    for piece in pieces:
        IMAGES[piece] = p.transfrom.scale(p.image.load("Images/" + piece + ".png")), (SQ_SIZE, SQ_SIZE)


# a loop to get all the image loaded in variable.

def main():
    p.init()
    screen = p.display.set_mode(WIDTH, HEIGHT)
    clock = p.time.clock()
    screen.fill(p.color("white"))
    gs = ChessEngine.GameState()
    print(gs.borad)
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen, gs):
    drawBoard(screen)  # draw squares

    drawPieces(screen, gs.borad)  # draw piece on square


def drawBoard(screen):
    colors = [p.color("white"), p.color("grey"), ]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[(r + c) % 2]
            p.draw.rect(screen, color, p.rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def drawPieces(screen, board):
    pass


if __name__ == "__main __":
    main()