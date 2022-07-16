from tkinter import *
import datetime
import time

def alaram(set_alaram_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The set date is: ",date)
        print(now)
        if now==set_alaram_timer:
            print("Time to wake up")
        try:
            import winsound
        except ImportError:
            import os
            def playsound(frequency,duration):
                os.system('beep -f %s -l %s' % (frequency,duration))
        else:
            def playsound(frequency,duration):
                winsound.Beep(frequency,duration)

        break

def actual_time():
    set_alaram_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alaram(set_alaram_timer)

clock = Tk()
clock.title("DataFlair Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=30)

submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)

clock.mainloop()