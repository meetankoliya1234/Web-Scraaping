import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from requests.api import head

bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url)
print(page)


headers = ['name', 'distance', 'mass', 'radius', 'luminosity']
    
stars_data = []
    
soup = bs(page.text, 'htmp.parser')
    
star_table = soup.find('table')
    
table_rows = star_table.find_all('tr')
    
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    stars_data.append(row)
    
Star_names = []
Distance = []
Mass = []
Radius = []
Lum = []
        
for i in range(1, len(stars_data)):
    Star_names.append(stars_data[i][1])
    Distance.append(stars_data[i][3])
    Mass.append(stars_data[i][5])
    Radius.append(stars_data[i][6])
    Lum.append(stars_data[i][7])
        
df2 = pd.DataFrame(list(zip(Star_names, Distance, Mass, Radius, Lum)), columns = [headers])
print(df2)
    
df2.to_csv('bright_stars.csv')