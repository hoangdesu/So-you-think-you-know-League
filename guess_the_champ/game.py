import tkinter as tk
import os
import random
from PIL import ImageTk, Image

class Tracker:
    score = 0
    correctChoice = ''

def main():
    
    path = "./splash/"
    
    splashes = []
    for spl in os.listdir(path):
        # exlude original skins
        if "_0" not in spl:
            splashes.append(spl)
    # print(splashes)
    myfont = ("Arial", 30)
    scoreLabel = tk.Label(game, text=tracker.score, font=myfont)
    scoreLabel.pack()
    
    
    canvas = tk.Canvas(game, width=1000, height=600)
    canvas.pack()
    

    randIndex = random.randint(0, len(splashes))
    # print(randIndex)
    randChampPath = splashes[randIndex]
    randImg = path + randChampPath
    print("skin:", randChampPath)
    tracker.correctChoice = randChampPath[:randChampPath.find('_')]
    print("Correct choice:", tracker.correctChoice)
    img = ImageTk.PhotoImage(Image.open(randImg))
    
    imgContainer = canvas.create_image(1000//2, 600//2, image=img)  
    
    questionLabel = tk.Label(game, text="What is the name of this champion?")
    questionLabel.pack()
    
    buttonsFrame = tk.Frame(master=game)
    buttonsFrame.pack()
    
    fourChoices = [tracker.correctChoice]
    for i in range(3):
        newRandIndex = random.randint(0, len(splashes))
        while newRandIndex == randIndex or splashes[newRandIndex] == tracker.correctChoice:
            newRandIndex = random.randint(0, len(splashes))
        newRandChamp = splashes[newRandIndex]
        newRandChamp = newRandChamp[:newRandChamp.find("_")]
        fourChoices.append(newRandChamp)
    
    # print("before shuff", fourChoices)
    
    for i in range(4):
        randInt = random.randint(0, 3)
        temp = fourChoices[i]
        fourChoices[i] = fourChoices[randInt]
        fourChoices[randInt] = temp
        
    print("after shuf",fourChoices)
    
    def checkAns(text):
        if text == tracker.correctChoice:
            canvas.forget()
            questionLabel.forget()
            buttonsFrame.forget()
            scoreLabel.forget()
            tracker.score += 1
            main()
        else:
            tracker.score -= 1
            scoreLabel.config(text=tracker.score)
    
    
    print(tracker.score)
        
    
    btnWidth = 35
    btnHeight = 2
    btn1 = tk.Button(master=buttonsFrame, text=fourChoices[0], width=btnWidth, height=btnHeight, command=lambda: checkAns(fourChoices[0]))
    btn1.grid(row=0, column=0)

    btn2 = tk.Button(master=buttonsFrame, text=fourChoices[1], width=btnWidth, height=btnHeight, command=lambda: checkAns(fourChoices[1]))
    btn2.grid(row=0, column=1)
    
    btn3 = tk.Button(master=buttonsFrame, text=fourChoices[2], width=btnWidth, height=btnHeight, command=lambda: checkAns(fourChoices[2]))
    btn3.grid(row=1, column=0)
    
    btn4 = tk.Button(master=buttonsFrame, text=fourChoices[3], width=btnWidth, height=btnHeight, command=lambda: checkAns(fourChoices[3]))
    btn4.grid(row=1, column=1)
    
    game.mainloop()
    
    

if __name__ == '__main__':
    print("Game started")
    game = tk.Tk()
    game.title("So you think you know League?")
    tracker = Tracker()
    main()