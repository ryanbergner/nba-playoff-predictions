from Nba_Merge_df import df_nba
import pandas as pd
import numpy as np

# 1) Remove Leage average row
# 2) Remove Columns 'Rk' and 'opp_Rk' because these variables are already correleated to the team and opponent data - would cause problems in machine learning algorithm
# 3) Make a label row (y-variable) giving information on weather or not each team ended up making the playoffs.
# 4) Split dataset into western and eastern confrences (8 teams from each confrence make the playoffs - we must split confrences in case one conference has overall better teams than the other)

#1)

df_nba = df_nba.drop(30 , axis = 0)

#2) 

df_nba = df_nba.drop(['Rk', 'opp_Rk' ], axis = 1)

#3)

playoff_dict = {
    "Dallas Mavericks*": 1,
    "Milwaukee Bucks*": 1,
    "Portland Trail Blazers*": 1,
    "Houston Rockets*": 1,
    "Los Angeles Clippers*": 1,
    "New Orleans Pelicans": 0,
    "Phoenix Suns": 0,
    "Washington Wizards": 0,
    "Memphis Grizzlies": 0,
    "Boston Celtics*": 1,
    "Miami Heat*": 1,
    "Denver Nuggets*": 1,
    "Toronto Raptors*": 1,
    "San Antonio Spurs": 0,
    "Philadelphia 76ers*": 1,
    "Los Angeles Lakers*": 1,
    "Brooklyn Nets*": 1,
    "Utah Jazz*": 1,
    "Indiana Pacers*": 1,
    "Oklahoma City Thunder*": 1,
    "Sacramento Kings": 0,
    "Orlando Magic*": 1,
    "Atlanta Hawks": 0,
    "Minnesota Timberwolves": 0,
    "Detroit Pistons": 0,
    "New York Knicks": 0,
    "Cleveland Cavaliers": 0,
    "Chicago Bulls": 0,
    "Golden State Warriors": 0,
    "Charlotte Hornets": 0
    }

df_nba["In_Playoffs"] = df_nba["Team"].map(playoff_dict)

#4)

conference_dict = {
    "Dallas Mavericks*" : "Western",  
    "Milwaukee Bucks*" : "Eastern" ,  
    "Portland Trail Blazers*" : "Western",
    "Houston Rockets*" : "Western",
    "Los Angeles Clippers*" : "Western",
    "New Orleans Pelicans" : "Western",
    "Phoenix Suns" : "Western", 
    "Washington Wizards" : "Eastern",
    "Memphis Grizzlies" : "Western",
    "Boston Celtics*" : "Eastern", 
    "Miami Heat*" : "Eastern", 
    "Denver Nuggets*" : "Western",
    "Toronto Raptors*" : "Eastern",
    "San Antonio Spurs" : "Western",
    "Philadelphia 76ers*" : "Eastern",
    "Los Angeles Lakers*" : "Western",
    "Brooklyn Nets*" : "Eastern",
    "Utah Jazz*" : "Western", 
    "Indiana Pacers*" : "Eastern", 
    "Oklahoma City Thunder*" : "Western",
    "Sacramento Kings" : "Western",
    "Orlando Magic*" : "Eastern",
    "Atlanta Hawks" : "Eastern",
    "Minnesota Timberwolves" : "Western",
    "Detroit Pistons" : "Eastern",
    "New York Knicks" : "Eastern", 
    "Cleveland Cavaliers" : "Eastern",
    "Chicago Bulls" : "Eastern",
    "Golden State Warriors" : "Western",
    "Charlotte Hornets" : "Eastern"
    }


df_nba["Conference"] = df_nba["Team"].map(conference_dict)

df_nba_west = df_nba[df_nba["Conference"] == "Western"]
df_nba_east = df_nba[df_nba["Conference"] == "Eastern"]




print(df_nba)
print(df_nba_west)
print(df_nba_east)

