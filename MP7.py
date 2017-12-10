import random
from Tkinter import *
import tkMessageBox

def keyPressed(event):
    if(canvas.data.gameOver == True or canvas.data.gameWin == True):
        if event.char == "r":
            canvas.data.gameOver = False
            canvas.data.gameWin = False
            canvas.data.life = 0
            canvas.data.eachIndex = [False,False,False,False,False,False,False,False]
            e1.set("")
            e2.set("")
            canvas.data.worngWord = ["","","","","","",""]
            canvas.data.worngWordIndex = 0

            init()

def timerFired():
    redrawAll()

    delay = 500
    canvas.after(delay, timerFired)

def redrawAll():
    canvas.delete(ALL)
    drawBackground()
    drawStickman()

def guessLetter():
    if(canvas.data.gameOver == False and canvas.data.gameWin == False):
        flag = False
        for i in xrange(len(canvas.data.newWord)):
            if(canvas.data.newWord[i] == Entry.get(letterInput).upper()):
                flag = True
                canvas.data.eachIndex[i] = True

        if(flag == False):
            canvas.data.life += 1
            canvas.data.worngWord[canvas.data.worngWordIndex] = Entry.get(letterInput).upper()
            canvas.data.worngWordIndex += 1
            

        flag2 = True
        for i in xrange(len(canvas.data.eachIndex)):
            if(canvas.data.eachIndex[i] == False):
                flag2 = False

        if(flag2 == True):
            canvas.data.gameWin = True

        if(canvas.data.life >= 7):
            canvas.data.gameOver = True

    e1.set("")

def guessWord():
    if(canvas.data.gameOver == False and canvas.data.gameWin == False):
        if(Entry.get(wordInput).upper() == canvas.data.newWord):
            for i in xrange(len(canvas.data.eachIndex)):
                canvas.data.eachIndex[i] = True
                canvas.data.gameWin = True
        else:
            canvas.data.life += 1

        if(canvas.data.life >= 7):
            canvas.data.gameOver = True

    e2.set("")

def getNewWord():
    canvas.data.newWord = canvas.data.Words[random.randint(0, 269)]
    

def drawStickman():
    if(canvas.data.life >= 1):
        canvas.create_line(250, 123,\
                            250, 200,\
                            fill = canvas.data.Colors[random.randint(0, 14)], width = 5)
    if(canvas.data.life >= 2):
        canvas.create_oval(210, 200,\
                            290, 280,\
                            outline = canvas.data.Colors[random.randint(0, 14)], width = 5)
    if(canvas.data.life >= 3):
        canvas.create_line(250, 283,\
                            250, 440,\
                            fill = canvas.data.Colors[random.randint(0, 14)], width = 10)
    if(canvas.data.life >= 4):
        canvas.create_line(250, 320,\
                            180, 400,\
                            fill = canvas.data.Colors[random.randint(0, 14)], width = 8)
    if(canvas.data.life >= 5):
        canvas.create_line(250, 320,\
                            320, 400,\
                            fill = canvas.data.Colors[random.randint(0, 14)], width = 8)
    if(canvas.data.life >= 6):
        canvas.create_line(250, 440,\
                            180, 520,\
                            fill = canvas.data.Colors[random.randint(0, 14)], width = 8)
    if(canvas.data.life >= 7):
        canvas.create_line(250, 440,\
                            320, 520,\
                            fill = canvas.data.Colors[random.randint(0, 14)], width = 8)

