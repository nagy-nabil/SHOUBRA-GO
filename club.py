from player import Player 
import os
import csv
from tkinter import *
from random import randrange
from tkinter import messagebox
from tkinter.ttk import *
import webbrowser #module used to open about me link
from PIL import Image, ImageTk
#function used to add the logo in any window in pack() , take window to add in and size of the logo
def show_logo(master,x,y):
    # Create a photoimage object of the image in the path
    try:
        image1 = Image.open("Shoubra_GO-logos_black.png")
    except:
        pass
    else:
        image1 = image1.resize((x, y), Image.ANTIALIAS)
        logo = ImageTk.PhotoImage(image1)
        label1 = Label(master,image=logo)
        label1.image=logo
        # label1.image = test
        #PhotoImage()
        label1.pack()

#to make menu with file and about only for main page and add club page
def main_menu(master):
    #menus gui
    menubar=Menu(master)
    #file menu to exit in any time
    filemenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="file",menu=filemenu)
    filemenu.add_command(label="add club",command=lambda:Club.add_club(master))
    filemenu.add_command(label="delete club",command=lambda:Club.delete_club_gui(master))
    filemenu.add_command(label="standing",state=DISABLED)
    filemenu.add_command(label="end league",state=DISABLED)
    filemenu.add_separator()
    #to close master window in any time
    filemenu.add_command(label="exit",command=master.destroy)
    #about menu gui to go to github page
    aboutmenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="About",menu=aboutmenu)
    aboutmenu.add_command(label="about me",command=open_link)
    #to set menubar as menu for master
    master.config(menu=menubar)


#function to open link from about me command 
def open_link():
    url="https://github.com/nagy-nabil/SHOUBRA-GO"
    webbrowser.open(url)

#function take entry and make sure it's not empty to use with almost all entry in the program
#return 1 if the entry not empty and zero if empty
def not_empty_entry(entry):
    if(entry.get().strip()):
        return 1
    else:
        return 0


