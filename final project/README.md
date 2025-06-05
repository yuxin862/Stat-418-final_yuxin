## Three popular steam games player counts prediction

#### Description
The data was scrapped from the Steam Charts website.(an ongoing analysis of Steam's concurrent players), SteamAPi and Google trend. I chose three popular games from steam which are Counter Strike 2, Dota2 and Pubg. These three games are different types of games even though Pubg and CS2 are fps games. Their game mode is totally different. I want to predict the average player counts of three different games using Time Series Model(Prophet). Finally I will compare the three predictions to get which game will be popular and better in the future.

The reason why I chose prophet model because:
1. Capturing long-term trends
2. Modeling seasonality (e.g., monthly/weekly cycles)
3. Handling missing data or outliers gracefully



#### Data Scrapping 
Using request.get, beautifulsoup and pytrend to scrap the data from website and api.
The scraping code is in

#### EDA

##### Variables
Avg.players - Average players counts
Gain - the increasing number of players comparing to last month
%Gain - increasing percentage of number of players comparing to last month
Peak players - the highest number of players during this month

I added two external variables after the first persentation
Patch_Count - using request to get updated patches released per month from steamapi
Google_Trends_Index - using pytrend to extract monthly search interest data from google trend

I finally used Avg.player(target), Patch_Count and Google_Trends_Index in my model

#### Data cleaning

I scrapped the data from three different place and combines them together. I want to do the Prophet model separtely, I make one csv files for each game.

The data was scrapped from 2012/7/1 to 2025/5/1 for cs2 and dota2, but pubg is start from 2017/3/1 to 2025/5/1 because it is a new game comparing with cs and dota.

In my model prediction, I finally choose the start date from 2021 since I want to make the prediction accurate. I did use the start date from 2012, but the predicted result for cs2 player counts is around 1 million on June 1st 2025. And the actual player counts now is 1.7 million. So the prediction result is significantly different from actual value, lead me to make the start date close to the current date and also set the changepoint scale for prophet as 1 to make it more sensitive to the trend.

#### plot

I made average player counts plot for the three games and use STL method that help to check trend, seasonality and residuals for three games.

### Predicted result for three games after ten months

The average player counts for CS2 and Pubg is still increasing in the future, but the number of players
of Dota2 is decreasing. We can imply that in the future, less people will play moba games. And FPS and Battle Royale is still
hot genre for games. This might support game developers in content planning.
