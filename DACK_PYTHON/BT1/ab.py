import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu, messagebox as msg

win = tk.Tk()
win.title("Python GUI")

mighty = ttk.LabelFrame(win, text="Mighty Python")
mighty.grid(column=0, row=0, padx=10, pady=10)

ttk.Label(mighty, text="Enter a name: ").grid(column=0, row=0, sticky="W")
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=1, row=0, sticky="W")
name_entered.focus()

def click_me():
    action.configure(text=f"Hello {name.get()}")

action = ttk.Button(mighty, text="Click Me!", command=click_me)
action.grid(column=2, row=0, padx=5)

ttk.Label(mighty, text="Choose a number:").grid(column=0, row=1, sticky="W")
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number)
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1, sticky="W")
number_chosen.current(0)

ttk.Label(mighty, text="Spinbox:").grid(column=0, row=2, sticky="W")
spin = ttk.Spinbox(mighty, from_=0, to=10, width=5)
spin.grid(column=1, row=2, sticky="W")

scrol_w, scrol_h = 30, 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=3, columnspan=3, pady=10)


check_frame = ttk.LabelFrame(win, text="Options")
check_frame.grid(column=0, row=1, padx=10, pady=10)

chVarDiss = tk.IntVar()
check1 = tk.Checkbutton(check_frame, text="Disabled", variable=chVarDiss, state="disabled")
check1.select()
check1.grid(column=0, row=0, sticky="W")

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(check_frame, text="Unchecked", variable=chVarUn)
check2.grid(column=1, row=0, sticky="W")

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(check_frame, text="Enabled", variable=chVarEn)
check3.select()
check3.grid(column=2, row=0, sticky="W")

def rad_call():
    rad_sel = radVar.get()
    colors = {1: "Blue", 2: "Gold", 3: "Red"}
    win.configure(background=colors.get(rad_sel, "White"))

radVar = tk.IntVar()
radio_frame = ttk.LabelFrame(win, text="Choose Color")
radio_frame.grid(column=0, row=2, padx=10, pady=10)

colors = ["Blue", "Gold", "Red"]
for idx, color in enumerate(colors, 1):
    rad = tk.Radiobutton(radio_frame, text=color, variable=radVar, value=idx, command=rad_call)
    rad.grid(column=idx - 1, row=0, sticky="W")

menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=win.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

def _msg_box():
    msg.showinfo("About", "This is a Python GUI example using Tkinter.")

help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msg_box)
menu_bar.add_cascade(label="Help", menu=help_menu)

win.mainloop()
