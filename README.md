## Three popular steam games player counts prediction

#### Description
The data was scrapped from the Steam Charts website.(an ongoing analysis of Steam's concurrent players). I chose three popular games from steam which are Counter Strike 2, Dota2 and Pubg. These three games are different types of games even though Pubg and CS2 are fps games. Their game mode is totally different. I want to predict the player counts of three different games using Time Series Model. Finally I will compare the three prediction to get which game will be popular in the future.


#### Data Scrapping
Using request.get and beautifulsoup to scrap the data from website

#### EDA

##### Variables
Avg.players - Average players counts
Gain - the increasing number of players comparing to last month
%Gain - increasing percentage of number of players comparing to last month
Peak players - the highest number of players during this month

#### Data cleaning
I removes some rows from CS2 and Dota2 to make the start date same. Now the data is from 2017/3/1 to 2025/4/1. I use Time Series Model and plot the the average player over time for three games to check if it is stationary. All of them are not stationary, so I difference the series.


