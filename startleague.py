
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
#global varialbe to go through the table
i=0
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
            #what to do after the league is over
            Label(master,text="your league is over").grid(row=100 , padx=10, pady=10)
            Button(master,text="EXIT",command=master.destroy).grid(row=101 ,column=1, padx=10, pady=10)
            Button(master,text="end league",command=lambda:end_league(master,league_name)).grid(row=101 ,column=3, padx=10, pady=10)
            Button(master,text="Standing",command=scoreboard).grid(row=101 ,column=2, padx=10, pady=10)
            #Button(text="exit",command=master.destroy).grid(row=100) #exit button
    else:
        messagebox.showerror("VALID", "NON VAILD SCORE")
        e1.delete(0,END)
        e2.delete(0,END)
        # notfi=Label(master,text="match result should be integer",fg="red")
        # notfi.grid(row=0,padx=10,pady=10)
    
#function to modify the file after change
def modify_file(name):
    #to modify league file
    with open(f'{os.getcwd()}/{name}.csv','w',newline='') as leagueFile:
        writer=csv.writer(leagueFile,delimiter=',',quotechar='|')
        #save clubs number to know how many matches we have
        writer.writerow([clubs_no])
        #save matches schudle in the file as [team1 name , team2 name , -1 , -1] -1 stands for the match still not played
        global table
        for match in table:
            writer.writerow([match[0], match[1],match[2],match[3]])
        #in that form [name, mp , win, draw, lose, gf, ga, gd ,pts]
        for team in clubs_objs:#team is club name
            writer.writerow([team,clubs_objs[team].get_no_matches(),clubs_objs[team].get_wins(),clubs_objs[team].get_draws(),clubs_objs[team].get_loses(),clubs_objs[team].get_GF(),clubs_objs[team].get_GA(),clubs_objs[team].get_GD(),clubs_objs[team].get_points()])
    #to modify squad for team1
    with open(f'{os.getcwd()}/{table[i][0]}/{table[i][0]}.csv','w',newline='') as squadFile:
        writerPlayer=csv.writer(squadFile,delimiter=',',quotechar='|')
        writerPlayer.writerow(["NAME",'AGE','POSITION','GOALS','Y CARDS','R CARDS'])
        squad=clubs_objs[table[i][0]].get_squad()
        for player in squad:
            writerPlayer.writerow([player.get_name(),player.get_age(),player.get_position(),player.get_no_goals(),player.get_yel_card(),player.get_red_card()])
        print(f"in mod after {table[i][0]} {len(squad)}")
    #to modify squad for team2
    with open(f'{os.getcwd()}/{table[i][1]}/{table[i][1]}.csv','w',newline='') as squadFile:
        writerPlayer=csv.writer(squadFile,delimiter=',',quotechar='|')
        writerPlayer.writerow(["NAME",'AGE','POSITION','GOALS','Y CARDS','R CARDS'])
        squad=clubs_objs[table[i][1]].get_squad()
        for player in squad:
            writerPlayer.writerow([player.get_name(),player.get_age(),player.get_position(),player.get_no_goals(),player.get_yel_card(),player.get_red_card()])
        # print(f"in mod after {table[i][1]} {len(squad)}")

#continue league know where we are in table 
def con_league(master,league_name):
    global i
    for match in table:
        #result for team 1 
        if match[2] != -1:
            table_gui_dis(master,i,league_name)
            i+=1
        else:
            return
