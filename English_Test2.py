import tkinter
from tkinter import *
import random

questions=[
    'We haven’t got ..... Champagne ',
    'She has her German classes …… ',
    'Which pen do you want? ',
    'I am m going out .......some cigarettes ',
    " He says he's been robbed. He can't find his wallet ….. ",
    "I haven’t got ….. ",
    " ..... orange juice in the fridge. ",
    "We haven’t got ..... mineral water. ",
    "I have class …..",
    "John is the manager, you need to speak to ….. ",
    "He ….. breakfast yesterday ",
    " I’ve lost my keys. I can’t find them ..... ",
    "We'll never get to the airport! There is ..... time! ",
    " I haven’t seen your cousin .....over a year ago. ",
    "We're really looking forward ..... on holiday. ",
]

answers_choice=[
    ["a lot","little","too", "much"],
    ["in Tuesday mornings","at Tuesday mornings","by Tuesday mornings", "on Tuesday mornings"],
    ["A one blue ","One blue","Two blue", "The blue one. "],
    ["to buying","for buying","to buy", "for to buy"],
    ["not anywhere.","nowhere","anywhere.", "somewhere."],
    ["no money.","money.","any money.", "some money."],
    ["There isn’t no ","There is any","There isn’t any", "There aren’t no"],
    ["a lot","little","too", "much"],
    [" on Mondays ","in Mondays","at Mondays", "at Mondays"],
    ["it","him","her", "them"],
    ["hadn’t","no had","didn’t have got", "didn’t have"],
    ["anywhere.","nowhere.","everywhere", "somewhere."],
    ["few.", "too little","too much little.", "too few. "],
    ["since ", "at", "for", "during "],
    ["to go", "going", "go", "to going"],
]

answers=[3,3,3,2,2,2,2,3,0,1,3,0,1,0,3]

user_answer=[]

indexes=[]


def gen():
    global indexes
    while (len(indexes) < 10):
        x = random.randint(0, 14)
        if x in indexes:
            continue
        else:
            indexes.append(x)


def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
        background="#ffffff",
        border=0,
    )
    labelimage.pack(pady=(50, 30))
    labelresulttext = Label(
        root,
        font=("Consolas", 20),
        background="#ffffff",
    )
    labelresulttext.pack()
    if score >= 10 and score>=8:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Your grade is A. You have {} points".format(score))
    elif (score >=6 or score==7):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Your grade is B.You have {} points".format(score))
    elif (score>=5 or score==6):
        img=PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="Your grade is C. You have {} points.".format(score))
    elif (score>=4 or score==5):
        img=PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image=img
        labelresulttext.configure(text="Your grade is D. You have {} points".format(score))
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="Your grade is F. !!You have {} points".format(score))


def calc():
    global indexes, user_answer, answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 1
        x += 1
    showresult(score)


ques = 1


def selected():
    global radiovar, user_answer
    global lblQuestion, r1, r2, r3, r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 10:
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()


def startquiz():
    global lblQuestion, r1, r2, r3, r4
    lblQuestion = Label(
        root,
        text=questions[indexes[0]],
        font=("Consolas", 16),
        width=500,
        justify="center",
        wraplength=400,
        background="#ffffff",
    )
    lblQuestion.pack(pady=(100, 30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][0],
        font=("Times", 12),
        value=0,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][1],
        font=("Times", 12),
        value=1,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][2],
        font=("Times", 12),
        value=2,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text=answers_choice[indexes[0]][3],
        font=("Times", 12),
        value=3,
        variable=radiovar,
        command=selected,
        background="#ffffff",
    )
    r4.pack(pady=5)


def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    gen()
    startquiz()


root=tkinter.Tk()
root.title("English Test")
root.geometry("700x562")
root.config(background="#ffffff")
root.resizable(0,0)

img1=PhotoImage(file="english.png")

labelimage=Label(
    root,
    image=img1,
    background="#ffffff",
)

labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "English Test",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)

labeltext.pack(pady=(0,50))

img2=PhotoImage(file="start.png")

btnStart=Button(
    root,
    image=img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)

btnStart.pack()

lblInstruction=Label(
    root,
    text="Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Consolas",14),
    justify = "center",
)

lblInstruction.pack(pady=(10,100))

lblRules = Label(
    root,
    text="This test contains 10 questions\n"
         "Once you select a radio button that will be a final choice",
    width = 100,
    font = ("Times",16),
    background="#000000",
    foreground="#FACA2F",
)

lblRules.pack()

root.mainloop()
