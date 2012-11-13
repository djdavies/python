#!/usr/bin/env python
"""
Remove ln 1 if you're on Windows. ./bill.py on Unix.
----------------------------------------------------
This is what friends are for.
"""
#import modules
import os, pygame # you need pygame
from random import choice

#defining classes
class Hammer(pygame.sprite.Sprite):
    #hammer sprite, derived from pygame sprites
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        #hammer img
        self.imagesource=os.path.join('resources',  'hammer1.png')
        self.image= pygame.image.load(self.imagesource)
        # rectangle describing loaded image
        self.rect=self.image.get_rect()
        #trasparent bkgrnd
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)
        #copy for restoring
        self.default=self.image
        self.default_rect=self.rect
        self.whack = 0
        # sound fx
        self.whacksound= pygame.mixer.Sound('resources/whack.wav')

    def update(self):
    #called before redrawing sprites
        #move hammer to mouse pos
        pos = pygame.mouse.get_pos()
        self.rect.center = pos
        #check if hitting
        if self.whack:
            #move sprite a bit +rotate 
            self.rect.move_ip(8, 12)
            self.image = pygame.transform.rotate(self.default, 45)

    def dowhack(self, target):
        #has it hit bill?
        if not self.whack:
            self.whack = 1
            hitrect = self.rect.inflate(-50, -50)
            return hitrect.colliderect(target.rect)

    def reset(self):
        #put hammer up and reset
        self.whack = 0
        self.image=self.default
    
    def playsound(self):
        #plays sound
        self.whacksound.play()



class Bill(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagesource=os.path.join('resources',  'bill.png')
        self.image= pygame.image.load(self.imagesource)
        self.rect=self.image.get_rect()
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)
        self.default=self.image
        self.default_rect=self.rect
        self.owwsound = pygame.mixer.Sound('resources/oww.wav')
        # timer 0 is default means bill not visible
        self.timer=0
        # if 0, bill not hit
        self.whacked=0
        # bill shows up here
        self.locations=[(20, 300), (155, 150), (290, 300),(425, 150),  (600, 300)]
        
    def appear(self): # head appearing
        self.timer=80 # if changed, also alter update method...
        self.loc=choice(self.locations)

    def update(self):
        # checking stuff
        if self.timer:
            # bill exists and visible
            self.timer -= 1 # count down
            if self.timer > 60:
                #appearing
                xpos, ypos=self.loc
                height=self.default.get_height()
                #part of the image to draw
                y=(height/20)*(self.timer-60)
                #copy from backup to main sprite 
                self.image=self.default.subsurface(0,0,self.default.get_width(),height-y)
                self.rect.left=xpos
                #Y position so pops up
                self.rect.top=ypos+y
            if self.timer == 0:
                #finished 
                self.rect=self.default_rect
            if self.timer < 12:
                '''vanish
                appearing but reversed '''
                xpos, ypos=self.loc
                height=self.default.get_height()
                y=(height/12)*self.timer
                self.image=self.default.subsurface(0,0,self.default.get_width(),y)
                self.rect.left=xpos
                self.rect.top=ypos-y+height 
            if self.whacked:
                #'ave it
                self.whacked += 1
                #if hit, rotate sprite 360 
                if self.whacked >= 10:
                    self.whacked = 0
                    self.image = self.default
                else:
                    self.image =pygame.transform.rotate(self.default, self.whacked*36)
                
                
    def is_hit(self):
        #when hit do this
        self.whacked=1
        #poor bill
        self.owwsound.play()
    


def main():
    """the main game logic"""
#initialising stuff
    pygame.init()
    screensize=(800, 600)
    screen = pygame.display.set_mode(screensize)
    pygame.display.set_caption('Good old Bill')
    pygame.mouse.set_visible(0)
    bgsource=os.path.join('resources',  'background.png')
    background = pygame.image.load(bgsource)
    background = background.convert()
    # timer for the game
    clock = pygame.time.Clock()
    hammer = Hammer()
    bill=Bill()
    #add sprites rendering group
    spritegroup= pygame.sprite.RenderPlain(( bill,  hammer))

    # control loop
   
    while 1:
        #adjust this to make game harder /easier
        clock.tick(130)
        
        #check what events are caught
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #button means hammer is being used
                hammer.playsound()
                if hammer.dowhack(bill):
                    bill.is_hit()
            elif event.type is pygame.MOUSEBUTTONUP:
                hammer.reset()
    #does bill show, make him appear
        if bill.timer==0:
            bill.appear()

    #refresh and draw everything
        #update methods on all sprites 
        spritegroup.update()
        #redraw background
        screen.blit(background, (0, 0))
        #draw everything
        spritegroup.draw(screen)
        #flip buffer
        pygame.display.flip()


if __name__ == '__main__': 
    main()
    pygame.quit()
