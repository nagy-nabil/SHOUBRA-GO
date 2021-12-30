# SHOUBRA-GO
![LOGO](https://github.com/nagy-nabil/SHOUBRA-GO/blob/main/Shoubra_GO-logos_black.png)
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
by adding clubs[^club] and players[^player] to the database you can create league with them by choosing the league name[^league]
after having league the program create matches where every team face all other teams twice(one home one away)
in real version of the program , the program will get every match score from API, but in our case it get the score from the user and assign the goals etc... to random player
the program working with autosaver any valid data automatically go to the database

## using
* python oop
* gui with TKINTER
* csv files as database
* random library
* webbrowser library

[^player]Player class where we store data about each player (name,age,position,number of goals,number of yellow cards,number of red cards)
set the basic methods for any player like getters , setters , how to store player , the validations , send player data to club, and the gui to input player data

[^club]Club class where we store data about each club (name,number of matches,wins,draws,loses,goals for,goals against,goals difference,points,squad list)
set the basic methods for any club like getters , setters ,add new club,  how to store club in database , the validations , gui to add club ,gui to delete club and any gui related to club class

[^league]league file where we set the essitial data to be knwon about any league (name,clubs list)
set the basic methods to deal with any league like how to start new league, the validations to start new league , read the database to get valid clubs,how to make the matches table, store every league data in our database, read leagues database to continue league , edit clubs and players database after each match, and how to end league(delete from database)
after having league (start new one, load one from database)
show the gui for each match , the scoreboard , each team players data , matches table, and how to send the data of every match for the clubs and players database

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
