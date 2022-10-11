import pygame
import math

pygame.init()

width = 400
height = 650

# WINDOW AND FONTS


wind = pygame.display.set_mode((width, height))
pygame.display.set_caption('Calculator')

black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
grey = (169, 169, 169)

font = pygame.font.Font(None, 50)

holy = [[20, 140, "OFF"], [115, 140, "ON"], [210, 140, "%"], [305, 140, "CE"], [20, 242, "7"], [115, 242, "8"],
        [210, 242, "9"], [305, 242, "÷"], [20, 344, "4"], [115, 344, "5"], [210, 344, "6"], [305, 344, "x"],
        [20, 446, "1"], [115, 446, "2"], [210, 446, "3"], [305, 446, "-"], [20, 548, "0"], [115, 548, "."],
        [210, 548, "="], [305, 548, "+"]]


# DRAWING CALCULATOR

wind.fill(black)
pygame.draw.rect(wind, white, pygame.Rect(20, 20, 360, 100))

# DRAW RECTANGLES
st = 20
ht = 140
for t in range(1, 6):
    for p in range(1, 5):
        pygame.draw.rect(wind, white, pygame.Rect(st, ht, 75, 82))
        st += 95
    ht += 102
    st = 20

# DRAW TEXT

for x in range(0, 20):
    text = font.render(holy[x][2], True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (holy[x][0] + 36, holy[x][1] + 41)
    wind.blit(text, textRect)
pygame.display.update()


# TOP CALCULATOR

stuff = ""
stuff1 = ["", "", "", ""]
total = 0
used = False

running = 0

def top(need, it):
    if it != 3 and it != 18:
        global font
        global stuff1
        global total
        global used
        global running
        stuff1[3] = stuff1[2]
        stuff1[2] = stuff1[1]
        stuff1[1] = stuff1[0]
        stuff1[0] = need
        global stuff
        if it == 11:
            need = '*'
        if it == 7:
            need = '/'
        stuff += str(need)
        pygame.draw.rect(wind, white, pygame.Rect(20, 20, 360, 100))
        cool = 370
        for x in range(0, 4):
            text = font.render(stuff1[x], True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.midright = (cool, 70)
            cool -= 95
            wind.blit(text, textRect)
    elif it == 3:
        stuff = ""
        stuff1 = ["", "", "", ""]
        pygame.draw.rect(wind, white, pygame.Rect(20, 20, 360, 100))
        running = 0
    elif it == 18:
        running = 0
        stuff1 = ["", "", "", ""]
        place = eval(stuff)
        place = math.ceil(place * 1000) / 1000
        stuff = str(place)
        stuff1[0] = stuff
        pygame.draw.rect(wind, white, pygame.Rect(20, 20, 360, 100))
        text = font.render(stuff, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.midright = (370, 70)
        used = True
        wind.blit(text, textRect)





running = 0
Fine = True
On = True

while On:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            On = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            posx, posy = pygame.mouse.get_pos()
            for x in range(0, 20):
                if holy[x][0] <= posx <= (holy[x][0] + 75) and holy[x][1] <= posy <= (holy[x][1] + 82):
                    if x == 0:
                        used = False
                        Fine = False
                        stuff = ""
                        wind.fill(black)
                        pygame.draw.rect(wind, grey, pygame.Rect(20, 20, 360, 100))

                        st = 20
                        ht = 140
                        for t in range(1, 6):
                            for p in range(1, 5):
                                pygame.draw.rect(wind, grey, pygame.Rect(st, ht, 75, 82))
                                st += 95
                            ht += 102
                            st = 20

                        pygame.draw.rect(wind, red, pygame.Rect(20, 140, 75, 82))
                        pygame.draw.rect(wind, green, pygame.Rect(115, 140, 75, 82))

                        for x in range(0, 20):
                            text = font.render(holy[x][2], True, (0, 0, 0))
                            textRect = text.get_rect()
                            textRect.center = (holy[x][0] + 36, holy[x][1] + 41)
                            wind.blit(text, textRect)

                        pygame.display.update()
                    if used:
                        if x == 2 or x == 3 or x == 7 or x == 11 or x == 15 or x == 19:
                            running += 1
                            font = pygame.font.Font(None, 50)
                            pygame.draw.rect(wind, blue, pygame.Rect(holy[x][0], holy[x][1], 75, 82))
                            text = font.render(holy[x][2], True, (0, 0, 0))
                            textRect = text.get_rect()
                            textRect.center = (holy[x][0] + 36, holy[x][1] + 41)
                            wind.blit(text, textRect)
                            top(holy[x][2], x)
                            used = False
                            font = pygame.font.Font(None, 50)
                            pygame.display.update()
                            pygame.time.delay(300)
                            pygame.draw.rect(wind, white, pygame.Rect(holy[x][0], holy[x][1], 75, 82))
                            text = font.render(holy[x][2], True, (0, 0, 0))
                            textRect = text.get_rect()
                            textRect.center = (holy[x][0] + 36, holy[x][1] + 41)
                            wind.blit(text, textRect)
                            pygame.display.update()
                    elif not used:
                        if not Fine:
                            if x == 1:
                                Fine = True;
                                running = 0
                                stuff = ""
                                stuff1 = ["", "", "", ""]
                                wind.fill(black)
                                pygame.draw.rect(wind, white, pygame.Rect(20, 20, 360, 100))

                                st = 20
                                ht = 140
                                for t in range(1, 6):
                                    for p in range(1, 5):
                                        pygame.draw.rect(wind, white, pygame.Rect(st, ht, 75, 82))
                                        st += 95
                                    ht += 102
                                    st = 20

                                for x in range(0, 20):
                                    text = font.render(holy[x][2], True, (0, 0, 0))
                                    textRect = text.get_rect()
                                    textRect.center = (holy[x][0] + 36, holy[x][1] + 41)
                                    wind.blit(text, textRect)
                                pygame.display.update()
                        if Fine and x != 1:
                            if running == 0:
                                if x != 0 and x != 2 and x != 7 and x != 11 and x != 15 and x != 19:
                                    running += 1
                                    font = pygame.font.Font(None, 50)
                                    pygame.draw.rect(wind, blue, pygame.Rect(holy[x][0], holy[x][1], 75, 82))
                                    text = font.render(holy[x][2], True, (0, 0, 0))
                                    textRect = text.get_rect()
                                    textRect.center = (holy[x][0] + 36, holy[x][1] + 41)
                                    wind.blit(text, textRect)
                                    top(holy[x][2], x)
                                    font = pygame.font.Font(None, 50)
                                    pygame.display.update()
                                    pygame.time.delay(300)
                                    pygame.draw.rect(wind, white, pygame.Rect(holy[x][0], holy[x][1], 75, 82))
                                    text = font.render(holy[x][2], True, (0, 0, 0))
                                    textRect = text.get_rect()
                                    textRect.center = (holy[x][0] + 36, holy[x][1] + 41)
                                    wind.blit(text, textRect)
                                    pygame.display.update()
                            else:
                                font = pygame.font.Font(None, 50)
                                pygame.draw.rect(wind, blue, pygame.Rect(holy[x][0], holy[x][1], 75, 82))
                                text = font.render(holy[x][2], True, (0, 0, 0))
                                textRect = text.get_rect()
                                textRect.center = (holy[x][0] + 36, holy[x][1] + 41)
                                wind.blit(text, textRect)
                                top(holy[x][2], x)
                                font = pygame.font.Font(None, 50)
                                pygame.display.update()
                                pygame.time.delay(300)
                                pygame.draw.rect(wind, white, pygame.Rect(holy[x][0], holy[x][1], 75, 82))
                                text = font.render(holy[x][2], True, (0, 0, 0))
                                textRect = text.get_rect()
                                textRect.center = (holy[x][0] + 36, holy[x][1] + 41)
                                wind.blit(text, textRect)
                                pygame.display.update()





pygame.quit()
