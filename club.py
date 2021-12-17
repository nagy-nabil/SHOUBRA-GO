from player import Player 
import os
import csv
from tkinter import *
from random import randrange
from tkinter import messagebox
from tkinter.ttk import *

import webbrowser #module used to open about me link


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
