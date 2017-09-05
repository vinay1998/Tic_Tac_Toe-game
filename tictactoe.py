import pygame,sys
from pygame.locals import *

pygame.init()

#dimensions
box_width,box_height=50,50
gap=5
x,y=115,90
clicks=[0]*9

box=[['a','b','c'],['d','e','f'],['g','h','i']]
user=1
game=True

#colors
green=(0,255,0)
black=(0,0,0)
white=(255,255,255)
ia_box=(255,178,102)
a_box=(255,128,0)


surface_obj=pygame.display.set_mode((400,400))
pygame.display.set_caption('Tic Tac Toe')
surface_obj.fill(white)
fontObject = pygame.font.Font("freesansbold.ttf",15)
textSurfaceObj=fontObject.render("'X' user:"+str(1)+" chance...",True,(0,0,0))
textRectObj=textSurfaceObj.get_rect()
textRectObj.bottomright=(390,390)
surface_obj.blit(textSurfaceObj,textRectObj)    

def reset_button():
    pygame.draw.rect(surface_obj,(255,0,0),(140,320,106,30))
    fontObject = pygame.font.Font("freesansbold.ttf",20)
    textSurfaceObj=fontObject.render("RESET",True,(255,255,255))
    textRectObj=textSurfaceObj.get_rect()
    textRectObj.center=((140+(106/2)), (320+(30/2)))
    surface_obj.blit(textSurfaceObj,textRectObj)
    

def check(box,user,clicks,surface_obj):
    if box[0][0]==box[1][1] and box[1][1]==box[2][2]:
        fontObject = pygame.font.Font("freesansbold.ttf",20)
        textSurfaceObj=fontObject.render("user "+str(user)+" won ",True,(0,0,255))
        textRectObj=textSurfaceObj.get_rect()
        textRectObj.topleft=(x+25,y+(3*box_height)+(3*(gap+5)))
        surface_obj.blit(textSurfaceObj,textRectObj)
        pygame.draw.rect(surface_obj,(255,255,255),(0,370,400,30))
        reset_button()
        return False
        
    elif box[0][2]==box[1][1] and box[1][1]==box[2][0]:
        fontObject = pygame.font.Font("freesansbold.ttf",20)
        textSurfaceObj=fontObject.render("user "+str(user)+" won ",True,(0,0,255))
        textRectObj=textSurfaceObj.get_rect()
        textRectObj.topleft=(x+25,y+(3*box_height)+(3*(gap+5)))
        surface_obj.blit(textSurfaceObj,textRectObj)
        pygame.draw.rect(surface_obj,(255,255,255),(0,370,400,30))
        reset_button()
        return False
        
    else:
        count=0
        for i in range(3):
            if box[i][0]==box[i][1] and box[i][1]==box[i][2]:
                fontObject = pygame.font.Font("freesansbold.ttf",20)
                textSurfaceObj=fontObject.render("user "+str(user)+" won ",True,(0,0,255))
                textRectObj=textSurfaceObj.get_rect()
                textRectObj.topleft=(x+25,y+(3*box_height)+(3*(gap+5)))
                surface_obj.blit(textSurfaceObj,textRectObj)
                pygame.draw.rect(surface_obj,(255,255,255),(0,370,400,30))
                reset_button()
                return False
            elif box[0][i]==box[1][i] and box[1][i]==box[2][i]:
                fontObject = pygame.font.Font("freesansbold.ttf",20)
                textSurfaceObj=fontObject.render("user "+str(user)+" won ",True,(0,0,255))
                textRectObj=textSurfaceObj.get_rect()
                textRectObj.topleft=(x+25,y+(3*box_height)+(3*(gap+5)))
                surface_obj.blit(textSurfaceObj,textRectObj)
                pygame.draw.rect(surface_obj,(255,255,255),(0,370,400,30))
                reset_button()
                return False
        for j in range(9):
            if clicks[j]!=0:
                count=count+1
        if count==9:
            fontObject = pygame.font.Font("freesansbold.ttf",20)
            textSurfaceObj=fontObject.render("Draw Match",True,(0,0,255))
            textRectObj=textSurfaceObj.get_rect()
            textRectObj.topleft=(x+25,y+(3*box_height)+(3*(gap+5)))
            surface_obj.blit(textSurfaceObj,textRectObj)
            pygame.draw.rect(surface_obj,(255,255,255),(0,370,400,30))
            reset_button()
            return False
    return True

                
            
