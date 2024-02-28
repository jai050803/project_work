import tkinter as tk
from tkinter import PhotoImage,Frame, Button

root = tk.Tk()
root.title("Dashboard")
root.state("zoomed")
root.title('EMS - A Business Intelligence tool')
root.configure(bg="#eff5f6")
image_icon = PhotoImage(file="logo.png")
root.iconphoto(False,image_icon)

#sidebar
sidebar = Frame(root, bg="#ffffff")
sidebar.place(x=0,y=0,width=200,height=700)

header = Frame(root, bg="#009df4", width=1366, height=60)
header.place(x=200, y=0)

home_button = Button(sidebar, text="User Dashboard",border = 0, font="arial 10 bold", bg="#ffffff", fg="black", cursor="hand2")
home_button.place(x=34,y=105)

data_wrangling_button = Button(sidebar, text="Data Wrangling",border = 0, font="arial 10 bold", bg="#ffffff", fg="black", cursor="hand2")
data_wrangling_button.place(x=35,y=175)

data_statistics_button = Button(sidebar, text="Data Statistics",border = 0, font="arial 10 bold", bg="#ffffff", fg="black", cursor="hand2")
data_statistics_button.place(x=40,y=245)

data_visualization_button = Button(sidebar, text="data Visualization",border = 0, font="arial 10 bold", bg="#ffffff", fg="black", cursor="hand2")
data_visualization_button.place(x=25,y=315)

root.mainloop()