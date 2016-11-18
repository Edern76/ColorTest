import tdl
from tdl import *

MENU_KEYS = {'LEFT': -1, 'RIGHT': 1}
DEBUG_KEYS = {'UP': -1, 'DOWN' : 1}

WIDTH, HEIGHT = 70, 36
MAX_FPS = 30

root = tdl.init(WIDTH, HEIGHT, 'Initializing...')
set_fps(MAX_FPS)
#choices = ['R', 'G', 'B']
index = 1
bWhite = (255, 255, 255)
rLevel, gLevel, bLevel = 255, 255, 255
loremX, loremY = 28, 8
offRight = WIDTH - (loremX + 12)
canContinue = False
loremIsEnabled = False
helpScreen = False

def getInput():
    global index
    user_input = tdl.event.key_wait()
    if user_input.keychar.upper() in MENU_KEYS:
        index += MENU_KEYS[user_input.keychar.upper()]
        if index > 3 or index == 4:
            index = 1
        if index < 1 or index == 0:
            index = 3
        update()    
    if user_input.keychar.upper() == 'ENTER':
        global canContinue
        canContinue = True
        update()
        if index == 1: #choices[index] == 'R':
            while canContinue:
                setrLevel()
        elif index == 2:#choices[index] == 'G':
            while canContinue:
                setgLevel()
        elif index == 3:#choices[index] == 'B':
            while canContinue:
                setbLevel()
    elif user_input.keychar.upper() == 'ESCAPE':
        raise SystemExit ('Escape has been pressed')
     
    elif user_input.keychar.upper() == 'F2':
        global loremIsEnabled
        loremIsEnabled = True
        while loremIsEnabled:
            loremDebug()
    
    elif user_input.keychar.upper() == 'F1':
        global helpScreen
        helpScreen = True
        while helpScreen:
            update()
            #help_input = tdl.event.key_wait()
            #if user_input.keychar.upper == 'ESCAPE' or help_input.keychar.upper == 'ESCAPE':
            for event in tdl.event.get():
                if (event.type == 'KEYDOWN' and event.key == 'ESCAPE'):
                    helpScreen = False
                    print('Escape pressed')
                    update()
                    break
            
    for event in tdl.event.get():
        if event.type == 'QUIT':
            raise SystemExit ('Window has been closed')            
def setrLevel():
    global rLevel
    global canContinue
    level_input = tdl.event.key_wait()
    if level_input.keychar.upper() in MENU_KEYS:
        rLevel += MENU_KEYS[level_input.keychar.upper()]
        if rLevel > 255:
            rLevel = 0
        if rLevel < 0:
            rLevel = 255
        update()        
    elif level_input.keychar.upper() == 'ESCAPE':
        canContinue = False
def setgLevel():
    global gLevel
    global canContinue
    level_input = tdl.event.key_wait()
    if level_input.keychar.upper() in MENU_KEYS:
        gLevel += MENU_KEYS[level_input.keychar.upper()]
        if gLevel > 255:
            gLevel = 0
        if gLevel < 0:
            gLevel = 255
        update()        
    elif level_input.keychar.upper() == 'ESCAPE':
        canContinue = False    
def setbLevel():
    global bLevel
    global canContinue
    level_input = tdl.event.key_wait()
    if level_input.keychar.upper() in MENU_KEYS:
        bLevel += MENU_KEYS[level_input.keychar.upper()]
        if bLevel > 255:
            bLevel = 0
        if bLevel < 0:
            bLevel = 255
        update()        
    elif level_input.keychar.upper() == 'ESCAPE':
        canContinue = False
def loremDebug():
    global canContinue
    global loremIsEnabled
    global loremX, loremY
    global offRight
    global WIDTH
    canContinue = True
    update()
    lorem_input = tdl.event.key_wait()
    if lorem_input.keychar.upper() in MENU_KEYS:
        loremX += MENU_KEYS[lorem_input.keychar.upper()]
        offRight = WIDTH - (loremX + 11)
        update()
    elif lorem_input.keychar.upper() in DEBUG_KEYS:
        loremY += DEBUG_KEYS[lorem_input.keychar.upper()]
        update()    
    elif lorem_input.keychar.upper() == 'ESCAPE':
        canContinue = False
        loremIsEnabled = False
        update()          
def update():
    root.clear()
    curFPS = get_fps()
    set_title('ColorTest | FPS : {} | By Gawein LE GOFF'.format(curFPS))
    if not(helpScreen):
        root.draw_str(loremX, loremY, 'Lorem Ipsum.', fg=(rLevel, gLevel, bLevel))
        if index == 1:
            root.draw_str(12, 18, ' R ', fg=(255,0,0), bg=bWhite)
            root.draw_str(32, 18, ' G ', fg=(0,255,0) , bg=None)
            root.draw_str(52, 18, ' B ', fg=(0,0,255), bg=None)
        elif index == 2:
            root.draw_str(12, 18, ' R ', fg=(255,0,0), bg=None)
            root.draw_str(32, 18, ' G ', fg=(0,255,0) , bg=bWhite)
            root.draw_str(52, 18, ' B ', fg=(0,0,255), bg=None)
        elif index == 3:
            root.draw_str(12, 18, ' R ', fg=(255,0,0), bg=None)
            root.draw_str(32, 18, ' G ', fg=(0,255,0) , bg=None)
            root.draw_str(52, 18, ' B ', fg=(0,0,255), bg=bWhite)
        else:
            raise SystemExit('Index out of bounds ({})'.format(index))
        root.draw_str(12, 19, str(rLevel))
        root.draw_str(32, 19, str(gLevel))
        root.draw_str(52, 19, str(bLevel))
        if canContinue:
            root.draw_str(0, 35, 'Press Escape to return to selection mode')
        else:
            root.draw_str(0, 1, 'F1 : ', fg=(0,255,0))
            root.draw_str(5, 1,'Help')
            root.draw_str(11, 1,'Arrows : ', fg=(0,255,0))
            root.draw_str(20, 1,'Select')    
        if loremIsEnabled:
            root.draw_str(0, 32, 'DEBUG', fg = (255,0,0))
            root.draw_str(0, 33, 'X = {}  Y= {}  Right Offset = {}'.format(loremX, loremY, offRight), fg = (255,0,0))
    else:
        root.draw_str(0, 1, 'Created by Gawein Le Goff using TDL 1.5.3')
        root.draw_str(0, 3, 'This simple program allows you to try different RGB combinations')
        root.draw_str(0, 4, "In order to use it, select using the arrow keys and the Enter key the")
        root.draw_str(0, 5, "color you'd like to change, then use the arrow keys to change its")
        root.draw_str(0, 6, 'value. (left arrow decreases by one, right arrow increases by one).' )
        root.draw_str(0, 8, 'The sentence "Lorem Ipsum." will change color in real time according')
        root.draw_str(0, 9, 'to the RGB values.')
        root.draw_str(0, 11, 'This software is made available according to the GNU General Public')
        root.draw_str(0, 12, 'V3, available at http://www.gnu.org/licenses/gpl.html.')
        root.draw_str(0, 35, 'Press ')
        root.draw_str(6, 35, 'Escape', fg = (0,255,0)) 
        root.draw_str(13, 35, 'to return to main screen.')     
    tdl.flush()                        
while True:
    update()
    getInput()

    