def mouse_position(clicks,x,y,box_width,box_height,gap,a_box,ia_box,surface_obj,user,box):

    game=True
    
    mouse_pos=pygame.mouse.get_pos()

    #box1
    if clicks[0]==0:
        if x<=mouse_pos[0]<=x+box_width and y<=mouse_pos[1]<=y+box_height:      
            pygame.draw.rect(surface_obj,a_box,(x,y,box_width,box_height))
            mouse_press=pygame.mouse.get_pressed()
            if mouse_press[0]==1 and clicks[0]==0:
                if(user==1):
                    box[0][0]='X'
                else:
                    box[0][0]='O'
                
                mouse_click(x,y,box_width,box_height,surface_obj,clicks[0],user)
                clicks[0]=1
                game=check(box,user,clicks,surface_obj)
        else:
            pygame.draw.rect(surface_obj,ia_box,(x,y,box_width,box_height))
            
    posx=x+box_width+gap
    posy=y
     
    #box2
    if clicks[1]==0:
        if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
            pygame.draw.rect(surface_obj,a_box,(posx,posy,box_width,box_height)) 
            mouse_press=pygame.mouse.get_pressed()
            if mouse_press[0]==1 and clicks[1]==0:
                if(user==1):
                    box[0][1]='X'
                else:
                    box[0][1]='O'
                mouse_click(posx,posy,box_width,box_height,surface_obj,clicks[1],user)
                clicks[1]=1
                game=check(box,user,clicks,surface_obj)
        else:
            pygame.draw.rect(surface_obj,ia_box,(posx,posy,box_width,box_height))
            
    posx=posx+box_width+gap

    #box3
    if clicks[2]==0:
        if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
            pygame.draw.rect(surface_obj,a_box,(posx,posy,box_width,box_height))
            mouse_press=pygame.mouse.get_pressed()
            if mouse_press[0]==1 and clicks[2]==0:
                if(user==1):
                    box[0][2]='X'
                else:
                    box[0][2]='O'
                
                mouse_click(posx,posy,box_width,box_height,surface_obj,clicks[2],user)
                clicks[2]=1
                game=check(box,user,clicks,surface_obj)
        else:
            pygame.draw.rect(surface_obj,ia_box,(posx,posy,box_width,box_height))
    posx=x
    posy=y+box_height+gap

    #box4
    if clicks[3]==0:
        if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
            pygame.draw.rect(surface_obj,a_box,(posx,posy,box_width,box_height))
            mouse_press=pygame.mouse.get_pressed()
            if mouse_press[0]==1 and clicks[3]==0:
                if(user==1):
                    box[1][0]='X'
                else:
                    box[1][0]='O'
                
                mouse_click(posx,posy,box_width,box_height,surface_obj,clicks[3],user)
                clicks[3]=1
                game=check(box,user,clicks,surface_obj)
        else:
            pygame.draw.rect(surface_obj,ia_box,(posx,posy,box_width,box_height))
    posx=posx+box_width+gap

    #box5
    if clicks[4]==0:
        if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
            pygame.draw.rect(surface_obj,a_box,(posx,posy,box_width,box_height))
            mouse_press=pygame.mouse.get_pressed()
            if mouse_press[0]==1 and clicks[4]==0:
                if(user==1):
                    box[1][1]='X'
                else:
                    box[1][1]='O'
                
                mouse_click(posx,posy,box_width,box_height,surface_obj,clicks[4],user)
                clicks[4]=1
                game=check(box,user,clicks,surface_obj)
        else:
            pygame.draw.rect(surface_obj,ia_box,(posx,posy,box_width,box_height))
    posx=posx+box_width+gap

    #box6
    if clicks[5]==0:
        if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
            pygame.draw.rect(surface_obj,a_box,(posx,posy,box_width,box_height))
            mouse_press=pygame.mouse.get_pressed()
            if mouse_press[0]==1 and clicks[5]==0:
                if(user==1):
                    box[1][2]='X'
                else:
                    box[1][2]='O'
                
                mouse_click(posx,posy,box_width,box_height,surface_obj,clicks[5],user)
                clicks[5]=1
                game=check(box,user,clicks,surface_obj)
        else:
            pygame.draw.rect(surface_obj,ia_box,(posx,posy,box_width,box_height))
    posx=x
    posy=posy+box_height+gap

    #box7
    if clicks[6]==0:
        if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
            pygame.draw.rect(surface_obj,a_box,(posx,posy,box_width,box_height))
            mouse_press=pygame.mouse.get_pressed()
            if mouse_press[0]==1 and clicks[6]==0:
                if(user==1):
                    box[2][0]='X'
                else:
                    box[2][0]='O'
                
                mouse_click(posx,posy,box_width,box_height,surface_obj,clicks[6],user)
                clicks[6]=1
                game=check(box,user,clicks,surface_obj)
        else:
            pygame.draw.rect(surface_obj,ia_box,(posx,posy,box_width,box_height))
    posx=posx+box_width+gap

    #box8
    if clicks[7]==0:
        if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
            pygame.draw.rect(surface_obj,a_box,(posx,posy,box_width,box_height))
            mouse_press=pygame.mouse.get_pressed()
            if mouse_press[0]==1 and clicks[7]==0:
                if(user==1):
                    box[2][1]='X'
                else:
                    box[2][1]='O'
                
                mouse_click(posx,posy,box_width,box_height,surface_obj,clicks[7],user)
                clicks[7]=1
                game=check(box,user,clicks,surface_obj)
        else:
            pygame.draw.rect(surface_obj,ia_box,(posx,posy,box_width,box_height))
    posx=posx+box_width+gap

    #box9
    if clicks[8]==0:
        if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
            pygame.draw.rect(surface_obj,a_box,(posx,posy,box_width,box_height))
            mouse_press=pygame.mouse.get_pressed()
            if mouse_press[0]==1 and clicks[8]==0:
                if(user==1):
                    box[2][2]='X'
                else:
                    box[2][2]='O'
                mouse_click(posx,posy,box_width,box_height,surface_obj,clicks[8],user)
                clicks[8]=1
                game=check(box,user,clicks,surface_obj)
        else:
            pygame.draw.rect(surface_obj,ia_box,(posx,posy,box_width,box_height))
    return game

