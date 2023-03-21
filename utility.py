import pygame


cross = pygame.image.load('x.png')
cross = pygame.transform.scale(cross, (100, 100))
zero = pygame.image.load('z.png')
zero = pygame.transform.scale(zero, (100, 100))
grey = (33, 41, 66, 1)


class Cross(pygame.sprite.Sprite):
    def __init__(self, cx, cy):
        pygame.sprite.Sprite.__init__(self)
        self.image = cross
        # self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.center = (cx, cy)


class Zero(pygame.sprite.Sprite):
    def __init__(self, cx, cy):
        pygame.sprite.Sprite.__init__(self)
        self.image = zero
        # self.image.fill(black)
        self.rect = self.image.get_rect()
        self.rect.center = (cx, cy)


def checkBoard(board) -> str:
    if board[4] == 'x' or board[4] == 'o':
        current = board[4]
        if current == board[0] and current == board[8]:
            return current
        if current == board[1] and current == board[7]:
            return current
        if current == board[2] and current == board[6]:
            return current
        if current == board[3] and current == board[5]:
            return current
    if board[8] == 'x' or board[8] == 'o':
        current = board[8]
        if current == board[2] and current == board[5]:
            return current
        if current == board[6] and current == board[7]:
            return current
    if board[0] == 'x' or board[0] == 'o':
        current = board[0]
        if current == board[2] and current == board[1]:
            return current
        if current == board[3] and current == board[6]:
            return current
    return ''


# for my own debuging
def drawGrid(board):
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("-----------")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("-----------")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])


class Button():
    def __init__(self, x, y, image, scale):
        if image:
            width = image.get_width()
            height = image.get_height()
            self.image = pygame.transform.scale(
                image, (int(width * scale), int(height * scale)))
            self.rect = self.image.get_rect()
        else:
            self.rect = pygame.Rect(x, y, 175, 44)
        self.rect.topleft = (x, y)
        self.clicked = False
        self.i = 0

    def draw(self, surface):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # draw button on screen
        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

    def draw2(self, surface):

        # get mouse position
        pos = pygame.mouse.get_pos()

        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.i = (self.i+1) % 4

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        myfont = pygame.font.Font(None, 50)
        title0 = myfont.render("2 player", True, (0, 0, 0))
        title1 = myfont.render("Random", True, (0, 0, 0))
        title2 = myfont.render("MinMax", True, (0, 0, 0))
        title3 = myfont.render("AplhaBeta", True, (0, 0, 0))
        # draw button on screen

        if self.i == 0:
            pygame.draw.rect(surface, (11, 227, 69), self.rect)
            surface.blit(title0, (self.rect.x+5, self.rect.y+5))
        elif self.i == 1:
            pygame.draw.rect(surface, (11, 220, 227), self.rect)
            surface.blit(title1, (self.rect.x+5, self.rect.y+5))
        elif self.i == 2:
            pygame.draw.rect(surface, (11, 94, 227), self.rect)
            surface.blit(title2, (self.rect.x+5, self.rect.y+5))
        else:
            pygame.draw.rect(surface, (182, 209, 6), self.rect)
            surface.blit(title3, (self.rect.x+5, self.rect.y+5))

        return self.i
