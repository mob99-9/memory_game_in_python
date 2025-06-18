from tkinter import *
from system import *
#show random letters
main_menu = Tk()

main_menu.title("Memory")
main_menu.geometry("720x480")

title = Label(main_menu, text="Memory", font=(50))
title.pack()

class GameMaster(Arbiter):
    def Hello(self):
        pass

game = GameMaster()

code = Label(main_menu, text=f"{game.randomizer()}", fg="BLACK", font=(300))
code.place(x=330, y=90)

#show timer and blocker 


#create entry box 

#show score

main_menu.mainloop()