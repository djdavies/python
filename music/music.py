#!/usr/bin/env python
"""
Click circles, make some sound
"""

import os, pygame

# globals
imagesource1=os.path.join('resources',  'blob1.png')
imagesource2=os.path.join('resources',  'blob2.png')
blob1image= pygame.image.load(imagesource1)
blob2image= pygame.image.load(imagesource2)

#classes
class strobe(pygame.sprite.Sprite):
    ''' displays the moving strobe line and triggers playing notes'''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        self.imagesource=os.path.join('resources',  'strobe.png')
        self.image= pygame.image.load(self.imagesource)
        self.rect=self.image.get_rect()
        self.xpos=0
        self. tempo=5

    def update(self):
        self.xpos += self.tempo
        if self.xpos>=800:
            self.xpos=0
        self.rect.left=self.xpos
        
class blob(pygame.sprite.Sprite):
    '''blobs to click on'''
    def __init__(self):
        # call it on itself
        pygame.sprite.Sprite.__init__(self) 
        # image 
        self.image=blob1image
        # rectangle describing the loaded image
        self.rect=self.image.get_rect()
        self.state= 0
    def toggle(self):
        self.state += 1
        if self.state > 1 :
            self.state = 0
            self.image=blob1image
        else:
            self.image=blob2image


def main():
    """main logic"""
#Initialise all
    pygame.mixer.pre_init(44100,-16,2, 1024)
    pygame.init()
    pygame.mixer.set_num_channels(12)
    screensize=(800, 600)
    screen = pygame.display.set_mode(screensize)
    pygame.display.set_caption('Click Blobs, Make Sounds')
    pygame.mouse.set_visible(1)
    sounds=[]
    for item in range(12):
        source=os.path.join('resources',  'soundsquare'+str(item+1)+'.wav')
        sounds.append(pygame.mixer.Sound(source))
    
    # timer 
    clock = pygame.time.Clock()
    #sprite objects, add to render groups
    spritegroup= pygame.sprite.RenderPlain()
    strobegroup= pygame.sprite.RenderPlain()
    s=strobe()
    s.add(strobegroup)
    cols=[]
    for col in range(16):
        rows=[]
        for row in range(12):
            newblob=blob()
            newblob.rect.top=row*50
            newblob.rect.left=col*50
            rows.append(newblob)
            newblob.add(spritegroup)
        cols.append(rows)
    spritegroup.draw(screen)    

    # control loop
   
    while 1:
        clock.tick(50)
        
        #check what events Pygame has caught
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #determine row and column
                (mx,  my) = pygame.mouse.get_pos()
                mrow=int(my/50)
                mcol=int(mx/50)
                cols[mcol][mrow].toggle()



    #refresh screen, drawing everything again
        strobegroup.update()
        spritegroup.draw(screen)
        strobegroup.draw(screen)
        pygame.display.flip()
        # play sounds? check position of 'scanner'
        if not s.xpos%50:
            #reached a new column
            column=cols[s.xpos/50]
            #go through list of blobs 
            for item in range(12):
                if column[item].state:
                    sounds[item].play()
        # end of playing sequence

if __name__ == '__main__': 
    main()
    pygame.quit()
