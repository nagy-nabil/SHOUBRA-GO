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