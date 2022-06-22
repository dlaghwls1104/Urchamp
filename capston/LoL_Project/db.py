import numpy as np
import pandas as pd
import pymysql
#이게 db넣는 코드
# T100 : Team 100 (Blue team) 챔피언 리스트
# T200 : Team 200 (Red team) 챔피언 리스트
# win : 100이면 Team 100 승리, 200이면 Team 200 승리
conn = pymysql.connect(host='localhost', user='root', password='dlwlgns21@', db='lolProject', charset='utf8')

curs = conn.cursor()

#이게 csv 
df = pd.read_csv('C:/Users/dlagh/lastdata0.csv',index_col=0, encoding='utf-8')

for i in range(len(df)):
    sql1 = "insert into df_game(T100,T200,win) values ('"+df['T100'][i]+"','"+df['T200'][i]+"','"+str(df['win'][i])+"');"
    curs.execute(sql1)
    conn.commit() 
conn.close()