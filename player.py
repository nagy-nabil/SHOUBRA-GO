from tkinter import *
from club import *
import os
import csv
from tkinter import messagebox
from tkinter.ttk import *

#function take entry and make sure it's not empty to use with almost all entry in the program
#return 1 if the entry not empty and zero if empty
def not_empty_entry(entry):
    if(entry.get().strip()):
        return 1
    else:
        return 0
current_poses=[]
class Player:
    def __init__(self,name,age,position,no_goals=0,yel_card=0,red_card=0):
        self.__name=name
        self.__age=age
        self.__position=position
        self.__no_goals=no_goals
        self.__yel_card=yel_card
        self.__red_card=red_card

    #method to return player object
    @classmethod
    def create_player(self,name,age,position):
        return Player(name,age,position)
    
    def set_age(self,age):
        self.__age=age
    def set_position(self,position):
        self.__position=position
    #add goals
    def scored(self,no_goals):
        self.__no_goals+=no_goals
    #add yellow card
    def yel_card(self):
        self.__yel_card+=1
    #add red card
    def red_card(self):
        self.__red_card+=1
    #return player name
    def get_name(self):
        return self.__name
    #return player age
    def get_age(self):
        return self.__age
    #return player position
    def get_position(self):
        return self.__position
    #return player number of goals
    def get_no_goals(self):
        return self.__no_goals
    #return player number of cards
    def get_yel_card(self):
        return self.__yel_card
    #return player number of red cards
    def get_red_card(self):
        return self.__red_card
    

    
    # use to print all object data
    def __str__(self):
        return f"player name: {self.__name}\n{self.__name} : {self.__age}\n{self.__name} position : {self.__position}\n{self.__name} number of goals: {self.__no_goals}\n{self.__name} number of yellow cards : {self.__yel_card}\n{self.__name} number of red cards: {self.__red_card}\n"

    #will be used as button command to get entry and clear the entry for next player  take variable o store in it the new player object 
    # save player button to control it and hide when user add 5 players
    #save_club_button to give number of players control on show sace club 
    #name e1 age e2 position e3
    positions=['GK','LB','CB','RB','LMF','DMF','CMF','AMF','RMF','LW','CF','SS','RW']
    @staticmethod
    def store_player(master,newclub,e1,e2,e3,player_num,save_player_button,save_club_button):
        #name age position
        #give error if the name entry is empty
        if not not_empty_entry(e1): 
            messagebox.showerror("EMPTY","Player name cannot be empty")
        #give error if the age entry is empty
        elif not not_empty_entry(e2):
            messagebox.showerror("EMPTY","PLayer age cannot be empty")
        
        #give error if the position entry is empty
        elif not not_empty_entry(e3):
            #notfi=Label(master,text="player position cannot be empty",fg="red")
            messagebox.showerror("EMPTY","Position age cannot be empty")

        #save data if no entry is empty but first check age is not string
        elif e1.get().strip().isdigit()==True:
            #notfi=Label(master,text="Enter Vaild name",fg="red")
            messagebox.showerror("VALIDATION","Enter Vaild name")
        elif e3.get().strip().upper() not in Player.positions:
            # notfi=Label(master,text="Enter Vaild position",fg="red")
            messagebox.showerror("VALIDATION",f"positions must be\n {Player.positions}")
            #messagebox.showerror(text=f"hint: positions must be {positions} ")
            #poses=Label(master,text=f"hint: positions must be {positions} ")
            
            #poses.grid(row=10,column=1,padx=10,pady=10)
        #if the player data passed all validation
        else:
            try:
                #try to cast age into int if no error go to else block if not show error from except
                int(e2.get().strip())
            except:
                #show error if the age cannot be int (age is string)
                #notfi=Label(master,text="\tEnter vaild age\t",fg="red")
                messagebox.showerror("VALIDATION","Enter Vaild Age")
            else: #the code to perform if age can be integer
                case=True
                if int(e2.get())<16 or int(e2.get())>40:
                    #notfi=Label(master,text="\tEnter vaild age\t",fg="red")
                    messagebox.showerror("VALIDATION","Must be older than 16 and younger than 40 ")
                else: #to check if there's a player with exactly the same data in players database
                    try:
                        with open(f"{os.getcwd()}\\allplayers.csv", 'r') as playersfile:
                        
                            lines=csv.reader(playersfile,delimiter=',',quotechar='|')
                            for line in lines:
                                if e1.get().strip().upper()==line[0] and e2.get().strip()==line[1] and e3.get().strip()==line[2] :
                                    messagebox.showerror("Existance","Player already exist")
                                    case=False
                    except:
                        case==True
                    #if the player doesn't exist save him
                    if case==True:
                        if e3.get().strip().upper() not in Player.positions:
                            messagebox.showerror("Existance",f"Position already taken\nhint: positions left {Player.positions}")
                        else:
                            with open(f"{os.getcwd()}\\allplayers.csv", 'a',newline='') as playersfile:
                                writer=csv.writer(playersfile,delimiter=',',quotechar='|')
                                writer.writerow([e1.get().strip().upper(),e2.get().strip(),e3.get().strip().upper()])
                            # notfi=Label(master,text="                                                                                                                     ",fg="red")
                            #create new player object
                            newplayer=Player(e1.get().strip().upper(),e2.get().strip(),e3.get().strip().upper())

                            Player.positions.remove(f'{e3.get().strip().upper()}')
                            #messagebox.showinfo("SAVED", "Player saved successfully")
                            newclub.add_player(newplayer)#to append this player in new club
                            #to delete data from entry prepare them for next time
                            e1.delete(0,END)
                            e2.delete(0,END)
                            e3.delete(0,END)
                            player_num[0]+=1 #to keep track how many player
                            if player_num[0]>5: # to remove save widget to prevent him adding more players
                                Player.positions=['GK','LB','CB','RB','LMF','DMF','CMF','AMF','RMF','LW','CF','SS','RW']
                                save_player_button.grid_remove()
                                save_club_button.grid(row=8,column=1,padx=10,pady=10)
                        
        #notfi.grid(row=9,column=1,padx=10,pady=10)
        

    """"to add new player supposed to be used in add club , with gui ,take window name and command which is take the input from entry and store in the club then delete the entry data to make him store another one
    and player number to know how many player did i store and prevent him from storing more than 5 players"""
    @staticmethod
    def get_player_data(newclub,master,player_num,save_club_button):
        #add widgets
        player_num_label=Label(master,text=f"please enter players data")
        player_name_label=Label(master,text=f"player name")
        player_age_label=Label(master,text=f"player age")
        player_position_label=Label(master,text=f"player  position")
        player_name=Entry(master)
        player_age=Entry(master)
        player_position=Entry(master)
        #to take data from entry and save them
        save=Button(master,text="add player data",command=lambda:Player.store_player(master,newclub,player_name,player_age,player_position,player_num,save,save_club_button)) # take entry and save them in club squa
        #edit widgets place with grid
        player_num_label.grid(row=3,column=0,padx=10,pady=10)
        player_name_label.grid(row =4,column=0,padx=10,pady=10)
        player_age_label.grid(row =5,column=0,padx=10,pady=10)
        player_position_label.grid(row =6,column=0,padx=10,pady=10)
        player_name.grid(row =4,column=1,padx=10,pady=10)
        player_age.grid(row =5,column=1,padx=10,pady=10)
        player_position.grid(row =6,column=1,padx=10,pady=10)
        save.grid(row=7,column=0,padx=10,pady=10)