import pygame
import keyboard
import numpy
import math


pygame.init()
pygame.font.init()
clock = pygame.time.Clock()


def newLetter(alphabet:list):
    for i in alphabet:
        if keyboard.is_pressed(i):
            if keyboard.is_pressed('shift'):
                return i.upper()
            else:
                return i
    else:
        return ''
    




stop = False
dt = 10
screenWidth = 1600
screenHeight = 850
screen = pygame.display.set_mode((screenWidth, screenHeight))
main_font = pygame.font.SysFont('arial', 25)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

currentEntry = ""

while ( stop != True):
    
  
    if keyboard.is_pressed('esc'):
        stop = True

    currentEntry = currentEntry + newLetter(alphabet)
    if keyboard.is_pressed('backspace') and len(currentEntry) > 0:
        currentEntryList = list(currentEntry)
        currentEntryList.pop()
        currentEntry = "".join(currentEntryList)
    if keyboard.is_pressed('enter'):
        currentEntry = ""
    
    screen.fill([0, 0, 0])

    screen.blit(main_font.render("Enter any password: " + currentEntry, True, [250, 250, 250]), [screenWidth * 0.05, screenHeight * 0.05])
    #time between each frame
    clock.tick(dt)
    #print(clock.get_fps())
    #updates the frame
    pygame.display.update()