def user_msg(surface_obj,user):
    pygame.draw.rect(surface_obj,(255,255,255),(0,370,400,30))
    fontObject = pygame.font.Font("freesansbold.ttf",15)
    if user==1:
        textSurfaceObj=fontObject.render("'X' user:"+str(user)+" chance...",True,(0,0,0))
    else:
        textSurfaceObj=fontObject.render("'O' user:"+str(user)+" chance...",True,(0,0,0))
    textRectObj=textSurfaceObj.get_rect()
    textRectObj.bottomright=(390,390)
    surface_obj.blit(textSurfaceObj,textRectObj)    



def mouse_click(posx,posy,box_width,box_height,surface_obj,clicks,user):
    
    if clicks==0:
        if user==1:
            pygame.draw.rect(surface_obj,(255,128,0),(posx,posy,box_width,box_height))
            fontObject = pygame.font.Font("freesansbold.ttf",20)
            textSurfaceObj=fontObject.render("X",True,(255,255,255))
            textRectObj=textSurfaceObj.get_rect()
            textRectObj.center=((posx+(box_width/2)), (posy+(box_height/2)))
            surface_obj.blit(textSurfaceObj,textRectObj)
            user_msg(surface_obj,2)

        else:
            pygame.draw.rect(surface_obj,(255,128,0),(posx,posy,box_width,box_height))
            fontObject = pygame.font.Font("freesansbold.ttf",20)
            textSurfaceObj=fontObject.render("O",True,(255,255,255))
            textRectObj=textSurfaceObj.get_rect()
            textRectObj.center=((posx+(box_width/2)), (posy+(box_height/2)))
            surface_obj.blit(textSurfaceObj,textRectObj)
            user_msg(surface_obj,1)
            