#function change dict data through each round
def match_result(master,obj1,obj2,g1,g2):
    page=Toplevel(master)
    g1=int(g1)
    g2=int(g2)
    obj1.goals(g1,g2)
    obj2.goals(g2,g1)
    if g1>g2:
        obj1.win()
        obj2.lose()
    elif g1<g2:
        obj1.lose()
        obj2.win()
    else:
        obj1.draw()
        obj2.draw()
    counter=0
    
    #obj2.add_cards()
    Label(page,text=f"{obj1.get_name()}").grid(row=0,column=0,padx=10,pady=10)
    while counter<g1:
        #n1 will contain player 1 name
        n1=obj1.player_score(1)
        counter += 1 
        Label(page,text=f"{n1} scored").grid(row=counter,column=0,padx=10,pady=10)
    player1,player2,flag=obj1.add_cards()
    Label(page,text=f"{player1} Got yellow card").grid(row=counter+1,column=0,padx=10,pady=10)
    Label(page,text=f"{player2} Got yellow card").grid(row=counter+2,column=0,padx=10,pady=10)
    if flag==1:
        Label(page,text=f"{player1} Got red card").grid(row=counter+3,column=0,padx=10,pady=10)
        
    counter=0
    Label(page,text=f"{obj2.get_name()}").grid(row=0,column=1,padx=10,pady=10)
    while counter<g2:
        n2=obj2.player_score(1)
        counter += 1 
        Label(page,text=f"{n2} scored").grid(row=counter,column=1,padx=10,pady=10)
    player1,player2,flag2=obj2.add_cards()
    Label(page,text=f"{player1} Got yellow card").grid(row=counter+1,column=1,padx=10,pady=10)
    Label(page,text=f"{player2} Got yellow card").grid(row=counter+2,column=1,padx=10,pady=10)
    if flag2==1:
        Label(page,text=f"{player1} Got red card").grid(row=counter+3,column=1,padx=10,pady=10)

#function to show scoreboard where every club name is button to access players data
def scoreboard():
    if len(clubs_objs)==0:
        return
    master=Tk()

    #in that form [name, mp , win, draw, lose, gf, ga, gd ,pts]
    # Label(master,text="CLUB NAME\t\t\tMP\t\t\tWINS\t\t\tDRAWS\t\t\tLOSSES\t\t\tGF\t\t\tGA\t\t\tGD\t\t\tPTS").grid(row=0,padx=10,pady=10)
    Label(master,text="CLUB NAME").grid(row=0,padx=10,pady=10,column=0)
    Label(master,text="MP").grid(row=0,padx=10,pady=10,column=1)
    Label(master,text="WINS").grid(row=0,padx=10,pady=10,column=2)
    Label(master,text="DRAWS").grid(row=0,padx=10,pady=10,column=3)
    Label(master,text="LOSSES").grid(row=0,padx=10,pady=10,column=4)
    Label(master,text="GF").grid(row=0,padx=10,pady=10,column=5)
    Label(master,text="GA").grid(row=0,padx=10,pady=10,column=6)
    Label(master,text="GD").grid(row=0,padx=10,pady=10,column=7)
    Label(master,text="PTS").grid(row=0,padx=10,pady=10,column=8)
    i=1    
    for team in clubs_objs.values():
        team_name=team.get_name()
        button_plyers_data(team_name,master,i)
        Label(master,text=f"{team.get_no_matches()}").grid(row=i,column=1,padx=10,pady=10)
        Label(master,text=f"{team.get_wins()}").grid(row=i,column=2,padx=10,pady=10)
        Label(master,text=f"{team.get_draws()}").grid(row=i,column=3,padx=10,pady=10)
        Label(master,text=f"{team.get_loses()}").grid(row=i,column=4,padx=10,pady=10)
        Label(master,text=f"{team.get_GF()}").grid(row=i,column=5,padx=10,pady=10)
        Label(master,text=f"{team.get_GA()}").grid(row=i,column=6,padx=10,pady=10)
        Label(master,text=f"{team.get_GD()}").grid(row=i,column=7,padx=10,pady=10)
        Label(master,text=f"{team.get_points()}").grid(row=i,column=8,padx=10,pady=10)

        i+=1
    master.mainloop()
#function used to assign each button to different team 
def button_plyers_data(teamName,master,i):
    Button(master,text=teamName,command=lambda:display_squad(clubs_objs.get(teamName),master)).grid(row=i,column=0,padx=5,pady=10)
    # pass
