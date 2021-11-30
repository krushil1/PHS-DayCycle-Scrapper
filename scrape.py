import requests
from bs4 import BeautifulSoup
import datetime


url = "https://phs.parklandsd.org/about/calendar"
page = requests.get(url)
data = page.text
soup = BeautifulSoup(data, 'html.parser')

scrapedData = [] #initializes scrapedData's array to blank 
found = False 

# Today's date
current_date = datetime.datetime.today()
day = current_date.strftime('%a')  # abbreviated day Ex: Fri
month = current_date.strftime('%b') # abbreviated month Ex: Dec
dayNum = current_date.strftime('%d')
date = " " + day + ", " + month + " " + dayNum

# Uses the listed class to scrape the data from the calendar
#  Mon, Nov 1   Day 5    HS -  Fall SAT Prep Class - 3-5pm  / 6:30-8:30pm PHS / Virtual    HS - A Schedule
for ff in soup.findAll("div", {"class": "fsStateHasEvents"}): 
    new = ff.text #converts the scrapped data in readable text
    for i in new : 
        filteredString = new.replace("\n", ' ') #removes anything that has \n
        fullstring = filteredString
        substring = 'Day'
        if fullstring.find(substring) != -1: #only runs if the scraped string contains the word day
            newFiltered = filteredString[filteredString.find('Schedule') + -16:] #Removes the extra information like the date in the front
            print(newFiltered)
            found = True
            break
        else:
            break
    
    if found == True:
        scrapedData.append(filteredString)

    # scrapedData.append(filteredString) #adds the filtered data to the array of scrapedData
# print(scrapedData)
# Fri, Dec 3   Day 2    HS - A Schedule



# Next day's date
tom_date = datetime.date.today() + datetime.timedelta(days=1)
dayTom = tom_date.strftime('%a')  # abbreviated day Ex: Fri
monthTom = tom_date.strftime('%b') # abbreviated month Ex: Dec
dayNumTom = tom_date.strftime('%d')
dateTom = " " + dayTom + ", " + monthTom + " " + dayNumTom
# print(dateTom)

# Day after's date
next_date = datetime.date.today() + datetime.timedelta(days=2)
dayNext = next_date.strftime('%a')  # abbreviated day Ex: Fri
monthNext = next_date.strftime('%b') # abbreviated month Ex: Dec
dayNumNext = next_date.strftime('%d')
dateNext = " " + dayNext + ", " + monthNext + " " + dayNumNext
# print(dateNext)