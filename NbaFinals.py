import pandas as pd

#Step 1 Get the data
df = pd.read_csv('championsdata.csv', index_col=0)


#Step 2 : Filter for Every Game 1 played at the championship teams home
query1_df = df[df.columns[0:4]][(df['Game']==1) & (df['Home']==1)]
# print((query1_df)) 


# Shows only teams that won Game 1 at home
total = query1_df['Win'].isin([1])
# print(total)


# Prints total number of Wins for Game 1 at home
WinTotal = query1_df['Win'].sum()
# print (WinTotal)


# Stores number of rows in variable
number_of_rows = len(query1_df)

# Prints the percent of Championship teams that have actually won Game 1 of the NBA Finals series at Home
WinningPercentage = WinTotal/number_of_rows*100
print("NBA Championship teams that have actually won Game 1 at home in the Nba Finals : " ,WinningPercentage , "%")


# Export results into a new csv file
# query1_df.to_csv('RaulsQueryresults.csv')


#----------------------------------------------------------------------------
#Percentage of Championship teams that have won any Game 1(Home or away)
# df = pd.read_csv('championsdata.csv', index_col=0)

# query1_df = df[df.columns[0:4]][(df['Game']==1)]
# total = query1_df['Win'].isin([1])
# WinTotal = query1_df['Win'].sum()
# number_of_rows = len(query1_df)
# WinningPercentage = WinTotal/number_of_rows*100
# print("NBA Championship teams that have actually won Game 1 away or at home in the Nba Finals : " ,WinningPercentage , "%")



#Runner Up Data ------------------------------------------------------------------

# df = pd.read_csv('runnerupsdata.csv', index_col=0)



#  Filter for Every Game 1 played at the RunnerUps teams home
# query2_df = df[df.columns[0:4]][(df['Game']==1) & (df['Home']==1)]

# Shows only runner up teams that won game 1
# total2 = query2_df['Win'].isin([1])
# print(total2)

# Prints total number of Wins for Game 1 at home
# WinTotal2 = query2_df['Win'].sum()
# print("Number of RunnerUp wins for Game 1 at home: ",WinTotal2)

# Stores number of rows in variable
# number_of_rows2 = len(query2_df)


# Prints the percent of Championship teams that have actually won Game 1 of the NBA Finals series at Home
# WinningPercentage2 = WinTotal2/number_of_rows2*100
# print("RunnerUp teams that have actually won Game 1 at home in the Nba Finals : " ,WinningPercentage2 , "%")


#------------------------------------------------------------------------------------------
# df = pd.read_csv('runnerupsdata.csv', index_col=0)


#Shows game 1 for all Runner up teams since 1980 - 2018
# query2_df = df[df.columns[0:4]][(df['Game']==1) ]
# print(query2_df)



#Shows only runner up teams that lost game 1 (Home and Away)
# total2 = query2_df['Win'].isin([0])
# print(total2)


# Prints total number of Losses for Game 1 at home
# WinTotal = total2.sum()
# print(WinTotal)


# Stores number of rows in variable
# number_of_rows = len(query2_df)


# WinningPercentage = WinTotal/number_of_rows*100
# print("NBA Runner Up teams that have lost Game 1 at home/away in the Nba Finals : " ,WinningPercentage , "%")

# Export results into a new csv file
#query2_df.to_csv('RunnerUpWinResults.csv')


