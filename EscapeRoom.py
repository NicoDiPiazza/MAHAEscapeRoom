import pygame
import keyboard


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
    

class Clue():
    def __init__(self, password:str, info:str, locked:bool):
        self.password = password
        self.info = info
        self.locked = locked
    




stop = False
dt = 10
screenWidth = 1600
screenHeight = 850
screen = pygame.display.set_mode((screenWidth, screenHeight))
main_font = pygame.font.SysFont('arial', 25)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
            'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
onHomeScreen = True

clue1 = Clue('password123', 'this is the first clue', True)
clue2 = Clue('guessthis', 'this is the second clue.', True)

clues = [clue1, clue2]

currentEntry = ""

underscoreShow = 0
maxUnderscore = 8

while ( stop != True):
    underscoreShow = underscoreShow + 1
    if underscoreShow >= maxUnderscore:
        underscoreShow = 0
  
    if keyboard.is_pressed('esc'):
        stop = True

    if onHomeScreen:
        currentEntry = currentEntry + newLetter(alphabet)
        if keyboard.is_pressed('backspace') and len(currentEntry) > 0:
            currentEntryList = list(currentEntry)
            currentEntryList.pop()
            currentEntry = "".join(currentEntryList)
        if keyboard.is_pressed('enter'):
            for i in clues:
                if currentEntry == i.password:
                    onHomeScreen = False
                    currentClue = i
                    i.locked = False
            currentEntry = ""
    else:
        if keyboard.is_pressed('space'):
            onHomeScreen = True
        


    ## still to be done: make the information release system based on inputting a valid password, 
    ##      make the tracker for locked vs unlocked clues
    
    screen.fill([0, 0, 0])

    if onHomeScreen:
        if underscoreShow < maxUnderscore/2:
            screen.blit(main_font.render("Enter any password: " + currentEntry, True, [255, 255, 255]), 
                    [screenWidth * 0.05, screenHeight * 0.05])
            
        else:
            screen.blit(main_font.render("Enter any password: " + currentEntry + '_', True, [255, 255, 255]), 
                    [screenWidth * 0.05, screenHeight * 0.05])
            
        clueNumber = 0
        for i in clues:
            clueNumber = clueNumber + 1
            if i.locked:
                screen.blit(main_font.render('Locked', True, [255, 0, 0]), 
                        [screenWidth * 0.85, screenHeight * clueNumber *0.5])
            else:
                screen.blit(main_font.render('Unlocked', True, [0, 255, 0]), 
                        [screenWidth * 0.85, screenHeight * clueNumber *0.5])

    else:
        screen.blit(main_font.render(currentClue.info, True, [255, 255, 255]), [screenWidth * 0.05, screenHeight * 0.05])
        screen.blit(main_font.render('Press spacebar to return home', True, [255, 255, 255]), [screenWidth * 0.2, screenHeight * 0.9])
    #time between each frame
    clock.tick(dt)
    #print(clock.get_fps())
    #updates the frame
    pygame.display.update()
