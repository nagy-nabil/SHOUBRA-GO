from startleague import  continue_league_gui ,start_league_gui
from club import Club,main_menu
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk


def main():
    master=Tk()#the only window we have
    master.geometry("250x500+500+200")
    master.title("main")
    # Create a photoimage object of the image in the path
    image1 = Image.open("Shoubra GO-logos_black.png")
    image1 = image1.resize((250, 250), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    main_menu(master)
    PhotoImage()
    main_frame=Frame(master)
    #add widgets
    add_club=Button(main_frame,text="add club",command=lambda:add_to_main(master))
    start=Button(main_frame,text="start league",command=lambda:start_to_main(master))
    continue_league_button=Button(main_frame,text="continue league",command=lambda:continue_to_main(master))
    exit=Button(main_frame,text="EXIT",command=master.destroy)
    #widgets setup with grid
    add_club.pack(padx=10,pady=10)
    start.pack(padx=10,pady=10)
    continue_league_button.pack(padx=10,pady=10)
    exit.pack(padx=10,pady=10)
    label1.grid(row=0,column=0)
    main_frame.grid(row=1,column=0)
    master.mainloop()

#to go to main again after storing club
def add_to_main(master):
    Club.add_club(master)
    main()
#to go to main again after league page
def start_to_main(master):
    start_league_gui(master)
    main()

def continue_to_main(master):
    continue_league_gui(master)
    main()

main()
