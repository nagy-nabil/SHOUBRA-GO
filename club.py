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
