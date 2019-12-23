from pygame import * #all graphics programs will need this
from random import *
from tkinter import *
from math import *
import os
import pygame

pygame.init() #sound
pygame.mixer.init() #sound
pygame.mixer.pre_init(22050,-16,2,2048) #sound

root=Tk()
root.withdraw()
init()
font.init()
###########################-Centering Screen-#############################
inf=display.Info() 
w,h=inf.current_w,inf.current_h
os.environ['SDL_VIDEO_WINDOW_POS']='25,25'
screen=display.set_mode((w-50,h-50),NOFRAME)
for x in range(0,screen.get_width(),10):
    draw.line(screen,(0,0,255),(x,0),(x,screen.get_height()))
display.flip()
#################################-Colours-################################
RED  =(255,0,0) #tuple - a list that can not be changed!
GREEN=(0,255,0)
BLUE= (0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
MYYELLOW=(204,224,90)
GOLD=(214, 200, 10)
GREY=(175,180,188)
################################-Basic Sizes-#############################
size=(1279,775) #screen resolution
screen=display.set_mode(size)#creating a 800x600 window
display.set_caption("Spongebob Meme Paint Project")
canvasRect=Rect(350,125,900,500)
################################-Variables-##############################
index=0 #for music
paused=False #for music
r=5 #for spray paint
##########################-FONTS-##############################
spongefont=font.SysFont("Krabby Patty",25) #title font
spongefont2=font.SysFont("Krabby Patty", 15) #body text font
##########################-All the Text-################################
penciltitle=spongefont.render("PENCIL TOOL",0,BLACK)
penciltext=spongefont2.render("This tool allows the user to draw thin lines",0,BLACK)
erasertitle=spongefont.render("ERASER TOOL",0,BLACK)
erasertext=spongefont2.render("This tool allows the user to erase mistakes",0,BLACK)
highlightertitle=spongefont.render("HIGHLIGHTER TOOL",0,BLACK)
highlightertext=spongefont2.render("This tool allows the user to draw transparent red circles",0,BLACK)
brushtitle=spongefont.render("BRUSH TOOL",0,BLACK)
brushtext=spongefont2.render("This tool allows the user to draw medium-sized lines",0,BLACK)
markertitle=spongefont.render("MARKER TOOL",0,BLACK)
markertext=spongefont2.render("This tool allows the user to draw thich lines",0,BLACK)
filltitle=spongefont.render("FILL TOOL",0,BLACK)
filltext=spongefont2.render("This tool allows the user to select a colour and fill an enclosed area with the colour chosen",0,BLACK)
ellipsetitle=spongefont.render("ELLIPSE TOOL",0,BLACK)
ellipsetext=spongefont2.render("This tool allows the user to draw an empty ellipse",0,BLACK)
filledellipsetitle=spongefont.render("FILLED ELLIPSE TOOL",0,BLACK)
filledellipsetext=spongefont2.render("This tool allows the user to draw a filled ellipse",0,BLACK)
recttitle=spongefont.render("RECTANGLE TOOL",0,BLACK)
recttext=spongefont2.render("This tool allows the user to draw an empty rectangle",0,BLACK)
filledrecttitle=spongefont.render("FILLED RECTANGLE TOOL",0,BLACK)
filledrecttext=spongefont2.render("This tool allows the user to draw a filled rectangle",0,BLACK)
linetitle=spongefont.render("LINE TOOL",0,BLACK)
linetext=spongefont2.render("This tool allows the user to draw a line",0,BLACK)
spraytitle=spongefont.render("SPRAY TOOL",0,BLACK)
spraytext=spongefont2.render("This tool mimics a spray paint. Use scroller to adjust size",0,BLACK)
freeformtitle=spongefont.render("FREEFORM TOOL",0,BLACK)
freeformtext=spongefont2.render("This tool allows the user to click points and lines will be",0,BLACK)
freeformtext2=spongefont2.render("drawn between the points. If the user clicks ENTER, a line",0,BLACK)
freeformtext3=spongefont2.render("will be drawn from the last point clicked to the first point",0,BLACK)
droppertitle=spongefont.render("DROPPER TOOL",0,BLACK)
droppertext=spongefont2.render("This tool allows the user to select a colour on the canvas",0,BLACK)
droppertext2=spongefont2.render("The colour selected will be the colour used by the tools",0,BLACK)
colourselect=spongefont2.render("Colour may be adjusted by using the palette",0,BLACK)
stamp1title=spongefont.render("STAMP 1",0,BLACK)
stamp1text=spongefont2.render("This stamp is known as Primal Spongebob",0,BLACK)
stamp2title=spongefont.render("STAMP 2",0,BLACK)
stamp2text=spongefont2.render("This stamp is known as Squidward",0,BLACK)
stamp3title=spongefont.render("STAMP 3",0,BLACK)
stamp3text=spongefont2.render("This stamp is known as Flabbergasted Star",0,BLACK)
stamp4title=spongefont.render("STAMP 4",0,BLACK)
stamp4text=spongefont2.render("This stamp is known as Handsome Squidward",0,BLACK)
stamp5title=spongefont.render("STAMP 5",0,BLACK)
stamp5text=spongefont2.render("This stamp is known as Jolly Sandy",0,BLACK)
stamp6title=spongefont.render("STAMP 6",0,BLACK)
stamp6text=spongefont2.render("This stamp is known as Greedy Pearl",0,BLACK)
stamp7title=spongefont.render("STAMP 7",0,BLACK)
stamp7text=spongefont2.render("This stamp is known as Krazy Krabs",0,BLACK)
stamp8title=spongefont.render("STAMP 8",0,BLACK)
stamp8text=spongefont2.render("This stamp is known as Pineapple Under the Sea",0,BLACK)
#############################-Subsurface-################################
brushHead=Surface((50,50),SRCALPHA)#20x20 surface
draw.circle(brushHead,(255,0,0,30),(25,25),10)
########################-Rectangle Positions(tools)-#####################
pencilRect=Rect(350,635,60,60)
eraserRect=Rect(350,705,60,60)
markerRect=Rect(420,635,60,60)
brushRect=Rect(420,705,60,60)
highlighterRect=Rect(490,635,60,60)
fillRect=Rect(490,705,60,60)
ellipseRect=Rect(560,635,60,60)
rectRect=Rect(560,705,60,60)
filledellipseRect=Rect(630,635,60,60)
filledrectRect=Rect(630,705,60,60)
lineRect=Rect(700,635,60,60)
sprayRect=Rect(700,705,60,60)
freeformRect=Rect(770,635,60,60)
dropperRect=Rect(770,705,60,60)
saveRect=Rect(10,10,50,50)
openRect=Rect(70,10,50,50)
undoRect=Rect(130,10,50,50)
redoRect=Rect(190,10,50,50)
######################-Rectangle Positions (stickers)-###################
stick1Rect=Rect(350,13,100,100)
stick2Rect=Rect(464,13,100,100)
stick3Rect=Rect(579,13,100,100)
stick4Rect=Rect(694,13,100,100)
stick5Rect=Rect(809,13,100,100)
stick6Rect=Rect(924,13,100,100)
stick7Rect=Rect(1039,13,100,100)
stick8Rect=Rect(1154,13,100,100)
########################-Other Rectangles Positions######################
colRect=Rect(270,515, 70,250)
colBorder=Rect(270,515,70,250)
clearRect=Rect(270,465,100,75)
paletteRect=Rect(10,515,250,250)
backRect=Rect(10,415,80,80)
playpauseRect=Rect(95,415,80,80)
forwardRect=Rect(180,415,80,80)
###############################-Info Box-################################
infoRect=Rect(840,635,410,130)
infoborderRect=Rect(840,635,410,130)
###########################-Loading Images-##############################
bikinibottom=image.load("images/Bikini_Bottom.jpg")
palette=image.load("images/map-saturation.png")
pencil=image.load("images/pencil.png")
pencilBW=image.load("images/pencilBW.png")
eraser=image.load("images/Eraser.png")
eraserBW=image.load("images/EraserBW.png")
dropper=image.load("images/dropper.png")
dropperBW=image.load("images/dropperBW.png")
brush=image.load("images/brush.png")
brushBW=image.load("images/brushBW.png")
marker=image.load("images/marker.png")
markerBW=image.load("images/markerBW.png")
highlighter=image.load("images/highlighter.png")
highlighterBW=image.load("images/highlighterBW.png")
rect=image.load("images/rect.png")
rectBW=image.load("images/rectBW.png")
filledrect=image.load("images/filledrect.png")
filledrectBW=image.load("images/filledrectBW.png")
line=image.load("images/line.png")
lineBW=image.load("images/lineBW.png")
clearbutton=image.load("images/clear.png")
clearbuttonD=image.load("images/clearD.png")
textbox=image.load("images/textbox.png")
textboxBW=image.load("images/textboxBW.png")
fill=image.load("images/fill.png")
fillBW=image.load("images/fillBW.png")
spray=image.load("images/spray.png")
sprayBW=image.load("images/sprayBW.png")
ellipse=image.load("images/ellipse.png")
ellipseBW=image.load("images/ellipseBW.png")
filledellipse=image.load("images/filledellipse.png")
filledellipseBW=image.load("images/filledellipseBW.png")
freeform=image.load("images/freeform.png")
freeformBW=image.load("images/freeformBW.png")
undo=image.load("images/undo.png")
redo=image.load("images/redo.png")
save=image.load("images/save.png")
saveBW=image.load("images/save.png")
open1=image.load("images/open.png")
openBW=image.load("images/openBW.png")
title=image.load("images/logo.png")
pause=image.load("images/pause.png")
play=image.load("images/play.png")
fastforward=image.load("images/fastforward.png")
backwards=image.load("images/backwards.png")
#############################-Stamps-###################################
sticker1=image.load("images/primsponge.png")
sticker2=image.load("images/Squidward.png")
sticker3=image.load("images/patrick.png")
sticker4=image.load("images/Handsome.png")
sticker5=image.load("images/Sandy.png")
sticker6=image.load("images/pearl.png")
sticker7=image.load("images/krabs.png")
sticker8=image.load("images/sbhouse.png")
############################-Stamp Icons-###############################
icon1=image.load("images/stick1ICON.png")
icon1BW=image.load("images/stick1ICONBW.png")
icon2=image.load("images/stick2ICON.png")
icon2BW=image.load("images/stick2ICONBW.png")
icon3=image.load("images/stick3ICON.png")
icon3BW=image.load("images/stick3ICONBW.png")
icon4=image.load("images/stick4ICON.png")
icon4BW=image.load("images/stick4ICONBW.png")
icon5=image.load("images/stick5ICON.png")
icon5BW=image.load("images/stick5ICONBW.png")
icon6=image.load("images/stick6ICON.png")
icon6BW=image.load("images/stick6ICONBW.png")
icon7=image.load("images/stick7ICON.png")
icon7BW=image.load("images/stick7ICONBW.png")
icon8=image.load("images/stick8ICON.png")
icon8BW=image.load("images/stick8ICONBW.png")
##############################-Resizing-##################################
paletteSmall=transform.scale(palette,(250,250))
background=transform.scale(bikinibottom,(1279,775))
sticker1=transform.scale(sticker1,(200,150))
pencilSmall=transform.scale(pencil,(80,82))
pencilBWSmall=transform.scale(pencilBW,(80,82))
eraserSmall=transform.scale(eraser,(60,60))
eraserBWSmall=transform.scale(eraserBW,(60,60))
dropperSmall=transform.scale(dropper,(60,60))
dropperBWSmall=transform.scale(dropperBW,(60,60))
brushSmall=transform.scale(brush,(60,60))
brushBWSmall=transform.scale(brushBW,(60,60))
markerSmall=transform.scale(marker,(60,60))
markerBWSmall=transform.scale(markerBW,(60,60))
highlighterSmall=transform.scale(highlighter,(60,60))
highlighterBWSmall=transform.scale(highlighterBW,(60,60))
rectSmall=transform.scale(rect,(60,60))
rectBWSmall=transform.scale(rectBW,(60,60))
filledrectSmall=transform.scale(filledrect,(60,60))
filledrectBWSmall=transform.scale(filledrectBW,(60,60))
lineSmall=transform.scale(line,(60,60))
lineBWSmall=transform.scale(lineBW,(60,60))
textboxSmall=transform.scale(textbox,(60,6))
textboxBWSmall=transform.scale(textboxBW,(60,60))
fillSmall=transform.scale(fill,(60,60))
fillBWSmall=transform.scale(fillBW,(60,60))
spraySmall=transform.scale(spray,(60,60))
sprayBWSmall=transform.scale(sprayBW,(60,60))
ellipseSmall=transform.scale(ellipse,(60,60))
ellipseBWSmall=transform.scale(ellipseBW,(60,60))
filledellipseSmall=transform.scale(filledellipse,(60,60))
filledellipseBWSmall=transform.scale(filledellipseBW,(60,60))
freeformSmall=transform.scale(freeform,(60,60))
freeformSmallBW=transform.scale(freeformBW,(60,60))
clearbuttonS=transform.scale(clearbutton,(70,45))
clearbuttonDS=transform.scale(clearbuttonD,(70,45))
undo=transform.scale(undo,(50,50))
redo=transform.scale(redo,(50,50))
saveSmall=transform.scale(save,(50,50))
saveSmallBW=transform.scale(saveBW,(50,50))
openSmall=transform.scale(open1,(50,50))
openSmallBW=transform.scale(openBW,(50,50))
play=transform.scale(play,(80,80))
pause=transform.scale(pause,(80,80))
fastforward=transform.scale(fastforward,(80,80))
backwards=transform.scale(backwards,(80,80))
###########################-Resizing Stamps-############################
primspongeSM=transform.scale(sticker1,(100,100))
sticker2=transform.scale(sticker2,(103,297))
sticker3=transform.scale(sticker3,(235,329))
sticker4=transform.scale(sticker4,(237,211))
sticker6=transform.scale(sticker6,(150,200))
#########################-Resizing Stamp Icons-############################
stick1=transform.scale(icon1,(100,100))
stick1BW=transform.scale(icon1BW,(100,100))
stick2=transform.scale(icon2,(100,100))
stick2BW=transform.scale(icon2BW,(100,100))
stick3=transform.scale(icon3,(100,100))
stick3BW=transform.scale(icon3BW,(100,100))
stick4=transform.scale(icon4,(100,100))
stick4BW=transform.scale(icon4BW,(100,100))
stick5=transform.scale(icon5,(100,100))
stick5BW=transform.scale(icon5BW,(100,100))
stick6=transform.scale(icon6,(100,100))
stick6BW=transform.scale(icon6BW,(100,100))
stick7=transform.scale(icon7,(100,100))
stick7BW=transform.scale(icon7BW,(100,100))
stick8=transform.scale(icon8,(100,100))
stick8BW=transform.scale(icon8BW,(100,100)) 
#######################MUSIC IMPORTS####################################
file1="Audio/1.mp3"
file2="Audio/2.mp3"
file3="Audio/3.mp3"
file4="Audio/4.mp3"
file5="Audio/5.mp3"
file6="Audio/6.mp3"
file7="Audio/7.mp3"
file8="Audio/8.mp3"
file9="Audio/9.mp3"
file10="Audio/10.mp3"
file11="Audio/11.mp3"
file12="Audio/12.mp3"
file13="Audio/13.mp3"
file14="Audio/14.mp3"
file15="Audio/15.mp3"
file16="Audio/16.mp3"
file17="Audio/17.mp3"
file18="Audio/18.mp3"
file19="Audio/19.mp3"
file20="Audio/20.mp3"
file21="Audio/21.mp3"
file22="Audio/22.mp3"
file23="Audio/23.mp3"
file24="Audio/24.mp3"

music=[] #adding all files to a list
music.append(file1)
music.append(file2)
music.append(file3)
music.append(file4)
music.append(file5)
music.append(file6)
music.append(file7)
music.append(file8)
music.append(file9)
music.append(file10)
music.append(file11)
music.append(file12)
music.append(file13)
music.append(file14)
music.append(file15)
music.append(file16)
music.append(file17)
music.append(file18)
music.append(file19)
music.append(file20)
music.append(file21)
music.append(file22)
music.append(file23)
music.append(file24)

shuffle(music) #shuffling music 
cSong=music[index] #current song
pygame.mixer.music.load(cSong) #loading to mixer
pygame.mixer.music.play() #playing music
END_MUSIC_EVENT=pygame.USEREVENT+0 #loops music
pygame.mixer.music.set_endevent(END_MUSIC_EVENT)
###############################-Defaults-################################
tool="pencil" #default tool
omx,omy=300,300 #defining omx,omy
col=RED #default colour


running=True
########################-Drawing and Bliting Images-######################
screen.blit(background,(0,0)) #bliting background
screen.blit(paletteSmall,(10,515)) #bliting palette
draw.rect(screen,(214, 200, 10),(10,515,250,250),3)#palette border
draw.rect(screen,WHITE,canvasRect) #drawing canvas
screen.blit(title,(25,5)) #bliting title picutre
draw.circle(screen,WHITE,(135,455),40)
screen.blit(play,(playpauseRect)) #play
screen.blit(backwards,(backRect)) #back
screen.blit(fastforward,(forwardRect)) #forward
############################-Undo Redo Lists-##############################
firstpic=screen.subsurface(canvasRect).copy()
undolist=[firstpic] #so there's not an empty list to start with
redolist=[]

myClock=time.Clock()
while running:
    click=False
    for evt in event.get():
        #print(evt)
        if evt.type==QUIT:
            running=False
        if evt.type==KEYDOWN:
            if evt.key==K_ESCAPE:
                running=False
        if evt.type==MOUSEBUTTONUP and canvasRect.collidepoint(mx,my):
            undopic=screen.subsurface(canvasRect).copy() 
            undolist.append(undopic)
        if evt.type==MOUSEBUTTONDOWN:
            shapeBack=screen.subsurface(canvasRect).copy() #copying screen
            cmx,cmy=mx,my #for pencil, brush, eraser, and marker tool
            omx,omy=mx,my #for line tool
            if evt.button==1: #left click
                start=evt.pos
                startx,starty=mx,my
                back=screen.copy() 
                click=True
            if evt.button==4 and r<20: #scroll up to adjust spray thickness, capped at 20
                r+=1
            if evt.button==5 and r>1: #scroll down to adjust spray thickness, minimum is 1
                r-=1
            if undoRect.collidepoint(mx,my) and len(undolist)>0:
                redolist.append(undolist[-1]) #adding the pic to redolist
                undolist.pop() #deleting it from undo list
                screen.blit(undolist[-1],(canvasRect)) #bliting old pic
            if redoRect.collidepoint(mx,my) and len(redolist)>0:
                undolist.append(redolist[-1]) #adding the pic to undolist
                redolist.pop() #deleting it from the redolist
                screen.blit(undolist[-1],(canvasRect)) #bliting old pic
                
        
            
    mx,my=mouse.get_pos()
    mb=mouse.get_pressed()
    ############-Drawing Rectangle That Shows User Colour Selected-#############
    draw.rect(screen,col,colRect,0)
    draw.rect(screen,GOLD,colBorder,3)#border
    ###########################-Bliting Images in Rectangles-####################
    #If the user hovers over the tool, the picture becomes Black and White
    screen.blit(pencilSmall,(338,627,60,60))
    if pencilRect.collidepoint(mx,my):
        screen.blit(pencilBWSmall,(338,627,60,60))
    screen.blit(eraserSmall,(eraserRect))
    if eraserRect.collidepoint(mx,my):
        screen.blit(eraserBWSmall,(eraserRect))
    screen.blit(brushSmall,(brushRect))
    if brushRect.collidepoint(mx,my):
        screen.blit(brushBWSmall,(brushRect))
    screen.blit(markerSmall,(markerRect))
    if markerRect.collidepoint(mx,my):
        screen.blit(markerBWSmall,(markerRect))
    screen.blit(highlighterSmall,(highlighterRect))
    if highlighterRect.collidepoint(mx,my):
        screen.blit(highlighterBWSmall,(highlighterRect))
    screen.blit(fillSmall,(fillRect))
    if fillRect.collidepoint(mx,my):
        screen.blit(fillBWSmall,(fillRect))
    screen.blit(rectSmall,(rectRect))
    if rectRect.collidepoint(mx,my):
        screen.blit(rectBWSmall,(rectRect))
    screen.blit(filledrectSmall,(filledrectRect))
    if filledrectRect.collidepoint(mx,my):
        screen.blit(filledrectBWSmall,(filledrectRect))
    screen.blit(ellipseSmall,(ellipseRect))
    if ellipseRect.collidepoint(mx,my):
        screen.blit(ellipseBWSmall,(ellipseRect))
    screen.blit(filledellipseSmall,(filledellipseRect))
    if filledellipseRect.collidepoint(mx,my):
        screen.blit(filledellipseBWSmall,(filledellipseRect))
    screen.blit(lineSmall,(lineRect))
    if lineRect.collidepoint(mx,my):
        screen.blit(lineBWSmall,(lineRect))
    screen.blit(clearbuttonS,(clearRect))
    if clearRect.collidepoint(mx,my):
        screen.blit(clearbuttonDS,(clearRect))
    screen.blit(spraySmall,(sprayRect))
    if sprayRect.collidepoint(mx,my):
        screen.blit(sprayBWSmall,(sprayRect))
    screen.blit(freeformSmall,(freeformRect))
    if freeformRect.collidepoint(mx,my):
        screen.blit(freeformSmallBW,(freeformRect))
    screen.blit(dropperSmall,(dropperRect))
    if dropperRect.collidepoint(mx,my):
        screen.blit(dropperBWSmall,(dropperRect))
    screen.blit(saveSmall,(saveRect))
    if saveRect.collidepoint(mx,my):
        screen.blit(saveSmallBW,(saveRect))
    screen.blit(openSmall,(openRect))
    if openRect.collidepoint(mx,my):
        screen.blit(openSmallBW,(openRect))
    ################-Undo Redo Pics-#################
    screen.blit(undo, (undoRect))
    screen.blit(redo, (redoRect))
    ##################-Info Box-##################### 
    draw.rect(screen,WHITE,(infoRect),0)
    draw.rect(screen,BLACK,(infoborderRect),3)
    ###########-Bliting Text into Text Box-###########
    #blits the toolbox over the text, then blits text
    if tool=="pencil":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(penciltitle,(845,635))
        screen.blit(penciltext,(845,660))
        screen.blit(colourselect,(845,680))
    if tool=="marker":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(markertitle,(845,635))
        screen.blit(markertext,(845,660))
        screen.blit(colourselect,(845,680))
    if tool=="brush":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(brushtitle,(845,635))
        screen.blit(brushtext,(845,660))
        screen.blit(colourselect,(845,680))
    if tool=="eraser":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(erasertitle,(845,635))
        screen.blit(erasertext,(845,660))
    if tool=="highlighter":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(highlightertitle,(845,635))
        screen.blit(highlightertext,(845,660))
    if tool=="fill":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(filltitle,(845,635))
        screen.blit(filltext,(845,660))
        screen.blit(colourselect,(845,680))
    if tool=="ellipse":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(ellipsetitle,(845,635))
        screen.blit(ellipsetext,(845,660))
        screen.blit(colourselect,(845,680))
    if tool=="filledellipse":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(filledellipsetitle,(845,635))
        screen.blit(filledellipsetext,(845,660))
        screen.blit(colourselect,(845,680))
    if tool=="rect":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(recttitle,(845,635))
        screen.blit(recttext,(845,660))
        screen.blit(colourselect,(845,680))
    if tool=="filledrect":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(filledrecttitle,(845,635))
        screen.blit(filledrecttext,(845,660))
        screen.blit(colourselect,(845,680))
    if tool=="line":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(linetitle,(845,635))
        screen.blit(linetext,(845,660))
        screen.blit(colourselect,(845,680))
    if tool=="spray":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(spraytitle,(845,635))
        screen.blit(spraytext,(845,660))
        screen.blit(colourselect,(845,680))
    if tool=="freeform":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(freeformtitle,(845,635))
        screen.blit(freeformtext,(845,660))
        screen.blit(freeformtext2,(845,675))
        screen.blit(freeformtext3,(845,690))
        screen.blit(colourselect,(845,705))
    if tool=="dropper":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(droppertitle,(845,635))
        screen.blit(droppertext,(845,660))
        screen.blit(droppertext2,(845,675))
    if tool=="sticker1":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(stamp1title,(845,635))
        screen.blit(stamp1text,(845,660))
    if tool=="sticker2":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(stamp2title,(845,635))
        screen.blit(stamp2text,(845,660))
    if tool=="sticker3":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(stamp3title,(845,635))
        screen.blit(stamp3text,(845,660))
    if tool=="sticker4":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(stamp4title,(845,635))
        screen.blit(stamp4text,(845,660))
    if tool=="sticker5":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(stamp5title,(845,635))
        screen.blit(stamp5text,(845,660))
    if tool=="sticker6":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(stamp6title,(845,635))
        screen.blit(stamp6text,(845,660))
    if tool=="sticker7":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(stamp7title,(845,635))
        screen.blit(stamp7text,(845,660))
    if tool=="sticker8":
        draw.rect(screen,WHITE,(infoRect),0)
        draw.rect(screen,BLACK,(infoborderRect),3)
        screen.blit(stamp8title,(845,635))
        screen.blit(stamp8text,(845,660))
    ###########-Drawing Tool Rectangles- ############      
    draw.rect(screen,GOLD,pencilRect,2)
    draw.rect(screen,GOLD,eraserRect,2)
    draw.rect(screen,GOLD,markerRect,2)
    draw.rect(screen,GOLD,brushRect,2)
    draw.rect(screen,GOLD,highlighterRect,2)
    draw.rect(screen,GOLD,fillRect,2)
    draw.rect(screen,GOLD,saveRect,2)
    draw.rect(screen,GOLD,openRect,2)
    draw.rect(screen,GOLD,sprayRect,2)
    draw.rect(screen,GOLD,rectRect,2)
    draw.rect(screen,GOLD,lineRect,2)
    draw.rect(screen,GOLD,filledrectRect,2)
    draw.rect(screen,GOLD,ellipseRect,2)
    draw.rect(screen,GOLD,filledellipseRect,2)
    draw.rect(screen,GOLD,freeformRect,2)
    draw.rect(screen,GOLD,dropperRect,2)
    ############-Drawing Sticker Rects-###############
    draw.rect(screen,GOLD,stick1Rect,2)
    draw.rect(screen,GOLD,stick2Rect,2)
    draw.rect(screen,GOLD,stick3Rect,2)
    draw.rect(screen,GOLD,stick4Rect,2)
    draw.rect(screen,GOLD,stick5Rect,2)
    draw.rect(screen,GOLD,stick6Rect,2)
    draw.rect(screen,GOLD,stick7Rect,2)
    draw.rect(screen,GOLD,stick8Rect,2) 
    #############-Bliting Stamps in Rects-############
    #if they hover over the rectangle, the icon become Black and White
    screen.blit(stick1, (stick1Rect))
    if stick1Rect.collidepoint(mx,my):
        screen.blit(stick1BW,(stick1Rect))
    screen.blit(stick2, (stick2Rect))
    if stick2Rect.collidepoint(mx,my):
        screen.blit(stick2BW,(stick2Rect))
    screen.blit(stick3,(stick3Rect))
    if stick3Rect.collidepoint(mx,my):
        screen.blit(stick3BW,(stick3Rect)) 
    screen.blit(stick4,(stick4Rect))
    if stick4Rect.collidepoint(mx,my):
        screen.blit(stick4BW,(stick4Rect))
    screen.blit(stick5,(stick5Rect))
    if stick5Rect.collidepoint(mx,my):
        screen.blit(stick5BW,(stick5Rect))
    screen.blit(stick6,(stick6Rect))
    if stick6Rect.collidepoint(mx,my):
        screen.blit(stick6BW,(stick6Rect))
    screen.blit(stick7,(stick7Rect))
    if stick7Rect.collidepoint(mx,my):
        screen.blit(stick7BW,(stick7Rect))
    screen.blit(stick8,(stick8Rect))
    if stick8Rect.collidepoint(mx,my):
        screen.blit(stick8BW,(stick8Rect))
    ###############-Selecting Colour-################
    if paletteRect.collidepoint(mx,my) and mb[0]==1:
        col=screen.get_at((mx,my))
    ###############-Selecting Tool-##################
    if pencilRect.collidepoint(mx,my) and mb[0]==1:
        tool="pencil"
        draw.rect(screen,RED,pencilRect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif eraserRect.collidepoint(mx,my) and mb[0]==1:
        tool="eraser"
        draw.rect(screen,RED,eraserRect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif markerRect.collidepoint(mx,my) and mb[0]==1:
        tool="marker"
        draw.rect(screen,RED,markerRect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif brushRect.collidepoint(mx,my) and mb[0]==1:
        tool="brush"
        draw.rect(screen,RED,brushRect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif highlighterRect.collidepoint(mx,my) and mb[0]==1:
        tool="highlighter"
        draw.rect(screen,RED,highlighterRect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif fillRect.collidepoint(mx,my) and mb[0]==1:
        tool="fill"
        draw.rect(screen,RED,fillRect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif lineRect.collidepoint(mx,my) and mb[0]==1:
        tool="line"
        draw.rect(screen,RED,lineRect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif rectRect.collidepoint(mx,my) and mb[0]==1:
        tool="rect"
        draw.rect(screen,RED,rectRect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif filledrectRect.collidepoint(mx,my) and mb[0]==1:
        tool="filledrect"
        draw.rect(screen,RED,filledrectRect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif ellipseRect.collidepoint(mx,my) and mb[0]==1:
        tool="ellipse"
        draw.rect(screen,RED,ellipseRect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif filledellipseRect.collidepoint(mx,my) and mb[0]==1:
        tool="filledellipse"
        draw.rect(screen,RED,filledellipseRect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif sprayRect.collidepoint(mx,my) and mb[0]==1:
        tool="spray"
        draw.rect(screen,RED,sprayRect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif freeformRect.collidepoint(mx,my) and mb[0]==1:
        tool="freeform"
        draw.rect(screen,RED,freeformRect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif dropperRect.collidepoint(mx,my) and mb[0]==1:
        tool="dropper"
        draw.rect(screen,RED,dropperRect,2) #drawing a red rectangle around tool box to show user they selected the tool
    ##################-Clear Screen-#################
    if clearRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,WHITE,canvasRect)
    ###############-Selecting Stickers-##############
    elif stick1Rect.collidepoint(mx,my) and mb[0]==1:
        tool="sticker1"
        draw.rect(screen,RED,stick1Rect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif stick2Rect.collidepoint(mx,my) and mb[0]==1:
        tool="sticker2"
        draw.rect(screen,RED,stick2Rect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif stick3Rect.collidepoint(mx,my) and mb[0]==1:
        tool="sticker3"
        draw.rect(screen,RED,stick3Rect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif stick4Rect.collidepoint(mx,my) and mb[0]==1:
        tool="sticker4"
        draw.rect(screen,RED,stick4Rect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif stick5Rect.collidepoint(mx,my) and mb[0]==1:
        tool="sticker5"
        draw.rect(screen,RED,stick5Rect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif stick6Rect.collidepoint(mx,my) and mb[0]==1:
        tool="sticker6"
        draw.rect(screen,RED,stick6Rect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif stick7Rect.collidepoint(mx,my) and mb[0]==1:
        tool="sticker7"
        draw.rect(screen,RED,stick7Rect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif stick8Rect.collidepoint(mx,my) and mb[0]==1:
        tool="sticker8"
        draw.rect(screen,RED,stick8Rect,2) #drawing a red rectangle around tool box to show user they selected the tool
    elif paletteRect.collidepoint(mx,my) and mb[0]==1:
        screen.set_clip(paletteRect) #only the palette can be adjusted
        screen.blit(paletteSmall,(10,515)) #bliting the palette again
        draw.rect(screen,(214, 200, 10),(10,515,250,250),3) #drawing palette border
        draw.circle(screen,WHITE,(mx,my),10,2) #drawing a white circle around mouse to show colour selected         
    #############-Utilizing the Tool-################
    if canvasRect.collidepoint(mx,my) and mb[0]==1:
        screen.set_clip(canvasRect) #only allows canvas to be modified
        if tool=="pencil":
            draw.line(screen,col,(cmx,cmy),(mx,my),2)
        elif tool=="eraser":
            dx=mx-cmx #using similar triangles, same thing as in lesson
            dy=my-cmy
            dist=int(sqrt(dx**2+dy**2))
            for i in range (1,dist+1):
                dotX=int(cmx+i*dx/dist)
                dotY=int(cmy+i*dy/dist)
                draw.circle(screen, WHITE,(dotX,dotY),10)
        elif tool=="marker":
            dx=mx-cmx #using similar triangles, same thing as in lesson
            dy=my-cmy
            dist=int(sqrt(dx**2+dy**2))
            for i in range (1,dist+1):
                dotX=int(cmx+i*dx/dist)
                dotY=int(cmy+i*dy/dist)
                draw.circle(screen, col,(dotX,dotY),10)
        elif tool=="rect":
            screen.blit(back,(0,0)) #so we can only draw one coordinate
            nmx=startx-mx #getting the second coordinates
            nmy=starty-my #getting the second coordinates
            if nmx<startx: #if point is to the left of starting point, multiply by -1 because there is not a negative coordinate on program
                nmx*=-1
            if nmy<starty: #if point is above the starting point, multiply by -1 because there is not a negative coordinate on program
                nmy*=-1
            draw.rect(screen,col,[startx,starty,nmx,nmy],1)
        elif tool=="filledrect":
            screen.blit(back,(0,0))#so we can only draw one rectangle on screen
            nmx=startx-mx #getting the second coordinates
            nmy=starty-my #getting the second coordinates
            if nmx<startx:
                nmx*=-1 #if point is to the left of starting point, multiply by -1 because there is not a negative coordinate on program
            if nmy<starty: #if point is above the starting point, multiply by -1 because there is not a negative coordinate on program
                nmy*=-1
            draw.rect(screen,col,[startx,starty,nmx,nmy],0)
        elif tool=="ellipse":
            screen.blit(back,(0,0)) #so we can only draw on ellipse on screen
            ellipse=Rect(cmx,cmy,mx-cmx,my-cmy) 
            ellipse.normalize() #makes it an ellipse: found it on stackoverflow
            try:
                draw.ellipse(screen,col,(ellipse),2)
            except:
                pass
        elif tool=="filledellipse":
            screen.blit(back,(0,0)) #draws only one ellispe
            ellipse=Rect(cmx,cmy,mx-cmx,my-cmy)
            ellipse.normalize() #makes it an ellipse: found it on stackoverflow
            try:
                draw.ellipse(screen,col,(ellipse),0)
            except:
                pass
        elif tool=="highlighter":
            if omx!=mx or omy!=my: #if we move the mouse
                if mb[0]==1:
                    screen.blit(brushHead,(mx-10,my-10))
        elif tool=="brush":
            dx=mx-cmx #using similar triangles, same thing as in lesson
            dy=my-cmy
            dist=int(sqrt(dx**2+dy**2))
            for i in range (1,dist+1):
                dotX=int(cmx+i*dx/dist)
                dotY=int(cmy+i*dy/dist)
                draw.circle(screen,col,(dotX,dotY),2)
        elif tool=="line":
            screen.blit(back,(0,0)) #So you can only draw one thing
            draw.line(screen,col,(omx,omy),(mx,my),2)
        elif tool=="fill":
            mainColour=screen.get_at((mx,my))#colour of pixel you clicked
            pointList=[(mx,my)] #points
            usedPointSet=set()
            while len(pointList)>0:
                pixel=pointList.pop()
                if mainColour==screen.get_at(pixel) and pixel not in usedPointSet:
                    screen.set_at(pixel,col)
                    pointList.append((pixel[0]+1,pixel[1])) #adding points around the point clicked
                    pointList.append((pixel[0]-1,pixel[1])) #adding points around the point clicked
                    pointList.append((pixel[0],pixel[1]+1)) #adding points around the point clicked
                    pointList.append((pixel[0],pixel[1]-1)) #adding points around the point clicked
                usedPointSet.add(pixel)
        elif tool=="spray":
            x=20//2 #variable in for loop
            for i in range(x): #Makes it faster
                sx=randint(-r,r) #random x in square
                sy=randint(-r,r) #random y in square
                if hypot(sx,sy)<=r: #if it falls on eq'n of circle
                    screen.set_at((sx+mx,sy+my),col) #setting
        elif tool=="freeform":
            pointList=[(mx, my)]
            while True:
                for evt in event.get(): 
                    if evt.type==MOUSEBUTTONDOWN: #if clicked
                        point=evt.pos #point clicked
                        pointList.append(point)#list of points that are clicked
                        draw.lines(screen,col,False,pointList,1) #drawing lines in between points
                        display.update()
                if evt.type==KEYDOWN:
                    if evt.key==K_RETURN:
                        try:
                            draw.lines(screen,col,True,pointList,1) #if pressed enter, draw line from last point to first point
                            break
                        except ValueError:
                            break
        elif tool=="dropper":
            if canvasRect.collidepoint(mx,my): #allows user to get a colour from the canvas
                col=screen.get_at((mx,my))
                screen.blit(paletteSmall,(10,515)) #makes the white circle disappear
                draw.rect(screen,(214, 200, 10),(10,515,250,250),3)
                draw.rect(screen,col,colRect,0)
                draw.rect(screen,GOLD,colBorder,3)
    ######################-Stamps-###########################
        if click: #so you can't drag the stamp, it'll only show up once
            if tool=="sticker1":
                screen.blit(sticker1,(mx-90,my-60))
            elif tool=="sticker2":
                screen.blit(sticker2,(mx-50,my-130))
            elif tool=="sticker3":
                screen.blit(sticker3,(mx-130,my-170))
            elif tool=="sticker4":
                screen.blit(sticker4,(mx-130,my-110))
            elif tool=="sticker5":
                screen.blit(sticker5,(mx-100,my-130))
            elif tool=="sticker6":
                screen.blit(sticker6,(mx-80,my-90))
            elif tool=="sticker7":
                screen.blit(sticker7,(mx-150,my-240))
            elif tool=="sticker8":
                screen.blit(sticker8,(mx-100,my-170))
    ####################-Music-#####################
    if playpauseRect.collidepoint(mx,my) and mb[0]==1:
        if click:
            if paused: #if it is already paused
                pygame.mixer.music.unpause()#unpauses music
                paused=False
                draw.circle(screen,WHITE,(135,455),40)
                screen.blit(play,(playpauseRect)) #bliting play icon
            else: #if the music is playing
                pygame.mixer.music.pause()#pauses music
                paused=True
                draw.circle(screen,WHITE,(135,455),40)
                screen.blit(pause,(playpauseRect)) #bliting pause icon
    if forwardRect.collidepoint(mx,my) and mb[0]==1:
        if click: #so you can't hold it down
            index+=1 #next song
            if index==len(music): #if it is the last song, restart at beginning
                index==0
            cSong=music[index] #new song
            pygame.mixer.music.load(cSong)
            pygame.mixer.music.play()
    if backRect.collidepoint(mx,my) and mb[0]==1:
        if click: #so you can't hold it down
            index-=1 #the song before
            if index==0: #if it's the first song, goes to the last song
                index==len(music)
            cSong=music[index] #playing new music
            pygame.mixer.music.load(cSong)
            pygame.mixer.music.play()
        
    #################-Open and Save-#################
    if saveRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,RED,saveRect,1)
        try:
            fname=filedialog.asksaveasfilename(defaultextension=".png")
            #asks the user to input file name they would like to save as

            image.save(screen.subsurface(canvasRect), fname)
        except:
            pass #prevent crashing


    #loading (opening) a picture
    if openRect.collidepoint(mx,my) and mb[0]==1:
        draw.rect(screen,RED,openRect,1)
        try:
            fname=filedialog.askopenfilename(filetypes=[("Images","*.png;*.bmp;*.jpg;*.jpeg")])
            #asks the user to open a file with the following extensions
            print(fname)

            #instead of just printing "fname" you need to actually
            #load the picture and blit the picture 
        except:
            pass
           
    
        

        
                
    screen.set_clip(None)
    #loading (opening) a picture
    


    cmx,cmy=mx,my
    display.flip()
    
quit() #closing the pygame window
