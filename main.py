from tkinter import *
from system import *

# this is the view of the app

main_menu = Tk()

main_menu.title("Memory")

player = Player()

player.ask_player_name()

main_menu.mainloop()