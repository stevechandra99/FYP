import pygame
import cv2

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(screen, ic , (x, y, w, h))

    Text_1 = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, Text_1)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(textSurf, textRect)

def webcam():
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()

def quitwindow():
    pygame.quit()
    quit()

# initializing the constructor
pygame.init()

# screen resolution
res = (720, 720)

# opens up a window
screen = pygame.display.set_mode(res)
screen.fill((60, 35, 60))
color = (255, 255, 255)
ic = (170, 170, 170)
ac = (150, 150, 150)
color = (110, 110, 110)
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()

#Set the title of the window
pygame.display.set_caption('Auto Path Planning')

#Define the clock for the module
pygame.time.Clock()
# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
text = smallfont.render('quit', True, color)

while True:

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            pygame.quit()
    largeText = pygame.font.Font('freesansbold.ttf', 30)
    textSurf, textRect = text_objects("Please Click the Desirable Button", largeText)
    textRect = ((width/5), 10)
    screen.blit(textSurf, textRect)
    button("Webcam Stream", 50, 350, 250, 50, ic, ac, webcam)
    button("Quit", 50, 450, 100, 50, color, color_dark, quitwindow)
    pygame.display.update()
'''
    click = pygame.mouse.get_pos()
    #print(mouse)

    if 150+100 > click[0] > 150 and 450 + 50 > click[1] > 450:
        pygame.draw.rect(screen, (150, 150, 150), (150, 450, 100, 50))
    else:
        pygame.draw.rect(screen, color_light, (150, 450, 100, 50))

    Text_1 = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("Try", Text_1)
    textRect.center = ( (150 + (100/2)), (450 + (50/2)))
    screen.blit(textSurf, textRect)
'''
'''
            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:

            # if the mouse is clicked on the
            # button the game is terminated
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.quit()

                # fills the screen with a color
    screen.fill((255, 255, 255))

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
        pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])

    else:
        pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])

        # superimposing the text onto our button
    screen.blit(text, (width / 2 + 50, height / 2))
'''