def drawBackground():
    canvas.create_rectangle(0, 0,\
                        canvas.data.width, canvas.data.height,\
                        fill = "#E2FFFF")
    canvas.create_line(100, 120,\
                        400, 120,\
                        fill = canvas.data.Colors[random.randint(0, 14)], width = 5)
    canvas.create_line(100, 118,\
                        100, 360,\
                        fill = canvas.data.Colors[random.randint(0, 14)], width = 5)
    canvas.create_line(100, 360,\
                        100, 600,\
                        fill = canvas.data.Colors[random.randint(0, 14)], width = 5)
    canvas.create_line(98, 600,\
                        400, 600,\
                        fill = canvas.data.Colors[random.randint(0, 14)], width = 5)
    canvas.create_line(525, 200,\
                        575, 200,\
                        fill = "black", width = 3)
    canvas.create_line(600, 200,\
                        650, 200,\
                        fill = "black", width = 3)
    canvas.create_line(675, 200,\
                        725, 200,\
                        fill = "black", width = 3)
    canvas.create_line(750, 200,\
                        800, 200,\
                        fill = "black", width = 3)
    canvas.create_line(825, 200,\
                        875, 200,\
                        fill = "black", width = 3)
    canvas.create_line(900, 200,\
                        950, 200,\
                        fill = "black", width = 3)
    canvas.create_line(975, 200,\
                        1025, 200,\
                        fill = "black", width = 3)
    canvas.create_line(1050, 200,\
                        1100, 200,\
                        fill = "black", width = 3)
    canvas.create_text(600, 350,\
                        text = "Input a letter:",\
                        font = "Helvetica 16",anchor = "center")
    canvas.create_text(600, 450,\
                        text = "Input a word:",\
                        font = "Helvetica 16",anchor = "center")
    if(canvas.data.eachIndex[0] == True):
        canvas.create_text(550, 180,\
                        text = canvas.data.newWord[0],\
                        font = "Helvetica 16 bold",anchor = "center")
    if(canvas.data.eachIndex[1] == True):
        canvas.create_text(625, 180,\
                        text = canvas.data.newWord[1],\
                        font = "Helvetica 16 bold",anchor = "center")
    if(canvas.data.eachIndex[2] == True):
        canvas.create_text(700, 180,\
                        text = canvas.data.newWord[2],\
                        font = "Helvetica 16 bold",anchor = "center")
    if(canvas.data.eachIndex[3] == True):
        canvas.create_text(775, 180,\
                        text = canvas.data.newWord[3],\
                        font = "Helvetica 16 bold",anchor = "center")
    if(canvas.data.eachIndex[4] == True):
        canvas.create_text(850, 180,\
                        text = canvas.data.newWord[4],\
                        font = "Helvetica 16 bold",anchor = "center")
    if(canvas.data.eachIndex[5] == True):
        canvas.create_text(925, 180,\
                        text = canvas.data.newWord[5],\
                        font = "Helvetica 16 bold",anchor = "center")
    if(canvas.data.eachIndex[6] == True):
        canvas.create_text(1000, 180,\
                        text = canvas.data.newWord[6],\
                        font = "Helvetica 16 bold",anchor = "center")
    if(canvas.data.eachIndex[7] == True):
        canvas.create_text(1075, 180,\
                        text = canvas.data.newWord[7],\
                        font = "Helvetica 16 bold",anchor = "center")
    if(canvas.data.gameOver == True):
        canvas.create_text(800, 550,\
                        text = "YOU LOSE!!!",\
                        font = "Helvetica 24 bold",anchor = "center")
        canvas.create_text(800, 600,\
                        text = "Press 'R' to start a new round",\
                        font = "Helvetica 20",anchor = "center")
        canvas.create_text(800, 650,\
                        text = "The correst answer is: " + canvas.data.newWord,\
                        font = "Helvetica 16",anchor = "center")
    if(canvas.data.gameWin == True):
        canvas.create_text(800, 550,\
                        text = "YOU WIN!!!",\
                        fill = canvas.data.Colors[random.randint(0, 14)],\
                        font = "Helvetica 24 bold",anchor = "center")
        canvas.create_text(800, 600,\
                        text = "Press 'R' to start a new round",\
                        font = "Helvetica 20",anchor = "center")
    for i in xrange(len(canvas.data.worngWord)):
        if(canvas.data.worngWord[i] != ""):
            canvas.create_text(650 + i * 50, 100,\
                        text = canvas.data.worngWord[i],\
                        font = "Helvetica 14 bold",anchor = "center")
        else:
            break;
    

