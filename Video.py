import audioop
from email.mime import audio
from tkinter import *
from tkVideoPlayer import TkinterVideo
from tkinter import messagebox
from PIL import ImageTk, Image

def film_napo():
    layar = Tk()
    layar.geometry("1000x682")
    layar.title("Film")

    re = ImageTk.PhotoImage(Image.open("film.jpg"))
    Label(layar, image=re).place(x=-0,y=0,relheight=1,relwidth=1)
    kotak_log = Frame(layar,bg="black")
    kotak_log.place(x=230,y=80,height=550,width=510)

    napo = TkinterVideo(master=kotak_log, scaled=True)
    napo.load(r"E:\Zetapulse Code\Chill Mini\film\NAPO.mp4")
    napo.pack(expand=True, fill="both")

    napo.play()

    layar.mainloop()

def film_kitbull():
    layar = Tk()
    layar.geometry("1000x682")
    layar.title("Napo")

    re = ImageTk.PhotoImage(Image.open("film.jpg"))
    Label(layar, image=re).place(x=-0,y=0,relheight=1,relwidth=1)
    kotak_log = Frame(layar,bg="black")
    kotak_log.place(x=230,y=80,height=550,width=510)

    kitbull = TkinterVideo(master=kotak_log, scaled=True)
    kitbull.load(r"E:\Zetapulse Code\Chill Mini\film\kitbull.mp4")
    kitbull.pack(expand=True, fill="both")

    kitbull.play()

    layar.mainloop()

def film_lib():
    layar = Tk()
    layar.geometry("1000x682")
    layar.title("Napo")

    re = ImageTk.PhotoImage(Image.open("film.jpg"))
    Label(layar, image=re).place(x=-0,y=0,relheight=1,relwidth=1)
    kotak_log = Frame(layar,bg="black")
    kotak_log.place(x=230,y=80,height=550,width=510)

    life = TkinterVideo(master=kotak_log, scaled=True)
    life.load(r"E:\Zetapulse Code\Chill Mini\film\LifeIsBeautiful.mp4")
    life.pack(expand=True, fill="both")

    life.play()

    layar.mainloop()

def film_purl():
    layar = Tk()
    layar.geometry("1000x682")
    layar.title("Napo")

    re = ImageTk.PhotoImage(Image.open("film.jpg"))
    Label(layar, image=re).place(x=-0,y=0,relheight=1,relwidth=1)
    kotak_log = Frame(layar,bg="black")
    kotak_log.place(x=230,y=80,height=550,width=510)

    Purl = TkinterVideo(master=kotak_log, scaled=True)
    Purl.load(r"E:\Zetapulse Code\Chill Mini\film\Purl.mp4")
    Purl.pack(expand=True, fill="both")

    Purl.play()

    layar.mainloop()

def film_sag():
    layar = Tk()
    layar.geometry("1000x682")
    layar.title("Napo")

    re = ImageTk.PhotoImage(Image.open("film.jpg"))
    Label(layar, image=re).place(x=-0,y=0,relheight=1,relwidth=1)
    kotak_log = Frame(layar,bg="black")
    kotak_log.place(x=230,y=80,height=550,width=510)

    sag = TkinterVideo(master=kotak_log, scaled=True)
    sag.load(r"E:\Zetapulse Code\Chill Mini\film\SmashAndGrab.mp4")
    sag.pack(expand=True, fill="both")

    sag.play()

    layar.mainloop()

def film_paper():
    layar = Tk()
    layar.geometry("1000x682")
    layar.title("Napo")

    re = ImageTk.PhotoImage(Image.open("film.jpg"))
    Label(layar, image=re).place(x=-0,y=0,relheight=1,relwidth=1)
    kotak_log = Frame(layar,bg="black")
    kotak_log.place(x=230,y=80,height=550,width=510)

    paper = TkinterVideo(master=kotak_log, scaled=True)
    paper.load(r"E:\Zetapulse Code\Chill Mini\film\paperman.mp4")
    paper.pack(expand=True, fill="both")

    paper.play()

    layar.mainloop()