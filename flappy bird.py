from m5stack import *
from m5ui import *
import time

#variablelen.
Status = ""
Run = True
Bird = None
Bird_Hoogte = 102
start_text_string = "Press button A"
list_pipe = []
list_pipe_coords = []

#game waardes
Val_Snelheid = 15 #Hiermee pas je de valsnelheid aan
Jump_Hoogte = 30 #Hiermee pas je de jump hoogte aan

#menu of the game
def game_menu():
    global start_text
    global Run
    Run = True
    #clear the screen + fill black
    lcd.clear(lcd.BLACK)
    #all the text in the menu
    start_text = M5TextBox(15, 100, start_text_string, lcd.FONT_Default, 0xffffff, rotate=0)
    start_text = M5TextBox(40, 120, "to start", lcd.FONT_Default, 0xffffff, rotate=0)


    game_loop()

def btnAPressed():
    global Status
    global Bird_Hoogte
    global Bird
    global Jump_Hoogte
    #if statement of game_start is begonnen, bird omhoog
    if Status == "":
        Status = "started"
        game_start()
    elif Status == "started":
        #jump bird
        Bird_Hoogte -= Jump_Hoogte
        Bird.setPosition(y=Bird_Hoogte)

def game_start():
    global Bird_Hoogte
    global Bird
    global Status
    global list_pipe_coords
    global list_pipe
    lcd.clear()
    
    #name of the background = "flappy-background-night.png" ,
    #lcd.image(0,0,"res/flappy-background-night.png")

    #name of the body = "flappy-body.png"
    Bird = M5Img(10, 102, "img/flappy-body.png", True)

    #pipe 2d array Y, coordinaten.
    list_pipe_coords = [
        [130,30],
        [130,150]
    ]
    #spauwn pipes.
    list_pipe = [
        M5Img(list_pipe_coords[0][0], list_pipe_coords[0][1], "img/flappy-body.png", True),
        M5Img(list_pipe_coords[1][0], list_pipe_coords[1][1], "img/flappy-body.png", True)
    ]
    #
    game_loop()
        
def game_loop():
    global Run
    global Bird
    global Bird_Hoogte
    global Val_Snelheid
    global list_pipe_coords
    global list_pipe

    while Run:
        time.sleep(0.1)
        #pipe = M5Img(10, list_pipe[0][1], "img/pip===0kjkjk.png", True)

        if btnA.wasPressed():
            btnAPressed()
        #bird naar beneden laten vallen
        elif Status == "started":
            #lcd.setScreenColor(lcd.GREEN)
            Bird_Hoogte += Val_Snelheid
            Bird.setPosition(y=Bird_Hoogte)

            i = 0
            for x in list_pipe_coords:
                #check collisions,kijk of het verschil tussen de posities zo klein is dat ze elkaar aanraken.
                if ((10 - x[0]) > -50 and (10 - x[0]) < 20) and (Bird_Hoogte - x[1] > -30 and Bird_Hoogte - x[1] < 30):
                    summon_death()

                #snelheid van de pipes veranderen veranderen.
                x[0] = x[0] - 6
                #var x, in de list[0] veranderd hij terug naar de waarde 130. if x = -5.
                if x[0] < -40:
                    x[0] = 130

                list_pipe[i].setPosition(x=list_pipe_coords[i][0])
                i += 1

        #stop
        if btnB.wasPressed():
            Run = False
        #hoger dan 220 px dan summon death
        if Bird_Hoogte > 220:
            summon_death()

def summon_death():
    global Run
    global Status
    global start_text_string
    global Bird_Hoogte
    global restart

    Run = False
    Status = ""
    start_text_string = "Game Over - Press button a"
    Bird_Hoogte = 100
    Bird.setPosition(y=Bird_Hoogte)
    #druk but A om te spelen
    game_menu()


#functies
game_menu()