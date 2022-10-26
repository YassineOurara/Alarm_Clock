from threading import Thread
from tkinter.ttk import *
from tkinter import *
from pygame import mixer

from datetime import datetime
from time import sleep

from PIL import ImageTk, Image

#colors
bg_color='#6EC1E4'
color1 = '#007FA4'
color2 = '#ffffff'


#window
window = Tk()
window.title("")
window.geometry('350x150')
window.configure(bg= bg_color)

#frames
frame_line = Frame(window, width=400, height=10, bg=color1)
frame_line.grid(row=0, column=0)
frame_body = Frame(window, width=400, height=200, bg=color2)
frame_body.grid(row=1, column=0)

#icon alarm
img= Image.open('alarm_icon.png')
img.resize((100,100))
img = ImageTk.PhotoImage(img)
app_image = Label(frame_body, height=100, image=img, bg=color2)
app_image.place(x=10,y=10)

#title
name = Label(frame_body, text="Alarm",height=1,font=('Ivy 18 bold'),bg=color2)
name.place(x=125,y=10)

#hour
hour = Label(frame_body, text="Hour",height=1,font=('Ivy 10 bold'),bg=color2, fg=color1)
hour.place(x=127,y=40)
cm_hour= Combobox(frame_body, width=2, font=('arial 15'))
cm_hour['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12")
cm_hour.current(0)
cm_hour.place(x=130,y=60)

#minutes
min = Label(frame_body, text="Minute",height=1,font=('Ivy 10 bold'),bg=color2, fg=color1)
min.place(x=177,y=40)
cm_min= Combobox(frame_body, width=2, font=('arial 15'))
cm_min['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
cm_min.current(0)
cm_min.place(x=180,y=60)

#secondes
sec = Label(frame_body, text="Second",height=1,font=('Ivy 10 bold'),bg=color2, fg=color1)
sec.place(x=227,y=40)
cm_sec= Combobox(frame_body, width=2, font=('arial 15'))
cm_sec['values'] = ("00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59")
cm_sec.current(0)
cm_sec.place(x=230,y=60)

#Period
period = Label(frame_body, text="Period",height=1,font=('Ivy 10 bold'),bg=color2, fg=color1)
period.place(x=277,y=40)
cm_period= Combobox(frame_body, width=3, font=('arial 15'))
cm_period['values'] = ("AM","PM")
cm_period.current(0)
cm_period.place(x=280,y=60)

#buttons

def activ_alarm():
    t = Thread(target=alarm)
    t.start()
    
def desactiv_alarm():
    print('Alarm desactivée', selected.get())
    mixer.music.stop()
    
selected = IntVar()
act = Radiobutton(frame_body, font=('arial 10 bold'), value=1, text='Activate' , bg=color2, command=activ_alarm, variable=selected)
act.place(x=125,y=95)

#run
def sound_alarm():
    mixer.music.load('alarm.mp3')
    mixer.music.play()
    selected.set(0)
    
    desact = Radiobutton(frame_body, font=('arial 10 bold'), value=2, text='Desactivate' , bg=color2, command=desactiv_alarm, variable=selected)
    desact.place(x=175,y=95)
    
def alarm():
    while True:
        control = selected.get()
        print(control)
        alarm_hour = cm_hour.get()
        alarm_minute = cm_min.get()
        alarm_sec = cm_sec.get()
        alarm_period = cm_period.get()
        alarm_period = str(alarm_period).upper()
        
        now = datetime.now()
        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime('%S')
        period = now.strftime('%p')
        
        if control == 1:
            if alarm_period == period:
                if alarm_hour == hour:
                    if alarm_minute == minute:
                        if alarm_sec == second:
                            print("Time take a break ")
                            sound_alarm()
        
        sleep(1) 
        
mixer.init()

window.mainloop()