def init():
    canvas.data.width = 1200
    canvas.data.height = 720
    canvas.data.Colors = ["red","yellow","blue","lime","wheat",
                          "magenta","pink","grey","tomato",
                          "cyan","green","orange",
                          "black","purple","brown"]
    canvas.data.Words = ["ABSOLUTE",
                            "ABSTRACT",
                            "ACADEMIC",
                            "ACCIDENT",
                            "ACCURACY",
                            "ACCURATE",
                            "ACTIVITY",
                            "ACTUALLY",
                            "ADDITION",
                            "ADEQUATE",
                            "ADJACENT",
                            "ADVOCATE",
                            "ADVISORY",
                            "ALLIANCE",
                            "ALTHOUGH",
                            "ANALYSIS",
                            "ANNOUNCE",
                            "APPARENT",
                            "APPROVAL",
                            "ARGUMENT",
                            "ARTISTIC",
                            "ASSEMBLY",
                            "ATHLETIC",
                            "ATTITUDE",
                            "ATTORNEY",
                            "AUDIENCE",
                            "AUTONOMY",
                            "AVIATION",
                            "BACHELOR",
                            "BECTERIA",
                            "BOUNDARY",
                            "BUSINESS",
                            "CALENDER",
                            "CAMPAIGN",
                            "CAPACITY",
                            "CASUALTY",
                            "CAUTIOUS",
                            "CELLULAR",
                            "CEREMONY",
                            "CHAMPION",
                            "CHEMICAL",
                            "CIRCULAR",
                            "CLINICAL",
                            "COLLAPSE",
                            "COMPLAIN",
                            "COMPLETE",
                            "COMPOUND",
                            "COMPUTER",
                            "CONCLUDE",
                            "CONCRETE",
                            "CONFLICT",
                            "CONGRESS",
                            "CONSIDER",
                            "CONSTANT",
                            "CONSUMER",
                            "CONTINUE",
                            "CONTRACT",
                            "CONTRAST",
                            "CONVINCE",
                            "CRIMINAL",
                            "CRITICAL",
                            "CUSTOMER",
                            "DAUGHTER",
                            "DECISION",
                            "DECREASE",
                            "DEFINITE",
                            "DELIVERY",
                            "DESCRIBE",
                            "DESIGNER",
                            "DIALOGUE",
                            "DIRECTOR",
                            "DISASTER",
                            "DISTANCE",
                            "DISTINCT",
                            "DISTRICT",
                            "DIVISION",
                            "DOCUMENT",
                            "DOMESTIC",
                            "DOMINANT",
                            "DRAMATIC",
                            "DURATION",
                            "DYNAMICS",
                            "ECONOMIC",
                            "ELECTION",
                            "ELECTRIC",
                            "ELIGIBLE",
                            "EMPHASIS",
                            "EMPLOYEE",
                            "ENGINEER",
                            "ENORMOUS",
                            "ENTRANCE",
                            "ENVELOPE",
                            "EQUALITY",
                            "EQUATION",
                            "ESTIMATE",
                            "EVALUATE",
                            "EVIDENCE",
                            "EXCHANGE",
                            "EXERCISE",
                            "EXPLICIT",
                            "EXPOSURE",
                            "EXTERNAL",
                            "FACILITY",
                            "FAMILIAR",
                            "FESTIVAL",
                            "FLEXIBLE",
                            "FORECAST",
                            "FRACTION",
                            "FREQUENT",
                            "FUNCTION",
                            "GENERATE",
                            "GENEROUS",
                            "GOVERNOR",
                            "GRADUATE",
                            "GUARDIAN",
                            "GUIDANCE",
                            "HERITAGE",
                            "HISTORIC",
                            "HOSPITAL",
                            "HUMANITY",
                            "IDENTIFY",
                            "IDENTITY",
                            "IMPERIAL",
                            "INCIDENT",
                            "INCREASE",
                            "INDICATE",
                            "INDUSTRY",
                            "INHERENT",
                            "INITIATE",
                            "INNOCANT",
                            "INSTANCE",
                            "INTEGRAL",
                            "INTIMATE",
                            "INVOLVED",
                            "JUDGMENT",
                            "JUDICIAL",
                            "JUNCTION",
                            "LANGUAGE",
                            "LAUGHTER",
                            "LEVERAGE",
                            "LITERARY",
                            "LOCATION",
                            "MAGAZINE",
                            "MAGNETIC",
                            "MAJORITY",
                            "MARGINAL",
                            "MARRIAGE",
                            "MATERIAL",
                            "MAXIMIZE",
                            "MEDICINE",
                            "MEDIEVAL",
                            "MEMORIAL",
                            "MERCHANT",
                            "MILITARY",
                            "MINIMIZE",
                            "MINISTER",
                            "MINISTRY",
                            "MINORITY",
                            "MODERATE",
                            "MOMENTUM",
                            "MOUNTAIN",
                            "MULTIPLE",
                            "NEGATIVE",
                            "NORTHERN",
                            "NUMEROUS",
                            "OBSERVER",
                            "OCCASION",
                            "OFFICIAL",
                            "OPERATOR",
                            "OPPONENT",
                            "OPPOSITE",
                            "OPTIMISM",
                            "OPTIONAL",
                            "ORDINARY",
                            "ORGANIZE",
                            "ORIGINAL",
                            "PARALLEL",
                            "PATIENCE",
                            "PERIODIC",
                            "PERSONAL",
                            "PERSUADE",
                            "PHYSICAL",
                            "PLEASANT",
                            "PLEASURE",
                            "POLITICS",
                            "PORTABLE",
                            "PORTRAIT",
                            "POSITION",
                            "POSITIVE",
                            "POSSIBLE",
                            "PRACTICE",
                            "PRECIOUS",
                            "PRINCESS",
                            "PRIORITY",
                            "PROPOSAL",
                            "PROSPECT",
                            "PROVIDER",
                            "PROVINCE",
                            "PURCHASE",
                            "QUANTITY",
                            "QUESTION",
                            "RATIONAL",
                            "REACTION",
                            "RECEIVER",
                            "RELATION",
                            "RELATIVE",
                            "RELEVANT",
                            "RELIABLE",
                            "RELIANCE",
                            "RELIGION",
                            "REMEMBER",
                            "REPORTER",
                            "REPUBLIC",
                            "REQUIRED",
                            "RESEARCH",
                            "RESIDENT",
                            "RESOURCE",
                            "RESPONSE",
                            "RESTIRCT",
                            "RIGOROUS",
                            "SCHEDULE",
                            "SEASONAL",
                            "SECURITY",
                            "SENSIBLE",
                            "SENTENCE",
                            "SEPERATE",
                            "SEQUENCE",
                            "SHIPPING",
                            "SHORTAGE",
                            "SHOULDER",
                            "SIMPLIFY",
                            "SOLUTION",
                            "SOUTHERN",
                            "SPECIFIC",
                            "SPECTRUM",
                            "STANDARD",
                            "STRAIGHT",
                            "STRATEGY",
                            "STRENGTH",
                            "STRUGGLE",
                            "STUNNING",
                            "SUPERIOR",
                            "SURPRISE",
                            "SURVIVAL",
                            "SYMBOLIC",
                            "SYMPATHY",
                            "TACTICAL",
                            "TANGIBLE",
                            "TENDENCY",
                            "TERMINAL",
                            "TERRIBLE",
                            "THIRTEEN",
                            "THOROUGH",
                            "THOUSAND",
                            "TOGETHER",
                            "TOMORROW",
                            "TRANSFER",
                            "TREASURY",
                            "TRIANGLE",
                            "TROPICAL",
                            "ULTIMATE",
                            "UMBRELLA",
                            "UNIVERSE",
                            "VALUABLE",
                            "VARIABLE",
                            "VERTICAL",
                            "VIOLENCE",
                            "WARRANTY",
                            "WEAKNESS"]
    getNewWord()
    redrawAll()

