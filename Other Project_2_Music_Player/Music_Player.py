from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MyMusic:
    def __init__(self, window ):
        window.geometry('320x190'); window.title('Soham Ray\'s Internship'); window.resizable(0,0)
        frame = LabelFrame(window, text='NexusByte Music Player', bg='#ff99ff',font=(20))
        frame.pack(expand=True, fill=BOTH)
        my_str = StringVar()
        l2 = Label(window,textvariable=my_str,fg='blue' )
        l2.place(x=10, y=50)
        my_str.set("Selected File : ")
        Load = Button(window, text = 'Load',  width = 15, font = ('Times', 10), command = self.load)
        
        Play = Button(window, text = 'Play',  width = 15,font = ('Times', 10), command = self.play)
        Pause = Button(window,text = 'Pause/Resume',  width = 15, font = ('Times', 10), command = self.pause)
        Stop = Button(window ,text = 'Stop',  width = 15, font = ('Times', 10), command = self.stop)
        Load.place(x=30,y=90);Play.place(x=170,y=90);Pause.place(x=30,y=130);Stop.place(x=170,y=130) 
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
        my_str1 = StringVar()
        l3 = Label(textvariable=my_str1,fg='red' )
        l3.place(x=90, y=50)
        musicname = self.music_file.split('/')[-1][:30] + '...mp3'
        my_str1.set(musicname)
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
root = Tk()
app= MyMusic(root)
root.mainloop()
