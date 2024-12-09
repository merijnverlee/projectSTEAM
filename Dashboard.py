import tkinter as tk
from datetime import datetime

print(datetime.now().strftime('%A, %d, %B %Y\n'))
print("AAN HET LADEN....")

root = tk.Tk()
root.resizable(False, False)
root.geometry('1305x780')
root.title("Project Steam")
root.configure(bg='#c7d5e0')

# DRAW TOP BLUE BAR - DRAW TITLE - DRAW DATETIME
top_bg = tk.Canvas(root, width=1305, height=60, bg='#1b2838', highlightthickness=0).place(x=0, y=0)
tk.Label(top_bg, text='Project Steam', font='Montserrat 25', bg='#1b2838', fg='white').place(x=15, y=3)
tk.Label(top_bg, text=datetime.now().strftime('%A, %d %B %Y'), font='Montserrat 20', bg='#1b2838', fg='white').place(
    x=930, y=8)

# STEAM TOP SELLING
steam_box = tk.Canvas(root, width=590, height=520, bg='#2a475e', highlightthickness=0).place(x=390, y=240)
steam_box_top = tk.Canvas(root, width=590, height=20, bg='#1b2838', highlightthickness=0).place(x=390, y=220)
steam_box_price = tk.Canvas(steam_box, width=80, height=520, bg='#171a21', highlightthickness=0).place(x=900, y=240)
tk.Label(steam_box_top, text='Steam Beste Reviews', font='Montserrat 8 bold', bg='#1b2838',
         fg='#FFFFFF').place(x=395, y=220)

#WEER
weather_box = tk.Canvas(root, width=1265, height=100, bg='#2a475e', highlightthickness=0).place(x=20, y=100)
weather_box_top = tk.Canvas(root, width=1265, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=80)
tk.Label(weather_box_top, text='Weersvoorspelling, Utrecht NL.', font='Montserrat 8 bold', bg='#1b2838',
         fg='#FFFFFF').place(x=25, y=80)

# PI
pihole_box = tk.Canvas(root, width=350, height=140, bg='#2a475e', highlightthickness=0).place(x=20, y=240)
pihole_box_top = tk.Canvas(root, width=350, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=220)
pihole_box_temp = tk.Canvas(pihole_box, width=350, height=30, bg='#2a475e', highlightthickness=0).place(x=20, y=240)
pihole_box_middle = tk.Canvas(pihole_box, width=350, height=20, bg='#171a21', highlightthickness=0).place(x=20, y=270)
tk.Label(pihole_box_top, text='Raspberry PI', font='Montserrat 8 bold', bg='#1b2838', fg='#FFFFFF') \
    .place(x=25, y=220)

# Vriendenlijst


vriendenlijst= tk.Canvas(root, width=350, height=160, bg='#2a475e', highlightthickness=0).place(x=20, y=420)
hdd_box_top = tk.Canvas(root, width=350, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=400)
tk.Label(hdd_box_top, text='Online vrienden', font='Montserrat 8 bold', bg='#1b2838', fg='#FFFFFF') \
    .place(x=25, y=400)

# NOS Nieuws
threshold_box = tk.Canvas(root, width=285, height=520, bg='#2a475e', highlightthickness=0).place(x=1000, y=240)
threshold_box_top = tk.Canvas(root, width=285, height=20, bg='#1b2838', highlightthickness=0).place(x=1000, y=220)
tk.Label(threshold_box_top, text='NOS Nieuws', font='Montserrat 8 bold', bg='#1b2838',
         fg='#FFFFFF').place(x=1005, y=220)

#DATABASE
news_box = tk.Canvas(root, width=350, height=140, bg='#2a475e', highlightthickness=0).place(x=20, y=620)
news_box_top = tk.Canvas(root, width=350, height=20, bg='#1b2838', highlightthickness=0).place(x=20, y=600)
tk.Label(news_box_top, text='DATABASE', font='Montserrat 8 bold', bg='#1b2838',
         fg='#FFFFFF').place(x=25, y=600)


root.mainloop()