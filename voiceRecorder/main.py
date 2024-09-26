from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import StringVar
import sounddevice as sound
from scipy.io.wavfile import write
import time
import wavio as wv

root=Tk()
root.geometry("600x700+400+80")
root.resizable(False,False)
root.title("Voice Recorder")
root.config(bg="#4a4a4a")

def Record():
    freq=44100
    dur=int(duration.get())
    recording=sound.rec(dur*freq, samplerate=freq, channels=2)
    
    #timer
    try:
        temp=int(duration.get())
    except:
        print("Please enter the right value")
    while temp>0:
        root.update()
        time.sleep(1)
        temp-=1
        if(temp==0):
            messagebox.showinfo("Time Countdown", "Time's up")
        Label(text=f"{str(temp)}", font="arial 40", width=4, bg="#4a4a4a").place(x=240,y=590)
    
    sound.stop()
    sound.wait()
    write("recording.wav", freq, recording)
    messagebox.showinfo("Voice Recorder", "Recording Saved")


#icon
image_icon=PhotoImage(file="Record.png")
root.iconphoto(False,image_icon)

#logo
photo=PhotoImage(file="Record.png")
myimage=Label(image=photo, bg="#4a4a4a")
myimage.pack(padx=5,pady=5)

#name
Label(root, text="Voice Recorder", font="arial 30 bold", bg="#4a4a4a", fg="white").pack()

#entry box
duration=StringVar()
entry=Entry(root, textvariable=duration, font="arial 20", width=15).pack(pady=10)
Label(text="Enter the time duration in sec", font="arial 15", bg="#4a4a4a", fg="white").pack()

#button
record=Button(root, font="arial 20", text="Record Audio", bg="#39c790", fg="white", border=0,command=Record).pack(pady=30)




root.mainloop()