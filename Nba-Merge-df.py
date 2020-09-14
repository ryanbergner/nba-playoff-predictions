import pandas as pd
import numpy as np

# data from https://www.basketball-reference.com/leagues/NBA_2020.html 

# First, we will rename the columns in the opponent dataframe so we can tell the difference between the columns in the team dataframe and the opponent dataframe

dfteam = pd.read_csv("NbaTeamData.csv")

dfopponent_unlabled = pd.read_csv("NbaOpponentData.csv")


# Create a dictionary to convert team column names to opponent stats column names for clarity (did not include team column because that would make no sense)
# We will also use team name 

dict_to_opp = {'Rk' : 'opp_Rk', 'G' : 'opp_G', 'MP' : 'opp_MP', 'FG' : 'opp_FG', 'FGA' : 'opp_FGA', 'FG % ' : 'opp_FG %', '3P' : 'opp_3P', '3PA' : 'opp_3P', '3P % ' : 'opp_3P %', '2P' : 'opp_2P',
               '2PA' : 'opp_2PA', '2P%' : 'opp_2P%', 'FT' : 'opp_FT', 'FTA' : 'opp_FTA', 'FT%' : 'opp_FT%', 'ORB' : 'opp_ORB', 'DRB' : 'opp_DRB' , 'TRB' : 'opp_TRB', 'AST' : 'opp_AST', 'STL' : 'opp_STL',
               'BLK' : 'opp_BLK', 'TOV' : 'opp_TOV', 'PF' : 'opp_PF', 'PTS' : 'opp_PTS'}

dfopponent = dfopponent_unlabled.rename( columns = dict_to_opp , inplace = False)


df_nba = dfteam.merge(dfopponent, how = "right", on = ["Team"])

print(df_nba)
