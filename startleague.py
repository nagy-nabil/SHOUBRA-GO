from typing import MutableMapping
from club import Club
from player import Player
from club import not_empty_entry
from tkinter import *
from random import shuffle
from tkinter import messagebox
import csv
import os
from tkinter.ttk import *
from club import open_link
#list of clubs names
clubs=[]
clubs_no=0
#list contain matches sechudle
table=[]
#the key will be club name the vslue is club object
clubs_objs={}

#load all league  contents
def load_league(name):
    global clubs_no
    global table
    global clubs_objs
    global clubs
    with open(f'{os.getcwd()}/{name}.csv','r',newline='') as leagueFile:
        reader=csv.reader(leagueFile,delimiter=',',quotechar='|')
        l=0 #l for line to keep track how many lines did we read from the league file
        end_loop=None
        for line in reader:
            if l==0:#first row
                clubs_no=int(line[0])
                end_loop=(clubs_no*(clubs_no-1)) + 1
                l+=1
            elif(l<end_loop):
                #[team1 ,team2, result1 , result2]
                table.append([line[0],line[1],int(line[2]),int(line[3])])
                l+=1
            elif(l>=end_loop):
                #edit clubs with clubs name
                clubs.append(line[0])
                #[name, mp , win, draw, lose, gf, ga, gd ,pts]
                #[0     1    2     3     4     5  6    7   8 ]
                clubs_objs[line[0]]=Club(name=line[0],no_matches=int(line[1]),wins=int(line[2]),draws=int(line[3]),loses=int(line[4]),GF=int(line[5]),GA=int(line[6]),GD=int(line[7]),points=int(line[8]),squad=[])
                #load squad
                with open(f"{os.getcwd()}/{line[0]}/{line[0]}.csv" , "r", newline='') as squad_file:
                    reader_player=csv.reader(squad_file,delimiter=',',quotechar='|')
                    j=0 #to skip first line in the squad file
                    for player in reader_player:
                        if j==0:
                            j=1
                            continue
                        #create player return player object and add player store player object in club squad list
                        clubs_objs[line[0]].add_player(Player(player[0],int(player[1]),player[2],no_goals=int(player[3]),yel_card=int(player[4]),red_card=int(player[5])))
                        # clubs_objs[team].add_player(clubs_objs[team].create_player(player[0],int(player[1]),player[2]))
                l+=1
        
#clubs is list of clubs names
def create_matches(clubs):
    #Create list of matches to be played
    table=[[i,j,-1,-1] for i in clubs for j in clubs if i!=j]
    shuffle(table)
    return table

#function to create new league file.csv
def new_league_file(name):
    #league file will contain the matches table first then the scoreboard
        #create new league file
        with open(f'{os.getcwd()}/{name}.csv','w',newline='') as leagueFile:
            writer=csv.writer(leagueFile,delimiter=',',quotechar='|')
            #save clubs number to know how many matches we have
            writer.writerow([len(clubs)])
            #save matches schudle in the file as [team1 name , team2 name , -1 , -1] -1 stands for the match still not played
            global table
            table=create_matches(clubs)
            for match in table:
                writer.writerow([match[0], match[1],"-1","-1"])
            #then save the scoreboard in any order as all data are zero from dict
            #in that form [name, mp , win, draw, lose, gf, ga, gd ,pts]
            for team in clubs:#team is club name
                writer.writerow([team,"0","0","0","0","0","0","0","0"])

#function to create new league dict
def new_league_dict():
    #the key is club name and the value is club object
    for team in clubs:#clubs list has clubs names
        clubs_objs[team]=Club(name=team,squad=[])
        #load the squad file first
        with open(f"{os.getcwd()}/{team}/{team}.csv" , "r", newline='') as squad_file:
            reader=csv.reader(squad_file,delimiter=',',quotechar='|')
            j=0#to skip first line in squad file
            for player in reader:
                if j==0:
                    j=1
                    continue
                #create player return player object and add player store player object in club squad list
                
                clubs_objs[team].add_player(Player(player[0],int(player[1]),player[2]))
                # clubs_objs[team].add_player(clubs_objs[team].create_player(player[0],int(player[1]),player[2]))
        # print(f"{team} in start= {len(clubs_objs[team].get_squad())}")

#function to print match schulde as gui
#global varialbe to go through the table
i=0
def table_gui(master,i,league_name,state=NORMAL):
    #show all gui for the table
    team1=Label(master,text=f"{table[i][0]}")
    team1_entry=Entry(master,state=state)
    team2_entry=Entry(master,state=state)
    x_button=Button(master,text="X",state=state,command=lambda:x_command(team1_entry,team2_entry,master,x_button,league_name))
    team2=Label(master,text=f"{table[i][1]}")
    team1.grid(row=i+1,column=1,padx=10,pady=10)
    team1_entry.grid(row=i+1,column=2,padx=10,pady=10)
    x_button.grid(row=i+1,column=3,padx=10,pady=10)
    team2.grid(row=i+1,column=4,padx=10,pady=10)
    team2_entry.grid(row=i+1,column=5,padx=10,pady=10)
    team2.grid(row=i+1,column=6,padx=10,pady=10)

def table_gui_dis(master,i,league_name):
    #show all gui for the table
    team1=Label(master,text=f"{table[i][0]}")
    team1_entry=Entry(master)
    team1_entry.insert(0,f"{table[i][2]}")
    team2_entry=Entry(master)
    team2_entry.insert(0,f"{table[i][3]}")
    team1_entry.config(state=DISABLED)
    team2_entry.config(state=DISABLED)
    x_button=Button(master,text="X",state=DISABLED,command=lambda:x_command(team1_entry,team2_entry,master,x_button,league_name))
    team2=Label(master,text=f"{table[i][1]}")
    team1.grid(row=i+1,column=1,padx=10,pady=10)
    team1_entry.grid(row=i+1,column=2,padx=10,pady=10)
    x_button.grid(row=i+1,column=3,padx=10,pady=10)
    team2.grid(row=i+1,column=4,padx=10,pady=10)
    team2_entry.grid(row=i+1,column=5,padx=10,pady=10)
    team2.grid(row=i+1,column=6,padx=10,pady=10)

#used to disable x button and 2 entry and create new table line(next match)
def x_command(e1,e2,master,button,league_name):
    global i
    global clubs_objs
    global table
    val1=e1.get().strip()
    val2=e2.get().strip()
    if( not_empty_entry(e1) and  not_empty_entry(e2) and val1.isdigit() and int(val1)>=0 and val2.isdigit() and int(val2)>=0 ):
        #disable both team1 and team2 entry and xbutton
        e1.config(state=DISABLED)
        e2.config(state=DISABLED)
        button.config(state=DISABLED)
        table[i][2]=val1
        table[i][3]=val2
        match_result(master,clubs_objs[table[i][0]], clubs_objs[table[i][1]],val1,val2)
        clubs_objs=dict(sorted(clubs_objs.items(), key=lambda x:x[1].get_points(),reverse=True))
        #{k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
        modify_file(league_name)
        #recall table gui to create next line of the table 
        i+=1
        if i<len(table):
            table_gui(master,i,league_name)
        else:
            Button(text="exit",command=master.destroy).grid(row=100) #exit button
    else:
        messagebox.showerror("VALID", "NON VAILD SCORE")
        e1.delete(0,END)
        e2.delete(0,END)
        # notfi=Label(master,text="match result should be integer",fg="red")
        # notfi.grid(row=0,padx=10,pady=10)
    
#function to modify the file after change