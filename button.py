import pygame
import random
import sys
pygame.init()
display = pygame.display.set_mode((650, 350))
white = (255,255,255)
display.fill(white)
button = pygame.image.load("button.png")
button = pygame.transform.scale(button, (200, 200)) # rescale button
display.blit(button, (220, 100))
myfont = pygame.font.SysFont("monospace", 30)
label = myfont.render("MakeSound By Koussay Jaballah, Day3", 1, (0, 0,
0))
display.blit(label, (20, 50))
pygame.display.update()
# assign sound files
blip_sound = pygame.mixer.Sound("easysound.mp3")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.quit()
        # check if button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
            # play sound
                pygame.mixer.Sound.play(blip_sound)


