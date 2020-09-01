import requests 
import pprint
from bs4 import BeautifulSoup # html parser

# Returns full URL belonging to the ID of the workshop mutator
def convertToUrl(id):
    if (type(id) != str):       # Converts id into string
        id = str(id)
    URL = "https://steamcommunity.com/sharedfiles/filedetails/?id=" + id
    return URL

# Returns size and date of the workshop mutator
def getSizeAndDate(result):
    results = result.split("\n")
    filtered_results = []
    for i in results:
        if (i == ''):
            pass
        else:
            filtered_results.append(i)

    return filtered_results[0], filtered_results[-1]

# name, size, date
def getWorkShopInfo(id):
    URL = convertToUrl(id)
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, 'html.parser')

    name = soup.find('div', class_='workshopItemTitle').getText()
    details = soup.find(class_='detailsStatsContainerRight').getText()
    
    size, date = getSizeAndDate(details)

    return name, size, date

# getWorkShopInfo(2058869377)
    