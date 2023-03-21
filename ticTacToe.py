import utility
import pygame
import ticTacToeAi as ai

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True
board = ['', '', '', '', '', '', '', '', '']
black = (0, 0, 0)
grey = (33, 41, 66, 1)
white = (255, 255, 255)
bgColor = (213, 30, 124, 0.37)
# put all sprites in a group
allSprite = pygame.sprite.Group()
# Rect(left, top, width, height) -> Rect
mainBox = (screen.get_width() / 2 - 300,
           screen.get_height() / 2 - 230, 600, 600)
smallBoxes = [pygame.Rect(mainBox[0], mainBox[1], 200, 200), pygame.Rect(mainBox[0]+200, mainBox[1], 200, 200), pygame.Rect(mainBox[0]+400, mainBox[1], 200, 200),
              pygame.Rect(mainBox[0], mainBox[1]+200, 200, 200), pygame.Rect(mainBox[0]+200, mainBox[1] +
                                                                             200, 200, 200), pygame.Rect(mainBox[0]+400, mainBox[1]+200, 200, 200),
              pygame.Rect(mainBox[0], mainBox[1]+400, 200, 200), pygame.Rect(mainBox[0]+200, mainBox[1]+400, 200, 200), pygame.Rect(mainBox[0]+400, mainBox[1]+400, 200, 200)]
resetimg = pygame.image.load('r.png')
resetbtn = utility.Button(600, 10, resetimg, 0.3)
modebtn = utility.Button(420, 110, None, None)


myfont = pygame.font.Font(None, 100)
title = myfont.render("TIC-TAC-TOE", True, black)
myfontSmall = pygame.font.Font(None, 50)
myfontSmaller = pygame.font.Font(None, 35)
currentX = myfontSmall.render("Current Turn : X", True, black)
currentO = myfontSmall.render("Current Turn : O", True, black)

turn = True
winnerDecided = False
modeI = 0
turns = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and winnerDecided == False:
            # print(pygame.mouse.get_pos())
            if turn and turns <= 8:
                for i, rect in enumerate(smallBoxes):
                    if rect.collidepoint(pygame.mouse.get_pos()):
                        # print(rect.center)
                        if board[i] == '':
                            # then only update
                            turns = turns+1
                            p = utility.Cross(rect.centerx, rect.centery)
                            allSprite.add(p)
                            turn = False
                            board[i] = 'x'
            elif turn == False and turns <= 8:
                # turn == false
                if modeI == 0:
                    # 2 player mode
                    for i, rect in enumerate(smallBoxes):
                        if rect.collidepoint(pygame.mouse.get_pos()):
                            # print(rect.center)
                            if board[i] == '' and not winnerDecided:
                                p = utility.Zero(rect.centerx, rect.centery)
                                allSprite.add(p)
                                turn = True
                                board[i] = 'o'
                                turns = turns+1
                elif modeI == 1:
                    # random
                    i = ai.randompicker(board)
                    rect = smallBoxes[i]
                    p = utility.Zero(rect.centerx, rect.centery)
                    allSprite.add(p)
                    turn = True
                    board[i] = 'o'
                    turns = turns+1
                elif modeI == 2:
                    evall, i = ai.minMax(board, True, 9-turns)
                    # print(evall, i)
                    rect = smallBoxes[i]
                    p = utility.Zero(rect.centerx, rect.centery)
                    allSprite.add(p)
                    turn = True
                    board[i] = 'o'
                    turns = turns+1
                elif modeI == 3:
                    evall, i = ai.alphaBeta(board, True, 9-turns, -10, 10)
                    # print(evall, i)
                    rect = smallBoxes[i]
                    p = utility.Zero(rect.centerx, rect.centery)
                    allSprite.add(p)
                    turn = True
                    board[i] = 'o'
                    turns = turns+1

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((127, 138, 244))
    resetBtnClicked = resetbtn.draw(screen)
    if resetBtnClicked:
        allSprite.empty()
        board = ['', '', '', '', '', '', '', '', '']
        turn = True
        winnerDecided = False
        turns = 0
    screen.blit(title, (mainBox[0], 40))
    winner = utility.checkBoard(board)
    if turn and winner == '' and turns <= 8:
        screen.blit(currentX, (mainBox[0], 120))
    elif not turn and winner == '' and turns <= 8:
        screen.blit(currentO, (mainBox[0], 120))
    else:
        if winner != '':
            winnerText = myfontSmall.render(
                "Winner is " + winner.upper(), True, black)
            screen.blit(winnerText, (mainBox[0], 120))
            winnerDecided = True
        else:
            gameOverText = myfontSmaller.render(
                "Game Over Please Reset", True, grey)
            screen.blit(gameOverText, (mainBox[0], 120))
    modeI = modebtn.draw2(screen)
    mainbox = pygame.draw.rect(screen, grey, mainBox)
    # RENDER YOUR GAME HERE
    for box in smallBoxes:
        r = pygame.draw.rect(screen, white, box, 2)
    allSprite.draw(screen)
    # flip() the display to put your work on screen

    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