if __name__ == '__main__':
    global canvas
    root = Tk()
    canvasWidth = 1200
    canvasHeight = 720
    canvas = Canvas(root, width = canvasWidth, height = canvasHeight)
    canvas.pack()
    root.resizable(width=0, height=0)

    e1 = StringVar()
    e2 = StringVar()
    letterInput = Entry(canvas, textvariable = e1, width = 30)
    wordInput = Entry(canvas, textvariable = e2, width = 30)
    letterInput.place(x = 800, y = 350, anchor = 'center')
    wordInput.place(x = 800, y = 450, anchor = 'center')
    but1 = Button(canvas,text = 'SUBMIT', command = guessLetter)
    but2 = Button(canvas,text = 'SUBMIT', command = guessWord)
    but1.place(x = 975, y = 350, anchor = 'center')
    but2.place(x = 975, y = 450, anchor = 'center')

    class Struct: pass
    canvas.data = Struct()
    canvas.data.canvasWidth = canvasWidth
    canvas.data.canvasHeight = canvasHeight
    canvas.data.gameOver = False
    canvas.data.gameWin = False
    canvas.data.newWord = ""
    canvas.data.eachIndex = [False,False,False,False,False,False,False,False]
    canvas.data.worngWord = ["","","","","","",""]
    canvas.data.worngWordIndex = 0
    canvas.data.death = 7
    canvas.data.life = 0
    
    init()
    root.bind("<Key>", keyPressed)
    timerFired()

    root.mainloop()
