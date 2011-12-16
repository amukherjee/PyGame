#!/usr/bin/python -tt

import pygame
from pygame.locals import *
from sys import exit

pygame.init()

SCREEN_SIZE = (640, 480)
screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
message = " This is a demonstration of the scrolly messae script.  "
pygame.display.set_caption('Hello World')

background_image_filename = 'data/noserape.jpg'
background = pygame.image.load(background_image_filename).convert()
font  = pygame.font.SysFont("arial",80);
text_surface = font.render(message, True, (0, 0, 255))
x = 0
y = (SCREEN_SIZE[1] - text_surface.get_height())/2



while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()

  screen.blit(background, (0,0))

  x-= 2
  if x < -text_surface.get_width():
    x= 0
  screen.blit(text_surface, (x, y))
  screen.blit(text_surface, (x+text_surface.get_width(), y))
  pygame.display.update()
