import pygame

class Player:
  def __init__(self, game):
    self.player_X_default = game.width/2 - 100
    self.player_X_dif = 0
    self.player_Y = game.height - 80
    self.player_img = pygame.image.load('player.png')
    self.game = game

  def draw(self, x_val):
    self.game.screen.blit(self.player_img, (x_val, self.player_Y))

  def move_left(self, x_val):
    if self.player_X_dif-x_val >= -self.player_X_default+10:
      self.player_X_dif -= x_val

  def move_right(self, x_val):
    if self.player_X_dif+x_val <= self.player_X_default-10:
      self.player_X_dif += x_val