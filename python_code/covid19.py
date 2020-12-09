import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
try:
    URL = 'https://www.worldometers.info/coronavirus/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='main_table_countries_yesterday')
    #timedelta for adding or substracting date and time
    yesterday= datetime.now() + timedelta(days=-1)
    #print(results.prettify())
    #List for holding actual data
    data=[]
    #list within list for holding multiple columns data
    #newdatat = []
    #remove_chars
    #rm_chars=[',','+']
    #tr is table row and td means table data
    rows=results.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols])
    #print(data)
    #newdatat is list of list and columns is defined for case
    #covid=pd.Dataframe(data)
    #covid
    covid=pd.DataFrame(data,columns = ['serial','Country','TotalCases','NewCases','TotalDeaths','NewDeaths','TotalRecovered','NewRecovered','ActiveCase','SeriousCase','TotCases_1m','Deathcase_1m','Total_test','Total_test_1m','populations','continent','case','death','test'])
    #print(covid.head())
    date_time = yesterday.strftime("%Y-%m-%d")
    covid['dates']=date_time
    covid.to_csv('covid19_'+date_time+'.csv',index=False,encoding='utf-8')
    
    print("Export Successfully")
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
