from tkinter import *
from tkinter import ttk
from poke import search_dict
import ast

with open("pikalytics.stats", "r") as rf:
	pokedict = ast.literal_eval(rf.read())

# root window
root = Tk()
root.geometry('600x350')
root.title('Trainer Trainer')
root.configure(bg = "#ececec")

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=20, side=BOTTOM)

type_colors = {
	"normal": "#F0F0F0", 
	"fighting": "#F0A0A0", 
	"ghost": "#7070F0", 
	"bug": "#D0F0C0", 
	"dark": "#505040", 
	"psychic": "#F0A0D0", 
	"fairy": "#F0D0D0", 
	"flying": "#A0D0F0", 
	"fire": "#F0A050", 
	"water": "#A0A0F0", 
	"grass": "#A0F0A0", 
	"ground": "#404000", 
	"poison": "#A030A0", 
	"steel": "#D0D0D5", 
	"rock": "#808040", 
	"ice": "#E0FFF0", 
	"electric": "#F0F0A0", 
	"dragon": "#F0D0F0"
}

bg_list = ["#FFF5F5", "#FFF5F0", "#FFFFEE", "#F5FFF5", "#F5F5FF", "#FAF5FF"]

pokemon = ["Zacian-*", "Blissey", "Mawile", "Ditto", "Marshadow", "Kyogre"]


for pos, mon in enumerate(pokemon):
    	
	info = search_dict(mon, pokedict)[0]
	tab = Frame(notebook, bg=bg_list[pos], width=600, height=200, highlightbackground="#D0A0A0", highlightthickness=1)
	
    
	tab.pack()

	notebook.add(tab, text=info["name"])
	
	move_text = ""
	
	moveframe = Frame(tab, bg="#F0F0F0", width = 400, height = 200, highlightbackground="#E0E0E0", highlightthickness=10)
	moveframe.pack(side = LEFT, padx = 10)

	for row, move in enumerate(info["moves"]):
		if "move" in move.keys():
			if move["move"] != "Other":

				Button(moveframe, text = move["move"], highlightbackground = type_colors[move["type"]], height = 1, width = 15).grid(sticky = "w", row = row*2)
				#Separator(moveframe, orient='horizontal').grid(sticky = "we")
				#Label(moveframe, text = move["percent"], bg = "#F0F0F0").grid(sticky = "e", row = row*2, column = 20)


root.mainloop()
