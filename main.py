import pygame;
from board_loc import*
from images import *
from string import ascii_uppercase

pygame.init()
screen_width, screen_height = 800, 800
scaling_factor = 1
clicked = False
click1 = False
# with reference to the board
click1_pos = 0
moves = 0
click2 = False
# with reference to the board
click2_pos = 0

screen = pygame.display.set_mode((screen_width, screen_height))

board = [
    [14,12,13,15,16,13,12,14],
    [11,11,11,11,11,11,11,11],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [21,21,21,21,21,21,21,21],
    [24,22,23,25,26,23,22,24]

]




def draw_board ():
    screen.blit(chess_board,(0,0))


def draw_piece():
    for i in range (8):
        for x in range (8):
            a = (x)*100
            b = (i)*100
            # for black pieces
            if board [i][x] < 20 and board [i][x] > 0:
                if board [i][x] == 11:
                    screen.blit(black_pawn,(a,b))
                elif board [i][x] == 12:
                    screen.blit(black_knight,(a,b))
                elif board [i][x] == 13:
                    screen.blit(black_bishop,(a,b))
                elif board [i][x] == 14:
                    screen.blit(black_rook,(a,b))
                elif board [i][x] == 15:
                    screen.blit(black_queen,(a,b))
                elif board [i][x] == 16:
                    screen.blit(black_king,(a,b))
            # white pieces
            elif board [i][x] > 20:
                if board [i][x] == 21:
                    screen.blit(white_pawn,(a,b))
                elif board [i][x] == 22:
                    screen.blit(white_knight,(a,b))
                elif board [i][x] == 23:
                    screen.blit(white_bishop,(a,b))
                elif board [i][x] == 24:
                    screen.blit(white_rook,(a,b))
                elif board [i][x] == 25:
                    screen.blit(white_queen,(a,b))
                elif board [i][x] == 26:
                    screen.blit(white_king,(a,b))

# check if there is a piece in the mouse_position
def check_piece(x,y):
    first = int(y/100)
    second = int(x/100)
    return board[first][second]

def check_piecev2(y,x):
    return board[y][x]

def get_pos(x,y):
    first = int(y/100)
    second = int(x/100)
    return first,second

# check who's turn it is
def check_turn():
    # for white
    if moves % 2 == 0:
        return True
    # for black
    elif moves % 2 == 1:
        return False

# moving a piece to the wanted location
def move_piece(old,new,move):
    if board[new[0]][new[1]] != board[old[0]][old[1]]:
        board[new[0]][new[1]] = board[old[0]][old[1]]
        board[old[0]][old[1]] = 0
        move = moves + 1
        return move

def append_arr(arr1,arr2,new_x,new_y,turn):
    # white
    if turn == True:
        # use black to check if move position in enemy or empty
        if black[0] < check_piecev2(new_y,new_x) < black[1] or check_piecev2(new_y,new_x) == 0:
            arr1.append(new_y),arr2.append(new_x)
            return arr1, arr2
    # black
    if turn == False:
        if white[0] < check_piecev2(new_y,new_x) < white[1] or check_piecev2(new_y,new_x) == 0:
            arr1.append(new_y), arr2.append(new_x)
            return arr1, arr2
        

def pawn_rule(pos,turn):
    vertical = []
    horizontal = []
    ver = pos[0]
    hor = pos[1]
#     # for white
    if turn == True:
        if ver == 6:
            temp = append_arr(vertical,horizontal,ver-2,hor,turn)
            vertical = temp[0]
            horizontal = temp[1]
        if ver < 7:
            append_arr(vertical,horizontal,ver-1,hor,turn)






run = True
while run:
    draw_board()
    draw_piece()
    mouse_pos = pygame.mouse.get_pos()
    clicks = pygame.mouse.get_pressed()

    # event is stuff happening to the mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            check = check_piece(mouse_pos[0],mouse_pos[1])
            # check if the first click is an empty piece
            if check != 0 and click1 == False:
                turn = check_turn()
                if turn == True and check > 20:
                    click1_pos = get_pos(mouse_pos[0],mouse_pos[1])
                    click1 = True
                elif turn == False and check < 20:
                    click1_pos = get_pos(mouse_pos[0],mouse_pos[1])
                    click1 = True
            elif click1 == True:
                click2_pos = get_pos(mouse_pos[0],mouse_pos[1])
                click2 = True

            # This part is for the moving of the pieces after the click
            if click1 == True and click2 == True:
                moves = move_piece(click1_pos,click2_pos,moves)
                click1 = False
                click2 = False

            clicked = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and clicked:
            clicked = False


    # pygame.draw.rect(screen, white, (x, y, rect_width, rect_height))
    pygame.display.update()

pygame.quit()

