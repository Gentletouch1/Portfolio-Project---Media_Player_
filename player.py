#setup screen= -
from tkinter import *
from PIL import Image,ImageTk
import os
import time
import tkinter.messagebox
from tkinter import filedialog
from pygame import mixer
from mutagen.mp3 import MP3
mixer.init()

class musicplayer:
    def __init__(self,Tk):
        self.root=Tk
        self.root.title('Music_Player')
        self.root.geometry('700x600')
        self.root.configure(background='magenta')
        
        #openfile---
        def Openfile():
            global filename
            filename=filedialog.askopenfilename()

        image_icon = PhotoImage(file='logo G3.png')
        root.iconphoto(False, image_icon)

        #Menu
        self.menubar=Menu(self.root)
        self.root.configure(menu=self.menubar)

        self.submenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Media',menu=self.submenu)
        self.submenu.add_command(label='Open',command=Openfile)
        self.submenu.add_command(label='Exit',command=self.root.destroy)

        self.submenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Audio',menu=self.submenu)
        self.submenu.add_command(label='Increase Volume')
        self.submenu.add_command(label='Decrease Volume')
        self.submenu.add_command(label='Mute')

        def About():
            tkinter.messagebox.showinfo('About Us','Music Player created By Gentletouch')


        self.submenu=Menu(self.menubar,tearoff=0)
        self.menubar.add_cascade(label='Help',menu=self.submenu)
        self.submenu.add_command(label='About',command=About)


        #Adding Label---
        self.filelabel=Label(text='Gentletouch Music Player',bg='indigo',fg='red',font=30)
        self.filelabel.place(x=50,y=15)
        self.label1=Label(self.root,text='Music is the Soul of Life',bg='black',fg='white',font=20)
        self.label1.pack(side=BOTTOM,fill=X)

        def songinf():
            self.filelabel['text']='Current Music :-' + os.path.basename(filename)

    
        #functions--
        def playmusic():
            try:
                paused
            except NameError:
                try:   
                    mixer.music.load(filename)
                    mixer.music.play()
                    self.label1['text']='Music_Playing...'
                    songinf()
                    length_bar()

                                                       
                except:
                    tkinter.messagebox.showerror('Error','File could Not Found, Please try Again...')

            else:
                mixer.music.unpause()
                self.label1['text']='Music_Unpaused'

            #self.im1=ImageTk.PhotoImage(file='skin5.jpeg')
            #self.im2=ImageTk.PhotoImage(file='skin6.jpeg')
            #self.im3=ImageTk.PhotoImage(file='skin7.jpeg')
            #self.im4=ImageTk.PhotoImage(file='skin8.jpeg')

            self.imglabel=Label(self.root,bg='indigo')
            self.imglabel.place(x=50,y=50)
                        
            animation()

                                              
        def stopmusic(): 
            mixer.music.stop()
            self.label1['text']='Music_Stopped...'

        def pausemusic():
            global paused
            paused=TRUE
            mixer.music.pause()
            self.label1['text']='Music_Paused...'

        #Mute--
        def mute():
            self.scale.set(0)
            self.mute=ImageTk.PhotoImage(file='mute.png')
            mute=Button(self.root,image=self.mute,command=unmute,bd=1,bg='yellow').place(x=310,y=520,width=40,height=40)
            self.label1['text']='Music_mute'

        #unmute--
        def unmute():
            self.scale.set(25)
            self.volimg=ImageTk.PhotoImage(file='speaker.png')
            volimg=Button(self.root,image=self.volimg,command=mute,bg='blue',bd=1).place(x=310,y=520,width=40,height=40)
            self.label1['text']='Music_unmute'

        #Animation--
        def animation():
            #self.im1=self.im2
            #self.im2=self.im3
            #self.im3=self.im4
            #self.im4=self.im1
            #self.imglabel.config(image=self.im1)
            #self.imglabel.after(1000,animation)


        #Adding leftside image--
            L=LEFT
        self.L_photo=ImageTk.PhotoImage(file='b2.png')
        L_photo=Label(self.root,image=self.L_photo).place(x=50,y=50,width=500,height=400)
        
        #Adding img--
        self.photo=ImageTk.PhotoImage(file='vi2.1.png')
        photo=Label(self.root,image=self.photo,bg='white').place(x=50,y=50,width=600,height=400)

        #frameCnt =30
        #frames=[PhotoImage(file='animation.gif', format = 'gif -index %i' %(i)) for i in range(frameCnt)]
                  
        #def update(ind):

        #    frame = frame[ind]
        #    ind +=1
        #    if ind == frameCnt:
        #        ind = 0
        #    label.configure(image=frame)
        #    root.after(40,update,ind)  
        #label=Label(root)
        #label.place(x=0,y=0)
        #root.after(0, update, 0)


        #for song length--
        def length_bar():
            #starting from zero
            current_time=mixer.music.get_pos()/1000
            convert_current_time=time.strftime('%M:%S',time.gmtime(current_time))

            print(convert_current_time)

            #select mp3 songs
            song_mut=MP3(filename)
            #get length of songs
            song_mut_length=song_mut.info.length
            #convert into min and sec
            convert_song_mut_length=time.strftime('%M:%S',time.gmtime(song_mut_length))
            #Blitz on screen--
            self.lengthbar.config(text=f'Total_Length:-{convert_current_time}:{convert_song_mut_length}')
            self.lengthbar.after(1000,length_bar)

            

                        

            song_mut=MP3(filename)
            song_mut_length=song_mut.info.length
            


        #label for length bar--
        self.lengthbar=Label(self.root,text='Total_Length:00:00',font=20,bg='pink',fg='purple')
        self.lengthbar.place(x=50,y=480)

        


        #Creating Button--
        #Play_button--
        self.photo_B1=ImageTk.PhotoImage(file='play.png')
        photo_B1=Button(self.root,image=self.photo_B1,bd=10,bg='orange',command=playmusic).place(x=50,y=520,width=50,height=50)

        #Pause_button--
        self.photo_B2=ImageTk.PhotoImage(file='pause.png')
        photo_B2=Button(self.root,image=self.photo_B2,bd=10,bg='blue',command=pausemusic).place(x=120,y=520,width=50,height=50)

        #Stop_button--
        self.photo_B3=ImageTk.PhotoImage(file='stop.png')
        photo_B3=Button(self.root,image=self.photo_B3,bd=10,bg='white',command=stopmusic).place(x=190,y=520,width=50,height=50)

        #Volume BarImg--
        self.volimg=ImageTk.PhotoImage(file='speaker.png')
        volimg=Button(self.root,image=self.volimg,command=mute,bg='blue',bd=1).place(x=310,y=520,width=40,height=40)

        #Function for volume bar--
        def volume(vol):
            volume=int(vol)/100
            mixer.music.set_volume(volume)


        #Volume bar--
        self.scale=Scale(self.root,from_=0,to=100,bg='green',
                         orient=HORIZONTAL,length=150,command=volume)
        self.scale.set(25)
        self.scale.place(x=350,y=520)

        #RES
        self.root.resizable(0,0)

        
        












        

root=Tk()
obj=musicplayer(root)
root.mainloop()