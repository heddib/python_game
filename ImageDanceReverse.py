import math
import pygame

class ImageDanceReverse (pygame.sprite.Sprite):
  def __init__(self, game, name, width, height, frames):
    super(ImageDanceReverse, self).__init__()
    self.name = name
    self.frames = frames
    self.images = []
    self.loadImages()
    self.image_X = 0
    self.image_Y = game.height/2
    self.game = game
    self.index = 0
    self.image = self.images[self.index]
    self.back = False
    self.rect = pygame.Rect(self.game.width + width + 10, self.game.height / 2, width, height)

  def loadImage(self, name):
    return pygame.image.load(name)

  def loadImages(self):
    for i in range(0, self.frames):
      self.images.append(self.loadImage(self.name+'/frames/'+str(i)+'.gif'))

  def update(self):
    self.index += 0.1
    if self.index >= len(self.images):
      self.index = 0
    self.image = self.images[math.floor(self.index)]
    if self.rect.x <= self.game.width - self.rect.width:
      self.back = True
    if self.back:
      self.rect.x+=1.5
    else:
      self.rect.x-=0.5