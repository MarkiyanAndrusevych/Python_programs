import pygame
import random

# Constants
WIDTH, HEIGHT = 400, 400  # Window size
GRID_SIZE = 10
MINE_COUNT = 20
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
GRAY = (200, 200, 200)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define constants for game
REVEALED = 0
FLAGGED = 1
HIDDEN = 2


def initialize_board(mine_positions=None):
    if mine_positions is None:
        mine_positions = random.sample(range(GRID_SIZE * GRID_SIZE), MINE_COUNT)
    board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    mine_positions_tuples = []

    for mine in mine_positions:
        x, y = mine % GRID_SIZE, mine // GRID_SIZE
        board[y][x] = -1  # -1 represents a mine
        mine_positions_tuples.append((x, y))  # Store mine positions as tuples

    # Calculate numbers for adjacent mines
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if board[y][x] != -1:
                mines_count = 0
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if 0 <= x + dx < GRID_SIZE and 0 <= y + dy < GRID_SIZE and board[y + dy][x + dx] == -1:
                            mines_count += 1
                if mines_count > 0:
                    board[y][x] = mines_count

    return board, mine_positions_tuples  # Return mine positions as tuples


def draw_board(screen, board, revealed, flagged_cells_positions):
    screen.fill(GRAY)  # Background color

    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            cell_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

            if revealed[y][x]:
                pygame.draw.rect(screen, WHITE, cell_rect)
                if board[y][x] == -1:
                    font = pygame.font.Font(None, 36)
                    text = font.render("X", True, BLACK)
                    text_rect = text.get_rect(center=cell_rect.center)
                    screen.blit(text, text_rect)
                elif board[y][x] == 1:
                    font = pygame.font.Font(None, 36)
                    text = font.render("1", True, BLUE)
                    text_rect = text.get_rect(center=cell_rect.center)
                    screen.blit(text, text_rect)
                elif board[y][x] == 2:
                    font = pygame.font.Font(None, 36)
                    text = font.render("2", True, GREEN)
                    text_rect = text.get_rect(center=cell_rect.center)
                    screen.blit(text, text_rect)
                elif board[y][x] == 3:
                    font = pygame.font.Font(None, 36)
                    text = font.render("3", True, RED)
                    text_rect = text.get_rect(center=cell_rect.center)
                    screen.blit(text, text_rect)
            elif (x, y) in flagged_cells_positions:
                pygame.draw.rect(screen, GRAY, cell_rect)
                pygame.draw.rect(screen, BLACK, cell_rect, 1)
                pygame.draw.polygon(screen, RED, [(cell_rect.x + 18, cell_rect.y + 6),
                                                  (cell_rect.x + 18, cell_rect.y + 30),
                                                  (cell_rect.x + 24, cell_rect.y + 24),
                                                  (cell_rect.x + 18, cell_rect.y + 18)])
            else:
                pygame.draw.rect(screen, GRAY, cell_rect)
                pygame.draw.rect(screen, BLACK, cell_rect, 1)


def draw_button(screen, rect, text):
    pygame.draw.rect(screen, BLACK, rect, 2)

    font = pygame.font.Font(None, 24)
    button_text = font.render(text, True, BLACK)
    text_rect = button_text.get_rect(center=rect.center)
    screen.blit(button_text, text_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("MyMinesweeper")

    revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    flagged_cells = set()
    continue_rect = pygame.Rect(60, HEIGHT - 60, 120, 40)
    new_game_rect = pygame.Rect(220, HEIGHT - 60, 120, 40)

    game_over = False
    board, mine_positions = initialize_board()  # Initialize the board and mine positions

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos[0] // CELL_SIZE, event.pos[1] // CELL_SIZE
                if event.button == 1:  # Left mouse button
                    if not revealed[y][x] and (x, y) not in flagged_cells:
                        revealed[y][x] = True
                        if board[y][x] == -1:
                            # Game over, reveal all mine locations
                            game_over = True
                elif event.button == 3:  # Right mouse button (RMB)
                    if not revealed[y][x]:
                        if (x, y) not in flagged_cells:
                            flagged_cells.add((x, y))
                        else:
                            flagged_cells.remove((x, y))

        if game_over:
            # Reveal mine positions
            for mine_x, mine_y in mine_positions:
                revealed[mine_y][mine_x] = True

        screen.fill(BLACK)
        draw_board(screen, board, revealed, flagged_cells)
        if game_over:
            draw_button(screen, continue_rect, "Continue")
            draw_button(screen, new_game_rect, "New Game")

        # Handle "Continue" button click
        if game_over and continue_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                # Resume the game with the same mine positions
                revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
                flagged_cells.clear()
                game_over = False

        # Handle "New Game" button click
        if new_game_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                # Start a new game
                revealed = [[False for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
                flagged_cells.clear()
                game_over = False
                board, mine_positions = initialize_board()  # Initialize a new board and mine positions

        pygame.display.flip()

if __name__ == "__main__":
    main()








