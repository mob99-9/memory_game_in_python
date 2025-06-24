from tkinter import *
from system import *

main_menu = Tk()

main_menu.title("Memory")
main_menu.geometry("720x480")

title = Label(main_menu, text="Memory", font=(50))
title.pack()

class GameMaster(GameSystem):
    def show_code(self):
        global code
        def blocker():
            code.config(bg="BLACK")

        code = Label(main_menu, text=f"{game.randomizer()}", fg="BLACK", font=("Comic Sans", 20))
        code.place(x=320, y=70)

        code.after(5000, blocker)

    def user_entry(self):
        global ask_user
        ask_user = Entry(main_menu)
        ask_user.place(x=310, y=280)

    def user_submit(self):
        submit_button = Button(main_menu, text="Submit", command=game.check_user)
        submit_button.place(x=340,y=300)

    def check_user(self):
        user_code = ask_user.get()
        user_answer = game.scorer(user_code)

        score = Label(main_menu, padx= 720, pady=480, font=(300), bg=f"{user_answer}")
        score.pack()

        game.restart_button()
        game.exit_button()

    def start_button(self):
        start_b = Button(main_menu, text="Start", command=start_game)
        start_b.place(x=340, y=300)

    def exit_button(self):
        exit_b = Button(main_menu, text="Exit", command=exit)
        exit_b.place(x=340, y=330)

    def restart_button(self):
        restart_b = Button(main_menu, text="Restart", command=restart_game)
        restart_b.place(x=340, y=300)



game = GameMaster()

def start_game():
    game.show_code()
    game.user_entry()
    game.user_submit()
    game.exit_button()

def restart_game():
    for widgets in main_menu.winfo_children():
            widgets.destroy()
    game.show_code()
    game.user_entry()
    game.user_submit()
    game.exit_button()    

if __name__ == "__main__":
    game.start_button()


main_menu.mainloop()