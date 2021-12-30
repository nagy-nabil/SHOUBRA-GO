# SHOUBRA-GO

## **CONTRIBUTORS**
* Nagy Nabil
* Omar Khaled
* Omar Ezzat
* Mohamed Tarek
* Rana Ahmed
* Raneem Wael

## UNDER THE SUPERVISION OF
### DR. SABAH ABDELAZIZ

## introduction 
simulating making and managing a real football league
by adding clubs[^club]. and players[^player]. to the database you can create league with them by choosing the league name[^league].
after having league the program create matches where every team face all other teams twice(one home one away)
in real version of the program , the program will get every match score from API, but in our case it get the score from the user and assign the goals etc... to random player
the program working with autosaver any valid data automatically go to the database

#### main page
![mainpage](https://github.com/nagy-nabil/SHOUBRA-GO/blob/main/images/mainpage.jpg)

#### main menu
![mainmenu](https://github.com/nagy-nabil/SHOUBRA-GO/blob/main/images/mainmenu.jpg)
## using
* python oop
* gui with TKINTER
* csv files as database
* random library
* webbrowser library

[^player]: Player class where we store data about each player (name,age,position,number of goals,number of yellow cards,number of red cards)
set the basic methods for any player like getters , setters , how to store player , the validations , send player data to club, and the gui to input player data

#### take player data
> player name , age and position

[^club]: Club class where we store data about each club (name,number of matches,wins,draws,loses,goals for,goals against,goals difference,points,squad list)
set the basic methods for any club like getters , setters ,add new club,  how to store club in database , the validations , gui to add club ,gui to delete club and any gui related to club class
#### add club window 
> unique club name, with at least 5 players
![add club](https://github.com/nagy-nabil/SHOUBRA-GO/blob/main/images/addclub.jpg)

#### delete club
>frame will show at the end of the window

![delete club](https://github.com/nagy-nabil/SHOUBRA-GO/blob/main/images/delete%20club.jpg)

[^league]: league file where we set the essitial data to be knwon about any league (name,clubs list)
set the basic methods to deal with any league like how to start new league, the validations to start new league , read the database to get valid clubs,how to make the matches table, store every league data in our database, read leagues database to continue league , edit clubs and players database after each match, and how to end league(delete from database)
after having league (start new one, load one from database)
show the gui for each match , the scoreboard , each team players data , matches table, and how to send the data of every match for the clubs and players database
#### start new league
> should be at least 3 clubs in database and not in active league
> if the name already exist ask you if you want to load the data
> if the database has enough clubs will load the clubs data and create the matches table
> after each match show the players stats
![start league](https://github.com/nagy-nabil/SHOUBRA-GO/blob/main/images/startleague.jpg)

#### continue league
>if the league name doesn't exist the programm will ask you if you want to create a new one
![continue](https://github.com/nagy-nabil/SHOUBRA-GO/blob/main/images/continueleague.jpg)

#### scoreboard and team stats
>show the standings , and every team name is button to show club stats
![scoreboard](https://github.com/nagy-nabil/SHOUBRA-GO/blob/main/images/playersdata.jpg)
### GENERAL VALIDATIONS
* *any input or entry*
    * **cannot be empty**  
    * **automatically delete any extra spaces**
* *string input or entry*
    * **cannot be empty**
    * **cannot be all numbers**  
    * **automatically delete any extra spaces**
    * **for some input the string should be something special like players position**
* *numbers entry or input*
    * **cannot be empty**  
    * **automatically delete any extra spaces**
    * **any entry return string so user input should be able convertable to numbers(means no chars or special chars)**
    * **for most of numbers input required numbers in interval to keep the data real**
* *objects data*
    * **cannot be empty**  
    * **automatically delete any extra spaces**
    * **names should be unique like clubs name league name but for players will refuse the data if the name ,age and position are the same**
