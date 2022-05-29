from cProfile import label
from logging import root
from sqlite3 import Cursor
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import ast
from tkVideoPlayer import TkinterVideo
from sinopsis import sinopsis_paper

#------------------------------------------------------------------------------------------------#
#Kotak Background
film1 = Tk()
film1.geometry("1200x720")
film1.title("Menu")   

bg = ImageTk.PhotoImage(Image.open("utama.jpg"))
Label(film1, image=bg).place(x=-0,y=0,relheight=1,relwidth=1)

kotak_menu= Frame(film1,bg="black")
kotak_menu.place(x=55,y=80,height=1000,width=1100)

#------------------------------------------------------------------------------------------------#
#tulisan + accesories animasi
tulis1=Label(film1,text="Animasi:",bg="red",fg="white",font=("Times New Roman",24,"bold"))
tulis1.place(x=80,y=100)

#------------------------------------------------------------------------------------------------#
def sinopsis_kittbull():
    sinopsis1 = Toplevel(film1)
    sinopsis1.geometry("1200x720")
    sinopsis1.title("Sinopsis")   

    bg = ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\zenith.jpg"))
    Label(sinopsis1, image=bg).place(x=-0,y=0,relheight=1,relwidth=1)
    #------------------------------------------------------------------------------------------------#
    #system film kitbull
    def film_kitbull():
        layar = Toplevel(sinopsis1)
        layar.geometry("1000x682")
        layar.title("Kitbull")


        re = ImageTk.PhotoImage(Image.open("film.jpg"))
        Label(layar, image=re).place(x=-0,y=0,relheight=1,relwidth=1)
        kotak_log = Frame(layar,bg="black")
        kotak_log.place(x=230,y=80,height=550,width=510)

        kitbull = TkinterVideo(master=kotak_log, scaled=True)
        kitbull.load(r"E:\Zetapulse Code\Chill Mini\film\kitbull.mp4")
        kitbull.pack(expand=True, fill="both")

        kitbull.play()

        layar.mainloop()

    #------------------------------------------------------------------------------------------------#
    #sinopsis dan tombol kitbull
    kitbull_poster_tempat=Frame(sinopsis1,bg="black")
    kitbull_poster_tempat.place(x=700,y=100,height=500,width=400)
    kitbull_poster= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\kitbull_poster_bg.jpg"))
    Label(kitbull_poster_tempat,image=kitbull_poster).place(x=0,y=0,relheight=1,relwidth=1)
    kitbull_judul_tempat=Frame(sinopsis1,bg="black")
    kitbull_judul_tempat.place(x=55,y=100,height=50,width=400)
    kitbull_judul=Label(kitbull_judul_tempat,text="Kitbull",bg="black",fg="white",font=("Times New Roman",30,"bold"))
    kitbull_judul.place(x=140,y=0)
    kitbull_sin_tempat= Frame(sinopsis1,bg="black")
    kitbull_sin_tempat.place(x=55,y=160,height=450,width=400)
    kitbull_sin1=Label(kitbull_sin_tempat,text="An unlikely connection sparks between two creatures:",bg="black",fg="white",font=("Times New Roman",14))
    kitbull_sin1.place(x=0,y=0)
    kitbull_sin2=Label(kitbull_sin_tempat,text="a fiercely independent stray kitten and a pit bull.",bg="black",fg="white",font=("Times New Roman",14))
    kitbull_sin2.place(x=0,y=25)
    kitbull_sin3=Label(kitbull_sin_tempat,text="Together they experience friendship for the first time.",bg="black",fg="white",font=("Times New Roman",14))
    kitbull_sin3.place(x=0,y=50)
    kitbull_tonton=Frame(kitbull_sin_tempat,bg="white")
    kitbull_tonton.place(x=150,y=90,height=40,width=100)
    tonton= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\sag_poster_mini.jpg"))
    Button(kitbull_tonton,image=tonton,cursor="hand2",command=film_kitbull).place(x=0,y=0,relheight=1,relwidth=1)

    sinopsis1.mainloop()
