import pygame

class Player:
  def __init__(self,x,y,z,sp,key1,key2,key3,key4,dive,jump):
    self.loc=[x,y,z]
    self.speed=sp
    self.keys=[key1,key2,key3,key4,dive,jump]
    self.h=10
    self.w=10

#fast easy to gain momentum though hard to stop
#screen shake when hitting something
#low air mobility
  def move(self,speed,pressed):
    if pressed(self.keys[0]):
      self.loc[0]-self.speed
    if pressed(self.keys[1]):
      self.loc[0]+self.speed

    if pressed(self.keys[2]):
      self.loc[1]-self.speed
    if pressed(self.keys[3]):
      self.loc[1]+self.speed
#dive
    if pressed(self.keys[4]):
      self.loc[2]-1
#jump
    if pressed(self.keys[5]):
      self.loc[2]+1

  def draw(self,screen):
    self.rect=pygame.draw.rect(screen,(142,0,53),self.loc[0],self.loc[1],self.h,self.w)




# maybe check a 5 block radius or dimeter around the player and enemies

#use the rect to find the locations edit th
  def collision(self,rect):
    for i in range (len(rect)):
      if self.rect.colliderect((rect[i])):
        
        #change the i statement to suit more object on the map
        if i<2:
          self.qual[0]=-self.qual[0]
        else:
          self.qual[1]=-self.qual[1]

  