#take club object
def display_squad(obj,master):
    # global master
    squad_page=Toplevel(master)
    # Label(master,text="PLAYER NAME\t\t\t\t\t\tAGE\t\t\tPOSITION\t\t\tNO GOALS\t\t\tYEL CARD\t\t\tRED CARDS").grid(row=0,padx=10,pady=10)
    Label(squad_page,text="PLAYER NAME").grid(row=0,padx=10,pady=10,column=0)
    Label(squad_page,text="AGE").grid(row=0,padx=10,pady=10,column=1)
    Label(squad_page,text="POSITION").grid(row=0,padx=10,pady=10,column=2)
    Label(squad_page,text="NO GOALS").grid(row=0,padx=10,pady=10,column=3)
    Label(squad_page,text="YEL CARD").grid(row=0,padx=10,pady=10,column=4)
    Label(squad_page,text="RED CARDS").grid(row=0,padx=10,pady=10,column=5)
    i=1
    for player in obj.get_squad():
        # Label(master,text=f"{player.get_name()}\t\t\t{player.get_age()}\t\t\t{player.get_position()}\t\t\t{player.get_no_goals()}\t\t\t{player.get_yel_card()}\t\t\t{player.get_red_card()}").grid(row=i,padx=10,pady=10)
        Label(squad_page,text=f"{player.get_name()}").grid(row=i,padx=10,pady=10,column=0)
        Label(squad_page,text=f"{player.get_age()}").grid(row=i,padx=10,pady=10,column=1)
        Label(squad_page,text=f"{player.get_position()}").grid(row=i,padx=10,pady=10,column=2)
        Label(squad_page,text=f"{player.get_no_goals()}").grid(row=i,padx=10,pady=10,column=3)
        Label(squad_page,text=f"{player.get_yel_card()}").grid(row=i,padx=10,pady=10,column=4)
        Label(squad_page,text=f"{player.get_red_card()}").grid(row=i,padx=10,pady=10,column=5)
        i+=1
    # master.mainloop()

#to end current league by deleting file league and close window
def end_league(master,name):
    if os.path.exists(f"{name}.csv"):
        sure=messagebox.askyesno("DELETE","are you sure you want to delete your league?")
        if sure:
            os.remove(f"{name}.csv")
            messagebox.showinfo("DELETED",f"{name} deleted successfully")
            master.destroy()
    else:
        messagebox.showerror("ERROR","file doesn't exist")

#to make menu with file and about only for start league
def main_menu(master,name):
    #menus gui
    menubar=Menu(master)
    #file menu to exit in any time
    filemenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="file",menu=filemenu)
    filemenu.add_command(label="add club",command=lambda:Club.add_club(master))
    filemenu.add_command(label="delete club",command=lambda:Club.delete_club_gui(master))
    filemenu.add_command(label="standing",command=lambda:scoreboard())
    filemenu.add_command(label="end league",command=lambda:end_league(master,name))
    filemenu.add_separator() 
    #to close master window in any time
    filemenu.add_command(label="exit",command=master.destroy)
    #about menu gui to go to github page
    aboutmenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="About",menu=aboutmenu)
    aboutmenu.add_command(label="about me",command=open_link)
    #to set menubar as menu for master
    master.config(menu=menubar)
# to know how many clubs do we have
def clubs_database():
    global clubs_no
    global clubs
    #try to open the file as read to not give error if the file doesn't exist
    try:
        with open(f'{os.getcwd()}/available.csv','r',newline='') as csvfile:
            reader = csv.reader(csvfile,delimiter=',',quotechar='|')
            for row in reader:
                #clubs will conatain the name of the clubs only
                clubs.append(row[0])
            clubs_no=len(clubs)
        #we only need to delete the file if we have enough clubs number otherwise leave the file
        if clubs_no>=3:
            os.remove(f'{os.getcwd()}/available.csv')
        print("No Error")
    except:
        print("Error")
