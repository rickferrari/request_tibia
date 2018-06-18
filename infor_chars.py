    #IMPORTS
import requests
from bs4 import BeautifulSoup
##import pandas as pd
from datetime import datetime
import sqlite3
##import worlds_list.py #import list of world

    # Data e hora de extração
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S, %A")

    # Load File
chars = list(open('char_name.txt','r'))
    # Remove /n
chars = [s.rstrip() for s in chars]

##https://secure.tibia.com/community/?subtopic=characters&name=Dudys
url = []
urli = 'https://secure.tibia.com/community/?subtopic=characters&name='

for c in chars:
        url.append(urli + c)
        

        # Conectando a base de dados
conn = sqlite3.connect('tibia.db')
cursor = conn.cursor()


        #SOUP
chars = []
chars1 = []
for u in url:    
    print(u)
    r = requests.get(u)
    soup = BeautifulSoup(r.text, 'html.parser')
    table = soup.find('div', attrs={'class':'BoxContent'})
    rows = table.find_all('tr')

        ## Pasando pelas linhas e agrupando em uma lista
    for row in rows: #Organizando as linhas da extração
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
##        print(cols)
        cols.append(now) #Insere a data de extração em cada linha
##        if len(cols[0]) < 3: #Eliminando a linha de "titulo"
        chars.append([ele for ele in cols if ele]) #Livrar-se de valores vazios
##        print(cols)
lista = list(chars)
##print (lista)
##for i in (1,2,3,4,5,6,7,8,9,11,15):
##    chars1[0].append((lista[i][0]).replace(u'\xa0', ' '))
for i in (1,2,3,4,5,6,7,8,9,11,15,17):
    chars1.append((lista[i][1]).replace(u'\xa0', ' '))
print(chars1)
##print(chars1)
##
##        #Inset data in table
##cursor.execute("""DELETE FROM char_infor""")
##conn.commit()
##cursor.execute("""UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='char_infor';""")
##conn.commit()
####for dmain in chars1:
####        print(dmain)
##cursor.execute("""
##INSERT INTO char_infor (Name, Sex, Vocation, Level, Achievement, World,
##Residence, House, Last_Login, Account_Status, Loyalty_Title, Extract_data)
##VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""",(chars1))
conn.commit()
print('Dados inseridos com sucesso.')
conn.close()



         
