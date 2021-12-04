from player import Player 
import os
import csv
from tkinter import *
#function take entry and make sure it's not empty to use with almost all entry in the program
#return 1 if the entry not empty and zero if empty
def not_empty_entry(entry):
    if(entry.get().strip()):
        return 1
    else:
        return 0

class Club:
    def __init__(self,name,no_matches=0,points=0,wins=0,draws=0,loses=0,position=0,squad=[],GF=0,GA=0,GD=0):
        self.__name=name
        self.__no_matches=no_matches
        self.__points=points
        self.__wins=wins
        self.__draws=draws
        self.__loses=loses
        self.__position=position
        self.__squad=squad
        self.__GF=GF
        self.__GA=GA
        self.__GD=GD
        self.create_folder()
    
    #method to set club name
    def set_name(self,name):
        self.__name=name
    #win add 3 points and increase wins number by 1
    def win(self):
        self.__points+=3
        self.__wins+=1
    #draw team take one point and drwas increase by 1
    def draw(self):
        self.__points+=1
        self.__draws+=1
    #lose team take no points so just increase number of loses matches    
    def lose(self):
        self.__loses+=1
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
    #return club position on the score board
    def get_position(self):
        return self.__position
    #reutn squad players (data about them)
    def get_squad(self):
        return self.__squad
    #return gf
    def get_GF(self):
        return self.__GF
    #return ga
    def get_GA(self):
        return self.__GA
    #return gd
    def get_GD(self):
        return self.__GD
    #add player to the squad
    def add_player(self,obj):
        self.__squad.append(obj)
    #to create folder for each club and if club exist it will make nothing
    def create_folder(self):
        try:
            os.mkdir(f'{os.getcwd()}/{self.__name}')
            return True
        except :
            del self
            # print("Club already exist")\
            
  
    #save squad in file
    def club_squad_file(self):
        #save the file in club folder
        with open(f'{os.getcwd()}/{self.__name}/{self.__name}.csv','a',newline='') as csvfile:
            writer = csv.writer(csvfile,delimiter=',',quotechar='|')
            #get squad will return list so we can go through it
            for player in self.get_squad():
                writer.writerow([player.get_name(),player.get_age(),player.get_position(),player.get_no_goals(),player.get_yel_card(),player.get_red_card()])

    #
    @staticmethod
    def store_club(clubs,newclub,master):
        clubs.append(newclub)
        newclub.club_squad_file()
        master.destroy()    

    #function used for create club button
    #main idea to check if the name not empty and create the club object
    #button suppose to take create club button to disabled it or remove it 
    @staticmethod
    def create_club_command(master,name_entry,clubs,button):
        #means if the name entry is empty show that name can't be empty
        if not not_empty_entry(name_entry):
            notfi=Label(master,text="club name cannot be empty",fg="red")
        else:
            notfi=Label(master,text="                                                                                               ",fg="red")
            button.grid_forget()
            name_entry.config(state=DISABLED)
            newclub=Club(name=name_entry.get().strip())#new club object
            #to keep track how many players did we store and if 5 show save club
            player_num=[1]
            #this button will be hidden until 5 players are stored
            save_club=Button(master,text="save club",command=lambda:Club.store_club(clubs,newclub,master))
            Player.add_player(newclub,master,player_num,save_club)#to show add player widgets and add the data in newplayer object
            #hide the club save button when 5 players are saved this button will be avaliable
            save_club.grid_forget()
        #to show failed or created in same place
        notfi.grid(row=9,column=1,padx=10,pady=10)

    """function to create add club page gui 
    and take club squad within it for new club 5 players
    to add new club you need just enter his name ,and 5 players name , age and position (5 players data will be taken witn function from player module)
    """
    @staticmethod
    def add_club(clubs):
        master=Tk()#window object
        master.title("add new club")
        master.geometry("450x400")
        master.resizable(False,False)
        #add widgets to set the window
        club_name_label=Label(master,text="club name")
        club_name=Entry(master)
        #button to take the name and create folder with that name (club folder)
        create_club=Button(master,text="create club",command=lambda:Club.create_club_command(master,club_name,clubs,create_club))
        #edit widgets with grid
        club_name_label.grid(row=1,column=0,padx=10,pady=10)
        club_name.grid(row=1, column=1,padx=10,pady=10)
        create_club.grid(row=1,column=2,padx=10,pady=10)
        master.mainloop()