#to start new league
def start_league_gui(window):
    window.destroy()
    '''
    take new league name and check it's avaliable
    '''
    #if league doesn't know how many club do we have
    
    master=Tk()
    master.iconbitmap('4876628.ico')
    master.geometry("750x600")
    league_name_label=Label(master,text="league name")
    league_name_entry=Entry(master)
    league_name_button=Button(master,text="start",command=lambda:start_league(master,league_name_entry,league_name_button))
    league_name_label.grid(row=0, column=0,padx=10,pady=10)
    league_name_entry.grid(row=0, column=1,padx=10,pady=10)
    league_name_button.grid(row=0, column=2,padx=10,pady=10)
    master.mainloop()
#start new league command
def start_league(master,name_entry,button):
    global clubs
    global clubs_no
    global table
    global clubs_objs
    global i
    #to remove any data exist before in the same run avoiding using the same data in different places 
    clubs.clear()
    clubs_no=0
    table.clear()
    clubs_objs.clear()
    i=0
    if not_empty_entry(name_entry):
        name=name_entry.get().strip().title()
        name_entry.config(state=DISABLED)
        button.destroy()
        
        clubs_database()#load from data base
        if f"{name}.csv" in os.listdir(os.getcwd()):
            ask=messagebox.askyesno("ASK","there's the same name do you want to load it?")
            if ask==1:
                main_menu(master,name)
                continue_league(master,name_entry,button)
                name_entry.config(state=DISABLED)
                button.destroy()
        #if there's no league will check for clubs number if bigger then 2 will make new league if not say not enough clubs and give button to add new club
        #start new league
        elif(clubs_no>2):
            main_menu(master,name)
            name_entry.config(state=DISABLED)
            button.destroy()
            new_league_dict()
            #create new league file
            new_league_file(name)
            table_gui(master,i,name)
        elif(clubs_no<3):
            Label(master,text="You don't Have enough clubs to start league").grid(row=1, column=0,padx=10,pady=10)
            add_club=Button(master,text="add club",command=lambda:Club.add_club(master))
            add_club.grid(row=3, column=1,padx=10,pady=10)
    else:
        messagebox.showerror("EMPTY","Empty league name")

def continue_league_gui(window):
    window.destroy()
    master=Tk()
    master.iconbitmap('4876628.ico')
    league_name_label=Label(master,text="league name")
    league_name_entry=Entry(master)
    league_name_button=Button(master,text="start",command=lambda:continue_league(master,league_name_entry,league_name_button))
    league_name_label.grid(row=0, column=0,padx=10,pady=10)
    league_name_entry.grid(row=0, column=1,padx=10,pady=10)
    league_name_button.grid(row=0, column=2,padx=10,pady=10)
    master.mainloop()

#function load data from league file and all squads files
def continue_league(master,name_entry,button):
    global clubs
    global clubs_no
    global table
    global clubs_objs
    global i
    #to remove any data exist before in the same run avoiding using the same data in different places 
    clubs.clear()
    clubs_no=0
    table.clear()
    clubs_objs.clear()
    i=0
    if not_empty_entry(name_entry):
        name=name_entry.get().strip().title()

        if f"{name}.csv" in os.listdir(os.getcwd()):
            main_menu(master,name)
            name_entry.config(state=DISABLED)
            button.destroy()
            load_league(name)
            con_league(master,name)
            # if i reach table length means that all matches had been played so tell the user the league has ended
            if (i>=len(table)):
                Label(master,text="your league is over").grid(row=100 , padx=10, pady=10)
                Button(master,text="EXIT",command=master.destroy).grid(row=101 ,column=1, padx=10, pady=10)
                Button(master,text="end league",command=lambda:end_league(master,name)).grid(row=101 ,column=3, padx=10, pady=10)
                Button(master,text="Standing",command=scoreboard).grid(row=101 ,column=2, padx=10, pady=10)
            else:
                table_gui(master,i,name)
        else:
            ask=messagebox.askyesno("ASK","name not avaliable do you want to create new league?")
            if ask==1:
                main_menu(master,name)
                name_entry.config(state=DISABLED)
                button.destroy()
                start_league(master,name_entry,button)
    else:
        messagebox.showerror("EMPTY","Empty league name")