#gameloop
while True:
    
    for event in pygame.event.get():
        if game:            
            game=mouse_position(clicks,x,y,box_width,box_height,gap,a_box,ia_box,surface_obj,user,box)
            if event.type==MOUSEBUTTONUP:
                
                mouse_pos=pygame.mouse.get_pos()
                
                #box1
                if clicks[0]==1:
                    if x<=mouse_pos[0]<=x+box_width and y<=mouse_pos[1]<=y+box_height:
                        clicks[0]=2
                        if user==1:
                            user=2
                        else:
                            user=1
                posx=x+box_width+gap
                posy=y
                
                #box2
                if clicks[1]==1:
                    if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
                        clicks[1]=2
                        if user==1:
                            user=2
                        else:
                            user=1
                posx=posx+box_width+gap
                #box3
                if clicks[2]==1:
                    if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
                        clicks[2]=2
                        if user==1:
                            user=2
                        else:
                            user=1
                posx=x
                posy=y+box_height+gap
                #box4
                if clicks[3]==1:
                    if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
                        clicks[3]=2
                        if user==1:
                            user=2
                        else:
                            user=1
                posx=posx+box_width+gap
                #box5
                if clicks[4]==1:
                    if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
                        clicks[4]=2
                        if user==1:
                            user=2
                        else:
                            user=1
                posx=posx+box_width+gap

                #box6
                if clicks[5]==1:
                    if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
                        clicks[5]=2
                        if user==1:
                            user=2
                        else:
                            user=1
                posx=x
                posy=posy+box_height+gap
                    

                #box7
                if clicks[6]==1:
                    if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
                        clicks[6]=2
                        if user==1:
                            user=2
                        else:
                            user=1
                posx=posx+box_width+gap

                #box8
                if clicks[7]==1:
                    if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
                        clicks[7]=2
                        if user==1:
                            user=2
                        else:
                            user=1
                posx=posx+box_width+gap

                #box9
                if clicks[8]==1:
                    if posx<=mouse_pos[0]<=posx+box_width and posy<=mouse_pos[1]<=posy+box_height:
                        clicks[8]=2
                        if user==1:
                            user=2
                        else:
                            user=1
        else:
            mouse_pos=pygame.mouse.get_pos()
            if 140<=mouse_pos[0]<=140+106 and 320<=mouse_pos[1]<=320+30:
                pygame.draw.rect(surface_obj,(255,255,255),(140,320,106,30))
                fontObject = pygame.font.Font("freesansbold.ttf",20)
                textSurfaceObj=fontObject.render("RESET",True,(255,0,0))
                textRectObj=textSurfaceObj.get_rect()
                textRectObj.center=((140+(106/2)), (320+(30/2)))
                surface_obj.blit(textSurfaceObj,textRectObj) 
                mouse_press=pygame.mouse.get_pressed()
                if mouse_press[0]==1:
                    clicks=[0]*9
                    box=[['a','b','c'],['d','e','f'],['g','h','i']]
                    user=1
                    game=True
                    surface_obj.fill(white)
                    fontObject = pygame.font.Font("freesansbold.ttf",15)
                    textSurfaceObj=fontObject.render("'X' user:"+str(1)+" chance...",True,(0,0,0))
                    textRectObj=textSurfaceObj.get_rect()
                    textRectObj.bottomright=(390,390)
                    surface_obj.blit(textSurfaceObj,textRectObj)
            else:
                reset_button()
                    
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
        
    pygame.display.update()



