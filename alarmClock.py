from tkinter import *
import datetime as dt
import time  # Add the time module import
import winsound as ws

def alarm(setAlarmTimer):
    while True:
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%H:%M:%S")
        currentDate = actualTime.strftime("%d/%m/%Y")
        the_message = "Current Time: " + currentTime
        print(the_message)
        if currentTime == setAlarmTimer:
            ws.PlaySound("sound.wav", ws.SND_ASYNC)
            break
        time.sleep(1)

def getAlarmTime():
    alarmSetTime = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm(alarmSetTime)

guiWindow = Tk()
guiWindow.title("The Alarm Clock")
guiWindow.geometry("464x200")
guiWindow.config(bg="#1E1E1E")

# Use a beautiful font for the labels
labelFont = ("Helvetica", 12, "bold")

timeFormat = Label(
    guiWindow,
    text="Remember to set time in 24-hour format!",
    fg="white",
    bg="#1E1E1E",
    font=labelFont
)
timeFormat.place(x=0, y=160)

add_time = Label(
    guiWindow,
    text="Hour     Minute     Second",
    font=("Courier", 12),
    fg="white",
    bg="#1E1E1E"
)
add_time.place(x=220, y=10)

setAlarm = Label(
    guiWindow,
    text="Set Time for Alarm: ",
    fg="white",
    bg="#1E1E1E",
    relief="solid",
    font=labelFont
)
setAlarm.place(x=5, y=50)

hour = StringVar()
minute = StringVar()
second = StringVar()

hourTime = Entry(
    guiWindow,
    textvariable=hour,
    bg="#363636",
    fg="white",
    width=4,
    font=("Arial", 12)
)
hourTime.place(x=220, y=53)

minuteTime = Entry(
    guiWindow,
    textvariable=minute,
    bg="#363636",
    fg="white",
    width=4,
    font=("Arial", 12)
)
minuteTime.place(x=297, y=53)

secondTime = Entry(
    guiWindow,
    textvariable=second,
    bg="#363636",
    fg="white",
    width=4,
    font=("Arial", 12)
)
secondTime.place(x=390, y=53)

submit = Button(
    guiWindow,
    text="Set The Alarm",
    fg="white",
    bg="#4CAF50",
    width=15,
    command=getAlarmTime,
    font=("Helvetica", 12, "bold")
)
submit.place(x=140, y=100)

guiWindow.mainloop()
