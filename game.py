import pygame, math, functions
from ball import Ball
from ImageDance import ImageDance
from ImageDanceReverse import ImageDanceReverse
from player import Player

class Game:
  def __init__(self, screen, width, height):
    self.screen = screen
    self.width = width
    self.height = height
    self.player = Player(self)
    self.ball = Ball(self)
    self.image = ImageDance(self, 'chika', 331, 498, 26)
    self.image_group = pygame.sprite.Group(self.image)
    self.imageReverse = ImageDanceReverse(self, 'chika', 331, 498, 26)
    self.image_groupReverse = pygame.sprite.Group(self.imageReverse)
    self.score = 0
    self.round = 1
    self.multiplier = 0.5
    self.showAnime = False
    self.showAnimeReverse = False
    self.clock = pygame.time.Clock()

  def game_over(self):
    self.ball.ball_X = self.width/2 - 15
    self.ball.ball_Y = 20
    self.ball.ball_dir_X = -1
    self.ball.ball_dir_Y = -1
    self.score = 0
    self.round = 1

  def updateRound(self):
    self.round += 1
    self.score += 1
    if self.round % 3 == 0:
      self.ball.ball_dir_X -= self.multiplier
      self.ball.ball_dir_Y -= self.multiplier
    if self.round % 5 == 0 and not self.round % 10 == 0:
      self.showAnime = True
      # La musique ne fonctionne pas sur Windows (libmpg123-0.dll: Le module spécifié est introuvable. pygame) donc je l'ai enlevé au cas où :(
      # pygame.mixer.music.load('wow.mp3')
      # pygame.mixer.music.play()
    if self.round % 10 == 0:
      self.showAnimeReverse = True
      # pygame.mixer.music.load('wow.mp3')
      # pygame.mixer.music.play()

  def calc_ball(self):
    if self.ball.ball_Y == 10:
        self.ball.ball_dir_Y *= -1
    elif (self.ball.ball_Y >= self.player.player_Y) and (self.ball.ball_X >= self.player.player_X_default+self.player.player_X_dif-30) and (self.ball.ball_X <= self.player.player_X_default+self.player.player_X_dif+200):
        self.ball.ball_dir_Y *= -1
        self.updateRound()
    elif self.ball.ball_X <= 10:
        self.ball.ball_dir_X *= -1
    elif self.ball.ball_X >= self.width-10-30:
        self.ball.ball_dir_X *= -1

    self.ball.ball_X+=self.ball.ball_dir_X
    self.ball.ball_Y+=self.ball.ball_dir_Y
    if (self.ball.ball_Y >= self.height - 10 - 30):
        self.game_over()
    self.ball.ball_Y = min(self.ball.ball_Y, self.height-10-30)
    self.ball.ball_Y = max(self.ball.ball_Y, 10)

  def drawStats(self):
    font = pygame.font.SysFont('arial', 25)
    self.screen.blit(font.render('Score : '+str(self.score), True, (0, 0, 255)), (10, 10))
    self.screen.blit(font.render('Round : '+str(self.round), True, (0, 0, 255)), (10, 40))
    self.screen.blit(font.render('FPS : '+str(math.trunc(self.clock.get_fps())), True, (0, 0, 255)), (10, 70))

  def update(self):
    self.screen.fill((255,225,226))
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_RIGHT]:
      self.player.move_right(4)
    elif key_input[pygame.K_LEFT]:
      self.player.move_left(4)
    self.player.draw(self.player.player_X_default+self.player.player_X_dif)
    self.calc_ball()
    self.ball.draw()

    if(self.showAnime):
      self.image_group.update()
      self.image_group.draw(self.screen)
    if(self.image.rect.x <= 0 - self.image.rect.width + 10 and self.image.back == True):
      self.showAnime = False
      self.image.back = False

    if(self.showAnimeReverse):
      self.image_groupReverse.update()
      self.image_groupReverse.draw(self.screen)
    if(self.imageReverse.rect.x >= self.width + self.imageReverse.rect.width + 10 and self.imageReverse.back == True):
      self.showAnimeReverse = False
      self.imageReverse.back = False

    self.drawStats()
    self.clock.tick() 
    pygame.display.flip()