#------------------------------------------------------------------------------------------------#
#poster kitbull
poster_letak1=Frame(film1,width=130,height=150,bg="white")
poster_letak1.place(x=65,y=150)
poster_kitbull= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\kitbull_poster_mini.jpg"))
Button(poster_letak1,image=poster_kitbull,cursor="hand2",command=sinopsis_kittbull).place(x=0,y=0,relheight=1,relwidth=1)
tulispost1=Label(film1,text="Kitbull",bg="black",fg="white",font=("Times New Roman",14,"bold"))
tulispost1.place(x=100,y=300)

#------------------------------------------------------------------------------------------------#
def sinopsis_lib():
    sinopsis1 = Toplevel(film1)
    sinopsis1.geometry("1200x720")
    sinopsis1.title("Sinopsis")   

    bg = ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\zenith.jpg"))
    Label(sinopsis1, image=bg).place(x=-0,y=0,relheight=1,relwidth=1)
    #------------------------------------------------------------------------------------------------#
    #system film lib
    def film_lib():
        layar = Toplevel(sinopsis1)
        layar.geometry("1000x682")
        layar.title("Life Is Beautiful")

        re = ImageTk.PhotoImage(Image.open("film.jpg"))
        Label(layar, image=re).place(x=-0,y=0,relheight=1,relwidth=1)
        kotak_log = Frame(layar,bg="black")
        kotak_log.place(x=230,y=80,height=550,width=510)

        life = TkinterVideo(master=kotak_log, scaled=True)
        life.load(r"E:\Zetapulse Code\Chill Mini\film\LifeIsBeautiful.mp4")
        life.pack(expand=True, fill="both")

        life.play()

        layar.mainloop()

    #------------------------------------------------------------------------------------------------#
    #sinopsis dan tombol lib
    lib_poster_tempat=Frame(sinopsis1,bg="black")
    lib_poster_tempat.place(x=700,y=100,height=500,width=400)
    lib_poster= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\lib_poster_bg.jpg"))
    Label(lib_poster_tempat,image=lib_poster).place(x=0,y=0,relheight=1,relwidth=1)
    lib_judul_tempat=Frame(sinopsis1,bg="black")
    lib_judul_tempat.place(x=55,y=100,height=50,width=400)
    lib_judul=Label(lib_judul_tempat,text="Life Is Beautiful",bg="black",fg="white",font=("Times New Roman",30,"bold"))
    lib_judul.place(x=70,y=0)
    lib_sin_tempat= Frame(sinopsis1,bg="black")
    lib_sin_tempat.place(x=55,y=160,height=450,width=400)
    lib_sin1=Label(lib_sin_tempat,text="Anton may be done with life, but life ain't done with  ",bg="black",fg="white",font=("Times New Roman",14))
    lib_sin1.place(x=0,y=0)
    lib_sin2=Label(lib_sin_tempat,text="Anton. In his convincing decision to change his mea- ",bg="black",fg="white",font=("Times New Roman",14))
    lib_sin2.place(x=0,y=25)
    lib_sin3=Label(lib_sin_tempat,text="sly existence he discovers the real greatness of life.",bg="black",fg="white",font=("Times New Roman",14))
    lib_sin3.place(x=0,y=50)
    lib_tonton=Frame(lib_sin_tempat,bg="white")
    lib_tonton.place(x=150,y=90,height=40,width=100)
    tonton= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\sag_poster_mini.jpg"))
    Button(lib_tonton,image=tonton,cursor="hand2",command=film_lib).place(x=0,y=0,relheight=1,relwidth=1)

    sinopsis1.mainloop()
#------------------------------------------------------------------------------------------------#
#poster life is beautiful
poster_letak2=Frame(film1,width=130,height=150,bg="white")
poster_letak2.place(x=220,y=150)
poster_lib= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\lib_poster_mini.jpg"))
Button(poster_letak2,image=poster_lib,cursor="hand2",command=sinopsis_lib).place(x=0,y=0,relheight=1,relwidth=1)
tulispost2=Label(film1,text="Life Is Beautiful",bg="black",fg="white",font=("Times New Roman",14,"bold"))
tulispost2.place(x=215,y=300)

