#Made by Vincius Santos-Tech
# Web Scraper for TIOBE Index - Programming Language Rankings

import requests
from bs4 import BeautifulSoup
class TiobeScraper():
    def __init__(self):
        self.url = 'https://www.tiobe.com/tiobe-index/'
        pass
    def GetSite(self):
        '''Function that try Get the website'''
        try:
            response = requests.get(self.url)
            self.soup = BeautifulSoup(response.text, 'html.parser')
        except Exception as e:
            return e
            
    def FindObject(self):
        '''Function to find the Object'''
        try:
            tabela = self.soup.find('table', {'id': 'top20'})
            if tabela:
                print("------------ TABLE FOUND!-------------")
                self.lines = tabela.find_all('tr')
        except Exception as e:
            return e 
    def Divcoluns(self):
        '''A function that divides all of the columms'''
        try:
            for line in self.lines[1:]:
                columns = line.find_all('td')
                if len(columns) >= 6: 
                    position = columns[0].text.strip()
                    language = columns[4].text.strip()  
                    rating = columns[5].text.strip()     
                    print(f"Position {position}: {language} - {rating}")
                else:
                    return "Table not found"
        except Exception as e:
            return e
    def Active(self):
        ''' A function that actives The class'''
        self.GetSite()
        self.FindObject()
        self.Divcoluns()

Action = TiobeScraper()
Action.Active()
