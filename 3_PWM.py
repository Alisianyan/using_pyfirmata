#-----------------------------------------------------
# GUI to turn ON blue/red LED with brightness control
#-----------------------------------------------------
import tkinter as tk
from tkinter import messagebox
from pyfirmata import Arduino, PWM
is_red_butt_on = False
is_blue_butt_on = False
from time import sleep
# Functions=========================================================
def redLED():

    brightness = float(LEDredbright.get())
    board.digital[3].write(brightness/100.0)

#--------------------------------------------
def greenLED():
    brightness = float(LEDgreenbright.get())
    board.digital[6].write(brightness/100.0)
#--------------------------------------------
def blueLED():

    brightness = float(LEDbluebright.get())
    board.digital[5].write(brightness/100.0)

#--------------------------------------------
def aboutMsg():
    messagebox.showinfo("About",
    "Logic Don't Care Software\nLED Control Ver 1.0\nAugust 2022")
#=================================================================
# Arduino board connected to serial port COM3
board = Arduino("COM4")
# set mode of Arduino pins D3 & D5 for PWM
board.digital[3].mode = PWM
board.digital[5].mode = PWM
#--------------------------------------------
# initialize window with title & size
win = tk.Tk()
win.title("LED Control")
win.minsize(235,150)
#--------------------------------------------
# Scale widget
LEDredbright = tk.Scale(win, bd=5, from_=0, to=100, orient=tk.HORIZONTAL)
LEDredbright.grid(column=2, row=1)
# Label widget
tk.Label(win, text="Red LED Brightness (%)").grid(column=3, row=1)
#--------------------------------------------
# Scale widget
LEDgreenbright = tk.Scale(win, bd=5, from_=0, to=100, orient=tk.HORIZONTAL)
LEDgreenbright.grid(column=2, row=2)
# Label widget
tk.Label(win, text="Green LED Brightness (%)").grid(column=3, row=2)
#--------------------------------------------
# Scale widget
LEDbluebright = tk.Scale(win, bd=5, from_=0, to=100, orient=tk.HORIZONTAL)
LEDbluebright.grid(column=2, row=3)
# Label widget
tk.Label(win, text="Blue LED Brightness (%)").grid(column=3, row=3)
#--------------------------------------------
# Button widgets
redBtn = tk.Button(win, bd=5, bg='#FF6666', text="LED ON", command=redLED)
redBtn.grid(column=1, row=1)

greenBtn = tk.Button(win, bd=5, bg='#90EE90', text="LED ON", command=greenLED)
greenBtn.grid(column=1, row=2)

blueBtn = tk.Button(win, bd=5, bg='#ADD8E6', text="LED ON", command=blueLED)
blueBtn.grid(column=1, row=3)

quitBtn = tk.Button(win, text="Quit", command=win.quit)
quitBtn.grid(column=2, row=5)
#--------------------------------------------
win.mainloop()