class Club:
    no_clubs = 0
    def __init__(self,name,no_matches=0,wins=0,draws=0,loses=0,GF=0,GA=0,GD=0,points=0,squad=[]):
        self.__name=name
        self.__no_matches=no_matches
        self.__points=points
        self.__wins=wins
        self.__draws=draws
        self.__loses=loses
        self.__squad=squad
        self.__GF=GF
        self.__GA=GA
        self.__GD=GD
        self.create_folder()
        Club.no_clubs += 1 
    

    #win add 3 points and increase wins number by 1
    def win(self):
        self.__points+=3
        self.__wins+=1
        self.__no_matches+=1
    #draw team take one point and drwas increase by 1
    def draw(self):
        self.__points+=1
        self.__draws+=1
        self.__no_matches+=1
    #lose team take no points so just increase number of loses matches    
    def lose(self):
        self.__loses+=1
        self.__no_matches+=1
    #increase matchs played after each round
    def match_played(self):
        self.__no_matches+=1
    #to  edit gf ga gd take the match result
    def goals(self,GF,GA):
        self.__GF+=GF
        self.__GA+=GA
        self.__GD=self.__GF-self.__GA
    #return club name
    def get_name(self):
        return self.__name
    #return number of matches played
    def get_no_matches(self):
        return self.__no_matches
    #return club points
    def get_points(self):
        return self.__points
    def get_wins(self):
        return self.__wins
    #reutn squad players (data about them)
    def get_loses(self):
        return self.__loses
    def get_draws(self):
        return self.__draws
    def get_squad(self):
        return self.__squad
    #get randomly single player
    def player_score(self,g):
        n=randrange(0,len(self.__squad))
        self.__squad[n].scored(g)
        return self.__squad[n].get_name()
    def add_cards(self):
        n=randrange(0,len(self.__squad))
        self.__squad[n].yel_card()
        flag=randrange(0,3)
        #flag is random number from 0:3 if flag =1 , 
        #one player will have red card else no one will take red card
        if flag==1:
            self.__squad[n].red_card()
        m=randrange(0,len(self.__squad))
        self.__squad[n].yel_card()
        return  [self.__squad[n].get_name(), self.__squad[m].get_name() , flag]


    #return gf
    def get_GF(self):
        return self.__GF
    #return ga
    def get_GA(self):
        return self.__GA
    #return gd
    def get_GD(self):
        return self.__GD
    def get_points(self):
        return self.__points

    #add player to the squad
    def add_player(self,obj):
        self.__squad.append(obj)
    #function to create folder for the club once we create it and if the folder already exist gives error
    def create_folder(self):
        try:
            os.mkdir(f'{os.getcwd()}/{self.__name.title()}')
            return True
        except :
            del self
    #Print the club
    def __str__(self):
        return f"name {self.__name}"
    #Print the club
    def __repr__(self):
        return f"name {self.__name}"
    #save squad in file
    def club_squad_file(self):
        #save the file in club folder
        file=self.__name.title()
        with open(f'{os.getcwd()}/{self.__name}/{file}.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile,delimiter=',',quotechar='|')
            writer.writerow(["NAME",'AGE','POSITION','GOALS','Y CARDS','R CARDS'])
            #get squad will return list so we can go through it
            for player in self.get_squad():
                writer.writerow([player.get_name(),player.get_age(),player.get_position(),player.get_no_goals(),player.get_yel_card(),player.get_red_card()])

    #function used to add club name to file contain all clubs name
    def add_to_all(self):
        with open(f'{os.getcwd()}/allclubs.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile,delimiter=',',quotechar='|')
            writer.writerow([self.get_name().title()])
        with open(f'{os.getcwd()}/available.csv','a',newline='') as csvfile2:
            writer2 = csv.writer(csvfile2,delimiter=',',quotechar='|')
            writer2.writerow([self.get_name().title()])

    #used to store club name in allclubs file (database refrence) and store club squad file
    @staticmethod
    def store_club(newclub,master):
        newclub.add_to_all()
        newclub.club_squad_file()
        messagebox.showinfo("SAVED", "Club saved successfully")
        master.destroy()


    #function used for create club button
    #main idea to check if the name not empty and create the club object
    #button suppose to take create club button to disabled it or remove it 
    @staticmethod
    def check_available_club(name):
        try:
            with open(f'{os.getcwd()}/allclubs.csv','r',newline='') as csvfile:
                reader = csv.reader(csvfile,delimiter=',',quotechar='|')
                for line in reader:
                    if name in line:
                        return False
            return True
        except : #if the file doesn't exist means no clubs so all names are avaliable
            return True
    @staticmethod
    def create_club_command(master,frame,name_entry,button):
        #means if the name entry is empty show that name can't be empty
        if not not_empty_entry(name_entry):
            
            messagebox.showerror("EMPTY","club name cannot be empty")
        else:
            if Club.check_available_club(name_entry.get().strip().title())==False:
                messagebox.showerror("EXIST","Club already exist")
            else:
                button.grid_forget()
                name_entry.config(state=DISABLED)
                newclub=Club(name=name_entry.get().strip().title(),squad=[])#new club object
                #to keep track how many players did we store and if 5 show save club
                player_num=[1]
                #this button will be hidden until 5 players are stored
                save_club=Button(frame,text="save club",command=lambda:Club.store_club(newclub,master))
                Player.get_player_data(newclub,frame,player_num,save_club)#to show add player widgets and add the data in newplayer object
                #hide the club save button when 5 players are saved this button will be avaliable
                save_club.grid_forget()


    """function to create add club page gui 
    and take club squad within it for new club 5 players
    to add new club you need just enter his name ,and 5 players name , age and position (5 players data will be taken witn function from player module)
    window to be destroyed to keep just one window 
    """
    @staticmethod
    def add_club(window):
        window.destroy()#to destroy the previous window
        master=Tk()#window object
        master.iconbitmap('4876628.ico')
        master.title("add new club")
        show_logo(master,250,250)
        master.geometry("550x550+300+200")
        master.resizable(False,False)
        main_menu(master)
        add_frame=Frame(master)
        #add widgets to set the window
        club_name_label=Label(add_frame,text="club name")
        club_name=Entry(add_frame)
        #button to take the name and create folder with that name (club folder)
        create_club=Button(add_frame,text="create club",command=lambda:Club.create_club_command(master,add_frame,club_name,create_club))
        #edit widgets with grid
        club_name_label.grid(row=1,column=0,padx=10,pady=10)
        club_name.grid(row=1, column=1,padx=10,pady=10)
        create_club.grid(row=1,column=2,padx=10,pady=10)
        add_frame.pack()
        master.mainloop()

    #window to add delete club frame in it 
    """
    works as that load the allclubs file and see if the club the user want to delete in it or not if exist will give him question yes no to be sure he want to delete this club becsue it will destroy the current working league 
    """
    @staticmethod
    def delete_club_gui(window):
        delete_frame=Frame(window)
        club_name_label=Label(delete_frame,text="club name")
        club_name_entry=Entry(delete_frame)
        club_name_button=Button(delete_frame,text="DELETE",command=lambda:Club.delete_club(delete_frame,club_name_entry))
        club_name_label.grid(row=0,column=0,padx=10,pady=10)
        club_name_entry.grid(row=0,column=1,padx=10,pady=10)
        club_name_button.grid(row=0,column=2,padx=10,pady=10)
        delete_frame.grid(row=1000)
    """take the frame to delete it after it no longer neaded and entry to take the data from it""" 
    @staticmethod
    def delete_club(frame,entry):
        name=entry.get().strip().title()
        clubs=[]#empty list to store all clubs name in it
        try:
            #try read the data 
            with open(f'{os.getcwd()}/allclubs.csv','r',newline='') as csvfile:
                reader = csv.reader(csvfile,delimiter=',',quotechar='|')
                for club in reader:
                    clubs.append(club[0])
                #close the file
            if name in clubs:#if you find the club do the operations
                sure=messagebox.askyesno("SURE","are you sure you want to delete the club?")
                if sure==1:
                    clubs.remove(name)
                    os.remove(f'{os.getcwd()}/{name}/{name}.csv')
                    os.rmdir(f'{os.getcwd()}/{name}')
                    #to rewrite the all clubs file without that club name
                    with open(f'{os.getcwd()}/allclubs.csv','w',newline='') as csvfile:
                        writer = csv.writer(csvfile,delimiter=',',quotechar='|')
                        for club in clubs:
                            writer.writerow([club])
                    #close the file
                    messagebox.showinfo("DELETED","club has been successfully deleted from your database")
                    frame.grid_forget()#to delete the delete club frame 
                else:#no longer need to delete club
                    messagebox.showinfo("no club","no clubs have been deleted")
                    frame.grid_forget()#to delete the delete club frame 
            else:#didn't find the club name
                messagebox.showinfo("no club","no club with that name")
                frame.grid_forget()#to delete the delete club frame 
        except : #if the file doesn't exist means no clubs to delete
            messagebox.showinfo("no club","no club with that name")
            frame.grid_forget()#to delete the delete club frame           