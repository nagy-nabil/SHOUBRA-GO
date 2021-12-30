from startleague import  continue_league_gui ,start_league_gui
from club import Club,main_menu, show_logo
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

#function to know it's the first time for the program or no

def main():
    master=Tk()#the only window we have
    master.iconbitmap('4876628.ico')
    master.geometry("550x550+300+200") 
    master.resizable(False,False)
    master.title("Shoubra Go")
    main_menu(master)
    #add the logo in row =0 col =0
    show_logo(master,250,250)
    main_frame=Frame(master)
    #add widgets
    add_club=Button(main_frame,text="add club",command=lambda:add_to_main(master),width=20)
    start=Button(main_frame,text="start league",command=lambda:start_to_main(master),width=20)
    continue_league_button=Button(main_frame,text="continue league",command=lambda:continue_to_main(master),width=20)
    exit=Button(main_frame,text="EXIT",command=master.destroy,width=20)
    #widgets setup with grid
    add_club.pack(padx=10,pady=10)
    start.pack(padx=10,pady=10)
    continue_league_button.pack(padx=10,pady=10)
    exit.pack(padx=10,pady=10)
    main_frame.pack()
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