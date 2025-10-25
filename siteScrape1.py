# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 19:18:44 2025

@author: thedo
"""

def main():

    from bs4 import BeautifulSoup
    import requests

    def fetching(): 

        url = 'https://www.scrapethissite.com/pages/forms/'
        page = requests.get(url)
    
    
        soup = BeautifulSoup(page.text, 'html.parser')
        teams = soup.find_all('tr', class_='team')

 
        for team in teams:
            name = team.find('td', class_='name').get_text(strip=True)
            year = team.find('td', class_='year').get_text(strip=True)
            wins = team.find('td', class_='wins').get_text(strip=True)
            losses = team.find('td', class_='year').get_text(strip=True)
            winrate = team.find('td', class_='pct').get_text(strip=True)
        
            print("\n")
            print(name.center(50))
            print("=" * 100)
            print("Year: ", year, " ---- Wins: ", wins, " ---- Losses: ", losses, "---- Win percentage: ", winrate)
            print("=" * 100)


    fetching()

main()

##names = soup.findAll()
