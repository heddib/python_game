import pygame

class Ball:
  def __init__(self, game):
    self.ball_img = pygame.image.load('ball.png')
    self.ball_X = game.width/2 - 15
    self.ball_Y = 20
    self.ball_dir_X = -1
    self.ball_dir_Y = -1
    self.game = game
  
  def draw(self):
    self.game.screen.blit(self.ball_img, (self.ball_X, self.ball_Y))