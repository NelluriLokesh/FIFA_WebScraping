'''
Steps to do Web Scraping

-  te data link "https://www.futwiz.com/en/fifa22/players"
-  Import all Libraries for WebScarpping , Analysis and Visualization
-  WebScrape the data from Sofifa.com
-  Convert the webscarped data into DataFrame.
-  Convert the DataFrame into Excel Sheet.
-  DO Exploration Analysis.
-  Explore Data Analysis.
        1.Find the name of the player who is having the highest value
        2. Hightest and Lowest 
            2.1 Find the the hightest PAC player
            2.2 Find the lowest PAC player
        3.list out the top 10 player accrding to their PAC
        4.create a new dataframe with the values of cloumes-- name and Rating
        5.plot a graphes x = first 10 players name
                         y = players Rating
        6.Find the player has the hightest values
        7.Find the player who as value more than 500
        8.find the player name who as over all 99 and Rating as 5
        9.find all the player whose PAC = 99 and Rating = 4
-  DO Visualizations.



'''
### step 1. Importation of library

import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from bs4 import BeautifulSoup
import requests

## an empty Data Frame to store the data in different web pages
FIFA_data = pd.DataFrame() 

###         step 2. checking the status code
n = int(input("Enter the no.of pages to scrap for the web : "))
for i in range(n):
    url = f'https://www.futwiz.com/en/fifa22/players?page={i}'
    req = requests.get(url)

###     step 3.scraping the data (OR)  parsing HTML and XML documents
    soup = BeautifulSoup(req.content)
    
    ### there are the table names which i want to scrap from web
    player_image = []
    player_name = []
    value = []
    code = []
    over_all = []
    PAC = []
    Rating = []
    Right_Striker = []
    DEF = []

##       create a empty one to append the data after cleaning
##  list refers to the no.of tables that you have created  
    lists = [[] for _ in range(8)] 

###                     4.data exploration,cleaniing,muniplunation
    for i in soup.findAll('tr'):
        player_image = re.sub('\n|^<.*>|<.*>$|<a.*src="|"/></a>','',str(i.find('td',{'class':'face'})))
        player_name = re.sub('\n|^<.*>|<.*>$|<img.*png">|<a href.*"><b>|</b></a>','',str(i.find('p',class_='name')))
        code = re.sub('\n|^<.*>|<.*>$|<img.*">| <a.*</a>|</a>|<a.*\d+/0">','',str(i.find('p',class_='team')))
        over_all = re.sub('\n|^<.*>|<.*>$|<a.*>|<div.*t">|</div>.*>|</a>','',str(i.find('td',class_='ovr')))
        PAC = re.sub('\n|^<.*>|<.*>$|<td.*>|<span |</span>|class="statLabel">.*>|class="stat">','',str(i.find('td',{'class':'statCol'})))
        Rating = re.sub('\n|<.*>','',str(i.find('span',class_='starRating')))
        Right_Striker = re.sub('\n|^<.*>|<span.*">|</span> </span>','',str(i.find('span',{'class':'wrs'})))
        value = re.sub('^<.*>|\n|<.*>$|M|K','',str(i.find('td',{'width':30})))
        lists[0].append(player_image)
        lists[1].append(player_name)
        lists[2].append(value)
        lists[3].append(code)
        lists[4].append(over_all)
        lists[5].append(PAC)
        lists[6].append(Rating)
        lists[7].append(Right_Striker)        
        
        # value = pd.to_numeric(value)

###              step 5.convert it into the dataframe
        DATA = pd.DataFrame({'image':lists[0],'name':lists[1],'value':lists[2],'code':lists[3],'over_all':lists[4],
                            'PAC':lists[5],'Rating':lists[6],'Right_Striker':lists[7]})
        DATA.drop(0 , inplace=True)
        
    FIFA_data = pd.concat([FIFA_data,DATA],ignore_index=True)
    
print(FIFA_data)


## Here changing the Dtype of the columns
DATA['value'] = pd.to_numeric(DATA['value'])
DATA['code'] = pd.to_numeric(DATA['code'])
DATA['over_all'] = pd.to_numeric(DATA['over_all'])
DATA['PAC'] = pd.to_numeric(DATA['PAC'])
DATA['Rating'] = pd.to_numeric(DATA['Rating'])
# DATA['Right_Striker'] = pd.to_numeric(DATA['Right_Striker'])


###                        step 6.exploringthe data
##      1.droping one are more columns
FIFA_data.drop(['image'],inplace=True,axis=1)
##      2.droping one are more columns which as one null values
# FIFA_data.dropna(['image','value'],inplace=True,axis=1)

##     3. to see first 10 data points 
# print(FIFA_data.head(10))

##     4. to see last 10 data points
# print(FIFA_data.tail(9))

##     5.to decribe the table
# print(FIFA_data.describe())

##                   step 7. data analytics

##          1.Find the name of the player who is having the highest PAC

# print(FIFA_data.duplicated().sum(axis=0))
# FIFA_data.drop_duplicates(inplace=True)
# print(FIFA_data[FIFA_data['PAC']==max(FIFA_data['PAC'])]['name'])


# #         # 2. Hightest and Lowest 
# ## 2.1 Find the the hightest PAC player
# print(FIFA_data[FIFA_data['PAC']== min(FIFA_data['PAC'])][['name','PAC']])

# ## 2.2  Find the the Lowest PAC player
# print(FIFA_data[FIFA_data['PAC']== max(FIFA_data['PAC'])][['name','PAC']])
   
            
###         3.list out the top 10 player accrding to their PAC
# print(FIFA_data.sort_values(by='PAC',ascending=False)['name'].head(10))


###         4.create a new dataframe with the values of cloumes-- name and Rating
# fifa_new = FIFA_data[['name','Rating']]
# print(fifa_new) 


# ##        5.plot a graphes in x = first 10 players name
# ##                            y = first 10 players Rating
# x = FIFA_data['name'][:10]
# y = FIFA_data['Rating'][:10]
# print(plt.bar(x,y))
# plt.xlabel("player_names")
# plt.ylabel("player_rating")
# plt.title("names and their rating")
# plt.grid()
# plt.show()


# #         6.Find the player has the hightest values
# print(FIFA_data[FIFA_data['value']== FIFA_data['value']]["name"].head(1))


# ##       7.Find the player who as move value than 500
# print(FIFA_data[FIFA_data['value']>=500]['name'])


# ##       8.find the player name who as over all 99 and Rating as 5
# print(FIFA_data[(FIFA_data['over_all'] == 98) & (FIFA_data['Rating'] == 5)])


# ##       9.find all the player whose PAC = 99 and Rating = 4
print(FIFA_data[(FIFA_data['PAC']==10)  &  (FIFA_data['Rating']==50)]['name'])

