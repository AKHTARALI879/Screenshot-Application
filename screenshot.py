import pyautogui
from tkinter import *
from tkinter.filedialog import *

csa = Tk()
csa.title("Screenshot App")
csa.geometry("500x500")


def take_screenshot():
    myscreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myscreenshot.save(save_path + "_screenshot.png")


button = Button(csa, text="Take Screenshot", fg="#5B5B5B", bg="#808080", font=(
    "Cooper Black", 20, "bold"), relief=RAISED, command=take_screenshot)
button.place(x=85, y=400, height=50, width=330)
csa.mainloop()
