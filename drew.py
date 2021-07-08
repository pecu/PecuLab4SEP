# encoding: utf-8

#-------------------------------------------------------------------------
# 畫Box.
#-------------------------------------------------------------------------
class Box(object):
    #-------------------------------------------------------------------------
    # 建構式.
    #   pygame    : pygame.
    #   canvas    : 畫佈.
    #   name    : 物件名稱.
    #   rect      : 位置、大小.
    #   color     : 顏色.
    #-------------------------------------------------------------------------
    def __init__( self, pygame, canvas, name, rect, color):
        self.pygame = pygame
        self.canvas = canvas
        self.name = name
        self.rect = rect
        self.color = color

        self.visivle = True
        
    #-------------------------------------------------------------------------
    # 更新.
    #-------------------------------------------------------------------------
    def update(self):
        if(self.visivle):
            self.pygame.draw.rect( self.canvas, self.color, self.rect)

#-------------------------------------------------------------------------
# 畫圓.
#-------------------------------------------------------------------------
class Circle(object):
    #-------------------------------------------------------------------------
    # 建構式.
    #   pygame  : pygame.
    #   canvas  : 畫佈.
    #   name    : 物件名稱.
    #   pos     : 位置.  
    #   radius  : 大小.
    #   color   : 顏色.    
    #-------------------------------------------------------------------------
    def __init__( self, pygame, canvas, name, pos, radius, color):
        self.pygame = pygame
        self.canvas = canvas
        self.name = name
        self.pos = pos
        self.radius = radius
        self.color = color
        
        self.visivle = True

    #-------------------------------------------------------------------------
    # 更新.
    #-------------------------------------------------------------------------
    def update(self):
        if(self.visivle):
            self.pygame.draw.circle( self.canvas, self.color, self.pos , self.radius)