#------------------------------------------------------------------------------------------------#
def sinopsis_napo():
    sinopsis1 = Toplevel(film1)
    sinopsis1.geometry("1200x720")
    sinopsis1.title("Sinopsis")   

    bg = ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\zenith.jpg"))
    Label(sinopsis1, image=bg).place(x=-0,y=0,relheight=1,relwidth=1)
    #------------------------------------------------------------------------------------------------#
    #system film napo
    def film_napo():
        layar = Toplevel(sinopsis1)
        layar.geometry("1000x682")
        layar.title("NAPO")

        re = ImageTk.PhotoImage(Image.open("film.jpg"))
        Label(layar, image=re).place(x=-0,y=0,relheight=1,relwidth=1)
        kotak_log = Frame(layar,bg="black")
        kotak_log.place(x=230,y=80,height=550,width=510)

        life = TkinterVideo(master=kotak_log, scaled=True)
        life.load(r"E:\Zetapulse Code\Chill Mini\film\NAPO.mp4")
        life.pack(expand=True, fill="both")

        life.play()

        layar.mainloop()

    #------------------------------------------------------------------------------------------------#
    #sinopsis dan tombol napo
    purl_poster_tempat=Frame(sinopsis1,bg="black")
    purl_poster_tempat.place(x=700,y=100,height=500,width=400)
    purl_poster= ImageTk.PhotoImage(Image.open(r"E:\Zetapulse Code\Chill Mini\poster\reta_poster_bg.jpg"))
    Label(purl_poster_tempat,image=purl_poster).place(x=0,y=0,relheight=1,relwidth=1)
    purl_judul_tempat=Frame(sinopsis1,bg="black")
    purl_judul_tempat.place(x=55,y=100,height=50,width=400)
    purl_judul=Label(purl_judul_tempat,text="NAPO",bg="black",fg="white",font=("Times New Roman",30,"bold"))
    purl_judul.place(x=135,y=0)
    purl_sin_tempat= Frame(sinopsis1,bg="black")
    purl_sin_tempat.place(x=55,y=160,height=450,width=400)
    purl_sin1=Label(purl_sin_tempat,text="John, unable to understand the illness that drives his",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin1.place(x=0,y=0)
    purl_sin2=Label(purl_sin_tempat,text="grandfather between past and present states,stumbles",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin2.place(x=0,y=25)
    purl_sin3=Label(purl_sin_tempat,text="into an old album full of photographs. The images",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin3.place(x=0,y=50)
    purl_sin4=Label(purl_sin_tempat,text="guide his imagination, transforming his grandfather's",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin4.place(x=0,y=75)
    purl_sin5=Label(purl_sin_tempat,text="memories into drawings that shape their relationship",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin5.place(x=0,y=100)
    purl_sin6=Label(purl_sin_tempat,text="into a history of memory-building and remembrance.",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin6.place(x=0,y=125)
    purl_tonton=Frame(purl_sin_tempat,bg="white")
    purl_tonton.place(x=140,y=165,height=40,width=100)
    tonton= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\sag_poster_mini.jpg"))
    Button(purl_tonton,image=tonton,cursor="hand2",command=film_napo).place(x=0,y=0,relheight=1,relwidth=1)

    sinopsis1.mainloop()
#------------------------------------------------------------------------------------------------#
#poster napo
poster_letak3=Frame(film1,width=130,height=150,bg="white")
poster_letak3.place(x=375,y=150)
poster_reta= ImageTk.PhotoImage(Image.open(r"E:\Zetapulse Code\Chill Mini\poster\reta_poster_mini.jpg"))
Button(poster_letak3,image=poster_reta,cursor="hand2",command=sinopsis_napo).place(x=0,y=0,relheight=1,relwidth=1)
tulispost3=Label(film1,text="Napo",bg="black",fg="white",font=("Times New Roman",14,"bold"))
tulispost3.place(x=415,y=300)

#------------------------------------------------------------------------------------------------#
def sinopsis_purl():
    sinopsis1 = Toplevel(film1)
    sinopsis1.geometry("1200x720")
    sinopsis1.title("Sinopsis")   

    bg = ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\zenith.jpg"))
    Label(sinopsis1, image=bg).place(x=-0,y=0,relheight=1,relwidth=1)
    #------------------------------------------------------------------------------------------------#
    #system film purl
    def film_purl():
        layar = Toplevel(sinopsis1)
        layar.geometry("1000x682")
        layar.title("Purl")

        re = ImageTk.PhotoImage(Image.open("film.jpg"))
        Label(layar, image=re).place(x=-0,y=0,relheight=1,relwidth=1)
        kotak_log = Frame(layar,bg="black")
        kotak_log.place(x=230,y=80,height=550,width=510)

        life = TkinterVideo(master=kotak_log, scaled=True)
        life.load(r"E:\Zetapulse Code\Chill Mini\film\Purl.mp4")
        life.pack(expand=True, fill="both")

        life.play()

        layar.mainloop()

    #------------------------------------------------------------------------------------------------#
    #sinopsis dan tombol lib
    purl_poster_tempat=Frame(sinopsis1,bg="black")
    purl_poster_tempat.place(x=700,y=100,height=500,width=400)
    purl_poster= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\purl_poster_bg.jpg"))
    Label(purl_poster_tempat,image=purl_poster).place(x=0,y=0,relheight=1,relwidth=1)
    purl_judul_tempat=Frame(sinopsis1,bg="black")
    purl_judul_tempat.place(x=55,y=100,height=50,width=400)
    purl_judul=Label(purl_judul_tempat,text="Purl",bg="black",fg="white",font=("Times New Roman",30,"bold"))
    purl_judul.place(x=150,y=0)
    purl_sin_tempat= Frame(sinopsis1,bg="black")
    purl_sin_tempat.place(x=55,y=160,height=450,width=400)
    purl_sin1=Label(purl_sin_tempat,text="An earnest ball of yarn named Purl gets a job at a ",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin1.place(x=0,y=0)
    purl_sin2=Label(purl_sin_tempat,text="start-up and must decide how far is she willing to",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin2.place(x=0,y=25)
    purl_sin3=Label(purl_sin_tempat,text="go to be accepted.",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin3.place(x=0,y=50)
    purl_tonton=Frame(purl_sin_tempat,bg="white")
    purl_tonton.place(x=140,y=90,height=40,width=100)
    tonton= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\sag_poster_mini.jpg"))
    Button(purl_tonton,image=tonton,cursor="hand2",command=film_purl).place(x=0,y=0,relheight=1,relwidth=1)

    sinopsis1.mainloop()
#------------------------------------------------------------------------------------------------#
#poster purl
poster_letak4=Frame(film1,width=130,height=150,bg="white")
poster_letak4.place(x=530,y=150)
poster_purl= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\purl_poster_mini.jpg"))
Button(poster_letak4,image=poster_purl,cursor="hand2",command=sinopsis_purl).place(x=0,y=0,relheight=1,relwidth=1)
tulispost4=Label(film1,text="Purl",bg="black",fg="white",font=("Times New Roman",14,"bold"))
tulispost4.place(x=575,y=300)

#------------------------------------------------------------------------------------------------#
def sinopsis_sag():
    sinopsis1 = Toplevel(film1)
    sinopsis1.geometry("1200x720")
    sinopsis1.title("Sinopsis")   

    bg = ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\zenith.jpg"))
    Label(sinopsis1, image=bg).place(x=-0,y=0,relheight=1,relwidth=1)
    #------------------------------------------------------------------------------------------------#
    #system film paper
    def film_sag():
        layar = Toplevel(sinopsis1)
        layar.geometry("1000x682")
        layar.title("Smash And Grab")

        re = ImageTk.PhotoImage(Image.open("film.jpg"))
        Label(layar, image=re).place(x=-0,y=0,relheight=1,relwidth=1)
        kotak_log = Frame(layar,bg="black")
        kotak_log.place(x=230,y=80,height=550,width=510)

        life = TkinterVideo(master=kotak_log, scaled=True)
        life.load(r"E:\Zetapulse Code\Chill Mini\film\SmashAndGrab.mp4")
        life.pack(expand=True, fill="both")

        life.play()

        layar.mainloop()

    #------------------------------------------------------------------------------------------------#
    #sinopsis dan tombol paper
    purl_poster_tempat=Frame(sinopsis1,bg="black")
    purl_poster_tempat.place(x=700,y=100,height=500,width=400)
    purl_poster= ImageTk.PhotoImage(Image.open(r"E:\Zetapulse Code\Chill Mini\poster\sag_poster_bg.jpg"))
    Label(purl_poster_tempat,image=purl_poster).place(x=0,y=0,relheight=1,relwidth=1)
    purl_judul_tempat=Frame(sinopsis1,bg="black")
    purl_judul_tempat.place(x=55,y=100,height=50,width=400)
    purl_judul=Label(purl_judul_tempat,text="Smash And Grab",bg="black",fg="white",font=("Times New Roman",30,"bold"))
    purl_judul.place(x=50,y=0)
    purl_sin_tempat= Frame(sinopsis1,bg="black")
    purl_sin_tempat.place(x=55,y=160,height=450,width=400)
    purl_sin1=Label(purl_sin_tempat,text="After years of toiling away inside the engine room ",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin1.place(x=0,y=0)
    purl_sin2=Label(purl_sin_tempat,text="of a towering locomotive, two antiquated robots will",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin2.place(x=0,y=25)
    purl_sin3=Label(purl_sin_tempat,text="risk everything for freedom and for each other.",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin3.place(x=0,y=50)
    purl_tonton=Frame(purl_sin_tempat,bg="white")
    purl_tonton.place(x=140,y=90,height=40,width=100)
    tonton= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\sag_poster_mini.jpg"))
    Button(purl_tonton,image=tonton,cursor="hand2",command=film_sag).place(x=0,y=0,relheight=1,relwidth=1)

    sinopsis1.mainloop()
#------------------------------------------------------------------------------------------------#
#poster smash and grab
poster_letak5=Frame(film1,width=130,height=150,bg="white")
poster_letak5.place(x=685,y=150)
poster_sag= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\sag_poster_mini.jpg"))
Button(poster_letak5,image=poster_sag,cursor="hand2",command=sinopsis_sag).place(x=0,y=0,relheight=1,relwidth=1)
tulispost5=Label(film1,text="Smash And Grab",bg="black",fg="white",font=("Times New Roman",14,"bold"))
tulispost5.place(x=677,y=300)

#------------------------------------------------------------------------------------------------#
def sinopsis_paper():
    sinopsis1 = Toplevel(film1)
    sinopsis1.geometry("1200x720")
    sinopsis1.title("Sinopsis")   

    bg = ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\zenith.jpg"))
    Label(sinopsis1, image=bg).place(x=-0,y=0,relheight=1,relwidth=1)
    #------------------------------------------------------------------------------------------------#
    #system film paper
    def film_paper():
        layar = Toplevel(sinopsis1)
        layar.geometry("1000x682")
        layar.title("Paperman")

        re = ImageTk.PhotoImage(Image.open("film.jpg"))
        Label(layar, image=re).place(x=-0,y=0,relheight=1,relwidth=1)
        kotak_log = Frame(layar,bg="black")
        kotak_log.place(x=230,y=80,height=550,width=510)

        life = TkinterVideo(master=kotak_log, scaled=True)
        life.load(r"E:\Zetapulse Code\Chill Mini\film\paperman.mp4")
        life.pack(expand=True, fill="both")

        life.play()

        layar.mainloop()

    #------------------------------------------------------------------------------------------------#
    #sinopsis dan tombol paper
    purl_poster_tempat=Frame(sinopsis1,bg="black")
    purl_poster_tempat.place(x=700,y=100,height=500,width=400)
    purl_poster= ImageTk.PhotoImage(Image.open(r"E:\Zetapulse Code\Chill Mini\poster\paperman_poster_bg.jpg"))
    Label(purl_poster_tempat,image=purl_poster).place(x=0,y=0,relheight=1,relwidth=1)
    purl_judul_tempat=Frame(sinopsis1,bg="black")
    purl_judul_tempat.place(x=55,y=100,height=50,width=400)
    purl_judul=Label(purl_judul_tempat,text="Paperman",bg="black",fg="white",font=("Times New Roman",30,"bold"))
    purl_judul.place(x=100,y=0)
    purl_sin_tempat= Frame(sinopsis1,bg="black")
    purl_sin_tempat.place(x=55,y=160,height=450,width=400)
    purl_sin1=Label(purl_sin_tempat,text="An office worker meets the girl of his dreams and uses ",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin1.place(x=0,y=0)
    purl_sin2=Label(purl_sin_tempat,text="a fleet of paper airplanes to get her attention.",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin2.place(x=0,y=25)
    purl_tonton=Frame(purl_sin_tempat,bg="white")
    purl_tonton.place(x=140,y=65,height=40,width=100)
    tonton= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\sag_poster_mini.jpg"))
    Button(purl_tonton,image=tonton,cursor="hand2",command=film_paper).place(x=0,y=0,relheight=1,relwidth=1)

    sinopsis1.mainloop()
#------------------------------------------------------------------------------------------------#
#poster paperman
poster_letak6=Frame(film1,width=130,height=150,bg="white")
poster_letak6.place(x=840,y=150)
poster_paperman= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\paperman_poster_mini.jpg"))
Button(poster_letak6,image=poster_paperman,cursor="hand2",command=sinopsis_paper).place(x=0,y=0,relheight=1,relwidth=1)
tulispost6=Label(film1,text="Paperman",bg="black",fg="white",font=("Times New Roman",14,"bold"))
tulispost6.place(x=860,y=300)

#------------------------------------------------------------------------------------------------#
#tulisan dan acesories drama indonesia
tulis2=Label(film1,text="Drama Indonesia:",bg="red",fg="white",font=("Times New Roman",24,"bold"))
tulis2.place(x=80,y=350)

#------------------------------------------------------------------------------------------------#
def sinopsis_darigea():
    sinopsis1 = Toplevel(film1)
    sinopsis1.geometry("1200x720")
    sinopsis1.title("Sinopsis")   

    bg = ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\zenith.jpg"))
    Label(sinopsis1, image=bg).place(x=-0,y=0,relheight=1,relwidth=1)
    #------------------------------------------------------------------------------------------------#
    #system film darigea
    def film_ibu():
        layar = Toplevel(sinopsis1)
        layar.geometry("1000x682")
        layar.title("Dari Gea Untuk Ayah")

        re = ImageTk.PhotoImage(Image.open("film.jpg"))
        Label(layar, image=re).place(x=-0,y=0,relheight=1,relwidth=1)
        kotak_log = Frame(layar,bg="black")
        kotak_log.place(x=230,y=80,height=550,width=510)

        life = TkinterVideo(master=kotak_log, scaled=True)
        life.load(r"E:\Zetapulse Code\Chill Mini\film\DariGea.mp4")
        life.pack(expand=True, fill="both")

        life.play()

        layar.mainloop()

    #------------------------------------------------------------------------------------------------#
    #sinopsis dan tombol darigea
    purl_poster_tempat=Frame(sinopsis1,bg="black")
    purl_poster_tempat.place(x=700,y=100,height=500,width=400)
    purl_poster= ImageTk.PhotoImage(Image.open(r"E:\Zetapulse Code\Chill Mini\poster\DariGea_poster_bg.jpg"))
    Label(purl_poster_tempat,image=purl_poster).place(x=0,y=0,relheight=1,relwidth=1)
    purl_judul_tempat=Frame(sinopsis1,bg="black")
    purl_judul_tempat.place(x=55,y=100,height=50,width=400)
    purl_judul=Label(purl_judul_tempat,text="Dari Gea Untuk Ayah",bg="black",fg="white",font=("Times New Roman",30,"bold"))
    purl_judul.place(x=10,y=0)
    purl_sin_tempat= Frame(sinopsis1,bg="black")
    purl_sin_tempat.place(x=55,y=160,height=450,width=400)
    purl_sin1=Label(purl_sin_tempat,text="Ayah memang tidak melahirkanmu.",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin1.place(x=0,y=0)
    purl_sin2=Label(purl_sin_tempat,text="Tapi ayah adalah sosok yang berjasa membesarkanmu",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin2.place(x=0,y=25)
    purl_sin3=Label(purl_sin_tempat,text="Merawatmu, memeliharamu,mendidikmu bercucuran",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin3.place(x=0,y=50)
    purl_sin4=Label(purl_sin_tempat,text="keringat dari pagi ketemu pagi.",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin4.place(x=0,y=75)
    purl_sin5=Label(purl_sin_tempat,text="Dari anak dan istri. Terimakasih ayah..",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin5.place(x=0,y=100)
    purl_tonton=Frame(purl_sin_tempat,bg="white")
    purl_tonton.place(x=140,y=140,height=40,width=100)
    tonton= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\sag_poster_mini.jpg"))
    Button(purl_tonton,image=tonton,cursor="hand2",command=film_ibu).place(x=0,y=0,relheight=1,relwidth=1)

    sinopsis1.mainloop()
#------------------------------------------------------------------------------------------------#
#poster Dari Gea
poster_letaka=Frame(film1,width=130,height=150,bg="white")
poster_letaka.place(x=65,y=400)
poster_gea= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\DariGea_poster_mini.jpg"))
Button(poster_letaka,image=poster_gea,cursor="hand2",command=sinopsis_darigea).place(x=0,y=0,relheight=1,relwidth=1)
tulisposta=Label(film1,text="Dari Gea",bg="black",fg="white",font=("Times New Roman",14,"bold"))
tulisposta.place(x=90,y=550)

#------------------------------------------------------------------------------------------------#
def sinopsis_ibu():
    sinopsis1 = Toplevel(film1)
    sinopsis1.geometry("1200x720")
    sinopsis1.title("Sinopsis")   

    bg = ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\zenith.jpg"))
    Label(sinopsis1, image=bg).place(x=-0,y=0,relheight=1,relwidth=1)
    #------------------------------------------------------------------------------------------------#
    #system film ibu
    def film_ibu():
        layar = Toplevel(sinopsis1)
        layar.geometry("1000x682")
        layar.title("Ibu")

        re = ImageTk.PhotoImage(Image.open("film.jpg"))
        Label(layar, image=re).place(x=-0,y=0,relheight=1,relwidth=1)
        kotak_log = Frame(layar,bg="black")
        kotak_log.place(x=230,y=80,height=550,width=510)

        life = TkinterVideo(master=kotak_log, scaled=True)
        life.load(r"E:\Zetapulse Code\Chill Mini\film\ibu.mp4")
        life.pack(expand=True, fill="both")

        life.play()

        layar.mainloop()

    #------------------------------------------------------------------------------------------------#
    #sinopsis dan tombol ibu
    purl_poster_tempat=Frame(sinopsis1,bg="black")
    purl_poster_tempat.place(x=700,y=100,height=500,width=400)
    purl_poster= ImageTk.PhotoImage(Image.open(r"E:\Zetapulse Code\Chill Mini\poster\ibu_poster_bg.jpg"))
    Label(purl_poster_tempat,image=purl_poster).place(x=0,y=0,relheight=1,relwidth=1)
    purl_judul_tempat=Frame(sinopsis1,bg="black")
    purl_judul_tempat.place(x=55,y=100,height=50,width=400)
    purl_judul=Label(purl_judul_tempat,text="Ibu",bg="black",fg="white",font=("Times New Roman",30,"bold"))
    purl_judul.place(x=160,y=0)
    purl_sin_tempat= Frame(sinopsis1,bg="black")
    purl_sin_tempat.place(x=55,y=160,height=450,width=400)
    purl_sin1=Label(purl_sin_tempat,text="Seorang Ibu bisa merawat 10 anaknya,",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin1.place(x=0,y=0)
    purl_sin2=Label(purl_sin_tempat,text="Tapi 10 anak belum tentu bisa merawar seorang ibu...",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin2.place(x=0,y=25)
    purl_sin3=Label(purl_sin_tempat,text="Sayangilah ibu kita selagi masih ada dihadapan kita...",bg="black",fg="white",font=("Times New Roman",14))
    purl_sin3.place(x=0,y=50)
    purl_tonton=Frame(purl_sin_tempat,bg="white")
    purl_tonton.place(x=140,y=90,height=40,width=100)
    tonton= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\sag_poster_mini.jpg"))
    Button(purl_tonton,image=tonton,cursor="hand2",command=film_ibu).place(x=0,y=0,relheight=1,relwidth=1)

    sinopsis1.mainloop()
#------------------------------------------------------------------------------------------------#
#poster Ibu
poster_letakb=Frame(film1,width=130,height=150,bg="white")
poster_letakb.place(x=220,y=400)
poster_ibu= ImageTk.PhotoImage(Image.open("E:\Zetapulse Code\Chill Mini\poster\ibu_poster_mini.jpg"))
Button(poster_letakb,image=poster_ibu,cursor="hand2",command=sinopsis_ibu).place(x=0,y=0,relheight=1,relwidth=1)
tulispostb=Label(film1,text="Ibu",bg="black",fg="white",font=("Times New Roman",14,"bold"))
tulispostb.place(x=260,y=550)

film1.mainloop()
