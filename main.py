from tkinter import *
from system import *
#show random letters
main_menu = Tk()

main_menu.title("Memory")
main_menu.geometry("720x480")

title = Label(main_menu, text="Memory", font=(50))
title.pack()

class GameMaster(Arbiter):

    def show_code(self):
        code = Label(main_menu, text=f"{game.randomizer()}", fg="BLACK", font=(300))
        code.place(x=330, y=90)

    def user_entry(self):
        global ask_user
        ask_user = Entry(main_menu)
        ask_user.place(x=310, y=280)

    def user_submit(self):
        submit_button = Button(main_menu, text="Submit", command=game.check_user)
        submit_button.place(x=340,y=300)

    def check_user(self):
        user_code = ask_user.get()
        game.scorer(user_code)
        
game = GameMaster()

game.show_code()
game.user_entry()
game.user_submit()

#show timer and blocker 


#create entry box 

#show score

main_menu.mainloop()