# -*- coding: utf-8 -*-

from flask import Flask, render_template, redirect, request, url_for
import csv
import json
import requests
import numpy as np
import pandas as pd
import pymysql
import time
import datetime
import ast
from pandasql import sqldf
dfsql = lambda q: sqldf(q, globals())
from operator import itemgetter
import requests
import re
from bs4 import BeautifulSoup


app = Flask(__name__)

conn = pymysql.connect(host='localhost', user='root', password='dlwlgns21@', db='lolProject', charset='utf8')

curs = conn.cursor()

a=["Aatrox","Ahri","Akali","Alistar","Amumu","Anivia","Annie","Aphelios","Ashe","AurelionSol","Azir","Bard","Blitzcrank","Brand","Braum","Caitlyn","Camille","Cassiopeia",
"Chogath","Corki","Darius","Diana","Draven","DrMundo","Ekko","Elise","Evelynn","Ezreal","Fiddlesticks","Fiora","Fizz","Galio","Gangplank","Garen",
"Gnar","Gragas","Graves","Hecarim","Heimerdinger","Illaoi","Irelia","Ivern","Janna","JarvanIV","Jax","Jayce","Jhin","Jinx","Kaisa","Kalista",
"Karma","Karthus","Kassadin","Katarina","Kayle","Kayn","Kennen","Khazix","Kindred","Kled","KogMaw","Leblanc","LeeSin","Leona","Lissandra","Lucian",
"Lulu","Lux","Malphite","Malzahar","Maokai","MasterYi","MissFortune","MonkeyKing","Mordekaiser","Morgana","Nami","Nasus","Nautilus","Neeko","Nidalee","Nocturne",
"Nunu","Olaf","Orianna","Ornn","Pantheon","Poppy","Pyke","Qiyana","Quinn","Rakan","Rammus","RekSai","Renekton","Rengar","Riven","Rumble","Ryze","Sejuani",
"Senna","Sett","Shaco","Shen","Shyvana","Singed","Sion","Sivir","Skarner","Sona","Soraka","Swain","Sylas","Syndra","TahmKench","Taliyah","Talon",
"Taric","Teemo","Thresh","Tristana","Trundle","Tryndamere","TwistedFate","Twitch","Udyr","Urgot","Varus","Vayne","Veigar","Velkoz","Vivi","Viktor",
"Vladimir","Volibear","Warwick","Xayah","Xerath","XinZhao","Yasuo","Yorick","Yuumi","Zac","Zed","Ziggs","Zilean","Zoe","Zyra","Lillia","Yone","Samira",
"Seraphine","Rell","Viego","Gwen"]
top=["Aatrox","Akali","Camille","Chogath","Darius","DrMundo","Fiora","Gangplank","Garen","Gnar","Graves","Heimerdinger","Illaoi","Irelia","Jax","Jayce","Kayle","Kennen","Kled","Lucian","Malphite","Maokai","MonkeyKing","Mordekaiser","Nasus","Olaf","Ornn","Pantheon","Poppy","Quinn","Renekton","Rengar","Riven","Rumble","Ryze","Sett","Shen","Singed","Sion","Sylas","TahmKench","Teemo","Trundle","Tryndamere","Urgot","Vladimir","Volibear","Warwick","Yasuo","Yorick","Zac","Lillia","Yone","Gwen"]
jungle=["Amumu","Diana","DrMundo","Ekko","Elise","Evelynn","Fiddlesticks","Gragas","Graves","Hecarim","Ivern","JarvanIV","Jax","Karthus","Kayn","Khazix","Kindred","LeeSin","MasterYi","MonkeyKing","Morgana","Nidalee","Nocturne","Nunu","Olaf","Pantheon","Qiyana","Rammus","RekSai","Rengar","Rumble","Sejuani","Shaco","Shyvana","Skarner","Taliyah","Talon","Trundle","Udyr","Vivi","Volibear","Warwick","XinZhao","Zac","Lillia","Viego"]
mid=["Ahri","Akali","Anivia","Annie","AurelionSol","Azir","Cassiopeia","Corki","Diana","Ekko","Fizz","Galio","Heimerdinger","Irelia","Jayce","Kassadin","Katarina","Leblanc","Lissandra","Lucian","Lux","Malzahar","MonkeyKing","Nocturne","Orianna","Pantheon","Qiyana","Renekton","Rumble","Ryze","Sylas","Syndra","Talon","Tryndamere","TwistedFate","Veigar","Velkoz","Viktor","Vladimir","Xerath","Yasuo","Zed","Ziggs","Zoe","Yone","Akshan"]
bottom=["Aphelios","Ashe","Caitlyn","Draven","Ezreal","Jhin","Jinx","Kaisa","Kalista","KogMaw","Lucian","MissFortune","Senna","Sivir","Tristana","Twitch","Varus","Vayne","Xayah","Ziggs","Samira"]
sup=["Alistar","Amumu","Bard","Blitzcrank","Brand","Braum","Galio","Janna","Karma","Leona","Lulu","Lux","Malphite","Maokai","MissFortune","Morgana","Nami","Nautilus","Neeko","Pyke","Rakan","Senna","Sett","Shen","Sona","Soraka","Swain","TahmKench","Taric","Thresh","Trundle","Veigar","Velkoz","Yuumi","Zilean","Zyra","Seraphine","Rell"]

def BLUE1totalGameCount(championid,other):
    if len(other)==0 and len(championid)==1:
        hi="select count(*) as total from df_game where (T100 like '%"+str(championid[0])+"%') "
        hi2="select count(*) as total1 from df_game where (T200 like '%"+str(championid[0])+"%') "
        curs.execute(hi)
        rows= curs.fetchone()
        curs.execute(hi2)
        rows2= curs.fetchone()
        s= rows[0]+rows2[0]
        return s
def BLUE1winCount(championid,other):
    if len(other)==0 and len(championid)==1:
        hi="select count(*) as total from df_game where (T100 like '%"+str(championid[0])+"%')AND win='100' "
        hi2="select count(*) as total1 from df_game where (T200 like '%"+str(championid[0])+"%')AND win='200' "
        curs.execute(hi)
        rows= curs.fetchone()
        curs.execute(hi2)
        rows2= curs.fetchone()
        s= rows[0]+rows2[0]
        return s
def RED12totalGameCount(championid,other):
    if len(championid) == 1 and len(other) == 1:
        hi="select count(*) as total from df_game where (T100 like '%"+str(championid[0])+"%' and  T200 like '%"+str(other[0])+"%') "
        hi2="select count(*) as total1 from df_game where (T200 like '%"+str(championid[0])+"%' and  T100 like '%"+str(other[0])+"%') "
        curs.execute(hi)
        rows= curs.fetchone()
        curs.execute(hi2)
        rows2= curs.fetchone()
        s= rows[0]+rows2[0]
        return s
def RED12winCount(championid,other):
    if len(championid) == 1 and len(other) == 1:
        hi="select count(*) as total from df_game where (T100 like '%"+str(championid[0])+"%' and  T200 like '%"+str(other[0])+"%')AND win='200' "
        hi2="select count(*) as total1 from df_game where (T200 like '%"+str(championid[0])+"%' and  T100 like '%"+str(other[0])+"%')AND win='100' "
        curs.execute(hi)
        rows= curs.fetchone()
        curs.execute(hi2)
        rows2= curs.fetchone()
        s= rows[0]+rows2[0]
        return s
def BLUE23totalGameCount(championid,other):
    if len(championid) == 2 and len(other) == 2:
        hi="select count(*) as total from df_game where (T100 like '%"+str(championid[0])+"%"+str(championid[1])+"%' or  T100 like '%"+str(championid[1])+"%"+str(championid[0])+"%') and (T200 like '%"+str(other[0])+"%"+str(other[1])+"%' or T200 like '%"+str(other[1])+"%"+str(other[0])+"%') "
        hi2="select count(*) as total1 from df_game where (T200 like '%"+str(championid[0])+"%"+str(championid[1])+"%' or  T200 like '%"+str(championid[1])+"%"+str(championid[0])+"%') and (T100 like '%"+str(other[0])+"%"+str(other[1])+"%' or T100 like '%"+str(other[1])+"%"+str(other[0])+"%') "
        curs.execute(hi)
        rows= curs.fetchone()
        curs.execute(hi2)
        rows2= curs.fetchone()
        s= rows[0]+rows2[0]
        return s
def BLUE23winCount(championid,other):
    if len(championid) == 2 and len(other) == 2:
        hi="select count(*) as total from df_game where (T100 like '%"+str(championid[0])+"%"+str(championid[1])+"%' or  T100 like '%"+str(championid[1])+"%"+str(championid[0])+"%') and (T200 like '%"+str(other[0])+"%"+str(other[1])+"%' or T200 like '%"+str(other[1])+"%"+str(other[0])+"%')AND win='100' "
        hi2="select count(*) as total1 from df_game where (T200 like '%"+str(championid[0])+"%"+str(championid[1])+"%' or  T200 like '%"+str(championid[1])+"%"+str(championid[0])+"%') and (T100 like '%"+str(other[0])+"%"+str(other[1])+"%' or T100 like '%"+str(other[1])+"%"+str(other[0])+"%')AND win='200' "
        curs.execute(hi)
        rows= curs.fetchone()
        curs.execute(hi2)
        rows2= curs.fetchone()
        s= rows[0]+rows2[0]
        return s
def RED34totalGameCount(championid,other):
    hi="select count(*) as total from df_game where (T100 like '%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[2])+"%' or  T100 like '%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[1])+"%'or  T100 like '%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[2])+"%'or  T100 like '%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[0])+"%'or  T100 like '%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[1])+"%'or  T100 like '%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[0])+"%') and (T200 like '%"+str(other[0])+"%"+str(other[1])+"%"+str(other[2])+"%' or T200 like '%"+str(other[0])+"%"+str(other[2])+"%"+str(other[1])+"%'or T200 like '%"+str(other[1])+"%"+str(other[0])+"%"+str(other[2])+"%'or T200 like '%"+str(other[1])+"%"+str(other[2])+"%"+str(other[0])+"%'or T200 like '%"+str(other[2])+"%"+str(other[0])+"%"+str(other[1])+"%'or T200 like '%"+str(other[2])+"%"+str(other[1])+"%"+str(other[0])+"%') "
    hi2="select count(*) as total1 from df_game where (T200 like '%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[2])+"%' or  T200 like '%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[1])+"%'or  T200 like '%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[2])+"%'or  T200 like '%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[0])+"%'or  T200 like '%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[1])+"%'or  T200 like '%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[0])+"%') and (T100 like '%"+str(other[0])+"%"+str(other[1])+"%"+str(other[2])+"%' or T100 like '%"+str(other[0])+"%"+str(other[2])+"%"+str(other[1])+"%'or T100 like '%"+str(other[1])+"%"+str(other[0])+"%"+str(other[2])+"%'or T100 like '%"+str(other[1])+"%"+str(other[2])+"%"+str(other[0])+"%'or T100 like '%"+str(other[2])+"%"+str(other[0])+"%"+str(other[1])+"%'or T100 like '%"+str(other[2])+"%"+str(other[1])+"%"+str(other[0])+"%') "
    curs.execute(hi)
    rows= curs.fetchone()
    curs.execute(hi2)
    rows2= curs.fetchone()
    s= rows[0]+rows2[0]
    return s
def RED34winCount(championid,other):
    hi="select count(*) as total from df_game where (T100 like '%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[2])+"%' or  T100 like '%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[1])+"%'or  T100 like '%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[2])+"%'or  T100 like '%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[0])+"%'or  T100 like '%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[1])+"%'or  T100 like '%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[0])+"%') and (T200 like '%"+str(other[0])+"%"+str(other[1])+"%"+str(other[2])+"%' or T200 like '%"+str(other[0])+"%"+str(other[2])+"%"+str(other[1])+"%'or T200 like '%"+str(other[1])+"%"+str(other[0])+"%"+str(other[2])+"%'or T200 like '%"+str(other[1])+"%"+str(other[2])+"%"+str(other[0])+"%'or T200 like '%"+str(other[2])+"%"+str(other[0])+"%"+str(other[1])+"%'or T200 like '%"+str(other[2])+"%"+str(other[1])+"%"+str(other[0])+"%' )AND win='200' "
    hi2="select count(*) as total1 from df_game where (T200 like '%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[2])+"%' or  T200 like '%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[1])+"%'or  T200 like '%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[2])+"%'or  T200 like '%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[0])+"%'or  T200 like '%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[1])+"%'or  T200 like '%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[0])+"%') and (T100 like '%"+str(other[0])+"%"+str(other[1])+"%"+str(other[2])+"%' or T100 like '%"+str(other[0])+"%"+str(other[2])+"%"+str(other[1])+"%'or T100 like '%"+str(other[1])+"%"+str(other[0])+"%"+str(other[2])+"%'or T100 like '%"+str(other[1])+"%"+str(other[2])+"%"+str(other[0])+"%'or T100 like '%"+str(other[2])+"%"+str(other[0])+"%"+str(other[1])+"%'or T100 like '%"+str(other[2])+"%"+str(other[1])+"%"+str(other[0])+"%') AND win='100' "
    curs.execute(hi)
    rows= curs.fetchone()
    curs.execute(hi2)
    rows2= curs.fetchone()
    s= rows[0]+rows2[0]
    return s
def BLUE45totalGameCount(championid,other):
    hi="select count(*) as total from df_game where (T100 like '%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[3])+"%'     or T100 like '%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[2])+"%'    or  T100 like '%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[3])+"%'    or  T100 like '%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[1])+"%'    or  T100 like '%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[2])+"%'    or  T100 like '%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[1])+"%'     or T100 like '%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[3])+"%'    or  T100 like '%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[2])+"%'    or  T100 like '%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[3])+"%'    or  T100 like '%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[0])+"%'    or  T100 like '%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[0])+"%'     or  T100 like '%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[2])+"%'     or T100 like '%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[3])+"%'    or  T100 like '%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[1])+"%'    or  T100 like '%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[3])+"%'    or  T100 like '%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[0])+"%'    or  T100 like '%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[1])+"%'     or T100 like '%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[0])+"%'    or  T100 like '%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[2])+"%'    or  T100 like '%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[1])+"%'    or  T100 like '%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[2])+"%'    or  T100 like '%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[0])+"%'     or  T100 like '%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[1])+"%'     or  T100 like '%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[0])+"%')     and (T200 like '%"+str(other[0])+"%"+str(other[1])+"%"+str(other[2])+"%"+str(other[3])+"%'     or T200 like '%"+str(other[0])+"%"+str(other[1])+"%"+str(other[3])+"%"+str(other[2])+"%'    or  T200 like '%"+str(other[0])+"%"+str(other[2])+"%"+str(other[1])+"%"+str(other[3])+"%'    or  T200 like '%"+str(other[0])+"%"+str(other[2])+"%"+str(other[3])+"%"+str(other[1])+"%'    or  T200 like '%"+str(other[0])+"%"+str(other[3])+"%"+str(other[1])+"%"+str(other[2])+"%'    or  T200 like '%"+str(other[0])+"%"+str(other[3])+"%"+str(other[2])+"%"+str(other[1])+"%'     or T200 like '%"+str(other[1])+"%"+str(other[0])+"%"+str(other[2])+"%"+str(other[3])+"%'    or  T200 like '%"+str(other[1])+"%"+str(other[0])+"%"+str(other[3])+"%"+str(other[2])+"%'    or  T200 like '%"+str(other[1])+"%"+str(other[2])+"%"+str(other[0])+"%"+str(other[3])+"%'    or  T200 like '%"+str(other[1])+"%"+str(other[2])+"%"+str(other[3])+"%"+str(other[0])+"%'    or  T200 like '%"+str(other[1])+"%"+str(other[3])+"%"+str(other[2])+"%"+str(other[0])+"%'     or  T200 like '%"+str(other[1])+"%"+str(other[3])+"%"+str(other[0])+"%"+str(other[2])+"%'     or T200 like '%"+str(other[2])+"%"+str(other[0])+"%"+str(other[1])+"%"+str(other[3])+"%'    or  T200 like '%"+str(other[2])+"%"+str(other[0])+"%"+str(other[3])+"%"+str(other[1])+"%'    or  T200 like '%"+str(other[2])+"%"+str(other[1])+"%"+str(other[0])+"%"+str(other[3])+"%'    or  T200 like '%"+str(other[2])+"%"+str(other[1])+"%"+str(other[3])+"%"+str(other[0])+"%'    or  T200 like '%"+str(other[2])+"%"+str(other[3])+"%"+str(other[0])+"%"+str(other[1])+"%'     or T200 like '%"+str(other[2])+"%"+str(other[3])+"%"+str(other[1])+"%"+str(other[0])+"%'    or  T200 like '%"+str(other[3])+"%"+str(other[0])+"%"+str(other[1])+"%"+str(other[2])+"%'    or  T200 like '%"+str(other[3])+"%"+str(other[0])+"%"+str(other[2])+"%"+str(other[1])+"%'    or  T200 like '%"+str(other[3])+"%"+str(other[1])+"%"+str(other[0])+"%"+str(other[2])+"%'    or  T200 like '%"+str(other[3])+"%"+str(other[1])+"%"+str(other[2])+"%"+str(other[0])+"%'     or  T200 like '%"+str(other[3])+"%"+str(other[2])+"%"+str(other[0])+"%"+str(other[1])+"%'     or  T200 like '%"+str(other[3])+"%"+str(other[2])+"%"+str(other[1])+"%"+str(other[0])+"%') "
    hi2="select count(*) as total1 from df_game where (T200 like '%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[3])+"%'     or T200 like '%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[2])+"%'    or  T200 like '%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[3])+"%'    or  T200 like '%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[1])+"%'    or  T200 like '%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[2])+"%'    or  T200 like '%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[1])+"%'     or T200 like '%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[3])+"%'    or  T200 like '%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[2])+"%'    or  T200 like '%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[3])+"%'    or  T200 like '%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[0])+"%'    or  T200 like '%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[0])+"%'     or  T200 like '%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[2])+"%'     or T200 like '%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[3])+"%'    or  T200 like '%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[1])+"%'    or  T200 like '%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[3])+"%'    or  T200 like '%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[0])+"%'    or  T200 like '%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[1])+"%'     or T200 like '%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[0])+"%'    or  T200 like '%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[2])+"%'    or  T200 like '%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[1])+"%'    or  T200 like '%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[2])+"%'    or  T200 like '%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[0])+"%'     or  T200 like '%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[1])+"%'     or  T200 like '%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[0])+"%')     and (T100 like '%"+str(other[0])+"%"+str(other[1])+"%"+str(other[2])+"%"+str(other[3])+"%'     or T100 like '%"+str(other[0])+"%"+str(other[1])+"%"+str(other[3])+"%"+str(other[2])+"%'    or  T100 like '%"+str(other[0])+"%"+str(other[2])+"%"+str(other[1])+"%"+str(other[3])+"%'    or  T100 like '%"+str(other[0])+"%"+str(other[2])+"%"+str(other[3])+"%"+str(other[1])+"%'    or  T100 like '%"+str(other[0])+"%"+str(other[3])+"%"+str(other[1])+"%"+str(other[2])+"%'    or  T100 like '%"+str(other[0])+"%"+str(other[3])+"%"+str(other[2])+"%"+str(other[1])+"%'     or T100 like '%"+str(other[1])+"%"+str(other[0])+"%"+str(other[2])+"%"+str(other[3])+"%'    or  T100 like '%"+str(other[1])+"%"+str(other[0])+"%"+str(other[3])+"%"+str(other[2])+"%'    or  T100 like '%"+str(other[1])+"%"+str(other[2])+"%"+str(other[0])+"%"+str(other[3])+"%'    or  T100 like '%"+str(other[1])+"%"+str(other[2])+"%"+str(other[3])+"%"+str(other[0])+"%'    or  T100 like '%"+str(other[1])+"%"+str(other[3])+"%"+str(other[2])+"%"+str(other[0])+"%'     or  T100 like '%"+str(other[1])+"%"+str(other[3])+"%"+str(other[0])+"%"+str(other[2])+"%'     or T100 like '%"+str(other[2])+"%"+str(other[0])+"%"+str(other[1])+"%"+str(other[3])+"%'    or  T100 like '%"+str(other[2])+"%"+str(other[0])+"%"+str(other[3])+"%"+str(other[1])+"%'    or  T100 like '%"+str(other[2])+"%"+str(other[1])+"%"+str(other[0])+"%"+str(other[3])+"%'    or  T100 like '%"+str(other[2])+"%"+str(other[1])+"%"+str(other[3])+"%"+str(other[0])+"%'    or  T100 like '%"+str(other[2])+"%"+str(other[3])+"%"+str(other[0])+"%"+str(other[1])+"%'     or T100 like '%"+str(other[2])+"%"+str(other[3])+"%"+str(other[1])+"%"+str(other[0])+"%'    or  T100 like '%"+str(other[3])+"%"+str(other[0])+"%"+str(other[1])+"%"+str(other[2])+"%'    or  T100 like '%"+str(other[3])+"%"+str(other[0])+"%"+str(other[2])+"%"+str(other[1])+"%'    or  T100 like '%"+str(other[3])+"%"+str(other[1])+"%"+str(other[0])+"%"+str(other[2])+"%'    or  T100 like '%"+str(other[3])+"%"+str(other[1])+"%"+str(other[2])+"%"+str(other[0])+"%'     or  T100 like '%"+str(other[3])+"%"+str(other[2])+"%"+str(other[0])+"%"+str(other[1])+"%'     or  T100 like '%"+str(other[3])+"%"+str(other[2])+"%"+str(other[1])+"%"+str(other[0])+"%') "
    curs.execute(hi)
    rows= curs.fetchone()
    curs.execute(hi2)
    rows2= curs.fetchone()
    s= rows[0]+rows2[0]
    return s
def BLUE45winCount(championid,other):
    hi="select count(*) as total from df_game where (T100 like '%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[3])+"%' or T100 like '%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[2])+"%'or  T100 like '%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[3])+"%'or  T100 like '%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[1])+"%'or  T100 like '%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[2])+"%'or  T100 like '%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[1])+"%' or T100 like '%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[3])+"%'or  T100 like '%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[2])+"%'or  T100 like '%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[3])+"%'or  T100 like '%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[0])+"%'or  T100 like '%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[0])+"%' or  T100 like '%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[2])+"%' or T100 like '%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[3])+"%'or  T100 like '%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[1])+"%'or  T100 like '%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[3])+"%'or  T100 like '%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[0])+"%'or  T100 like '%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[1])+"%' or T100 like '%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[0])+"%'or  T100 like '%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[2])+"%'or  T100 like '%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[1])+"%'or  T100 like '%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[2])+"%'or  T100 like '%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[0])+"%' or  T100 like '%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[1])+"%' or  T100 like '%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[0])+"%') and (T200 like '%"+str(other[0])+"%"+str(other[1])+"%"+str(other[2])+"%"+str(other[3])+"%' or T200 like '%"+str(other[0])+"%"+str(other[1])+"%"+str(other[3])+"%"+str(other[2])+"%'or  T200 like '%"+str(other[0])+"%"+str(other[2])+"%"+str(other[1])+"%"+str(other[3])+"%'or  T200 like '%"+str(other[0])+"%"+str(other[2])+"%"+str(other[3])+"%"+str(other[1])+"%'or  T200 like '%"+str(other[0])+"%"+str(other[3])+"%"+str(other[1])+"%"+str(other[2])+"%'or  T200 like '%"+str(other[0])+"%"+str(other[3])+"%"+str(other[2])+"%"+str(other[1])+"%' or T200 like '%"+str(other[1])+"%"+str(other[0])+"%"+str(other[2])+"%"+str(other[3])+"%'or  T200 like '%"+str(other[1])+"%"+str(other[0])+"%"+str(other[3])+"%"+str(other[2])+"%'or  T200 like '%"+str(other[1])+"%"+str(other[2])+"%"+str(other[0])+"%"+str(other[3])+"%'or  T200 like '%"+str(other[1])+"%"+str(other[2])+"%"+str(other[3])+"%"+str(other[0])+"%'or  T200 like '%"+str(other[1])+"%"+str(other[3])+"%"+str(other[2])+"%"+str(other[0])+"%' or  T200 like '%"+str(other[1])+"%"+str(other[3])+"%"+str(other[0])+"%"+str(other[2])+"%' or T200 like '%"+str(other[2])+"%"+str(other[0])+"%"+str(other[1])+"%"+str(other[3])+"%'or  T200 like '%"+str(other[2])+"%"+str(other[0])+"%"+str(other[3])+"%"+str(other[1])+"%'or  T200 like '%"+str(other[2])+"%"+str(other[1])+"%"+str(other[0])+"%"+str(other[3])+"%'or  T200 like '%"+str(other[2])+"%"+str(other[1])+"%"+str(other[3])+"%"+str(other[0])+"%'or  T200 like '%"+str(other[2])+"%"+str(other[3])+"%"+str(other[0])+"%"+str(other[1])+"%' or T200 like '%"+str(other[2])+"%"+str(other[3])+"%"+str(other[1])+"%"+str(other[0])+"%'or  T200 like '%"+str(other[3])+"%"+str(other[0])+"%"+str(other[1])+"%"+str(other[2])+"%'or  T200 like '%"+str(other[3])+"%"+str(other[0])+"%"+str(other[2])+"%"+str(other[1])+"%'or  T200 like '%"+str(other[3])+"%"+str(other[1])+"%"+str(other[0])+"%"+str(other[2])+"%'or  T200 like '%"+str(other[3])+"%"+str(other[1])+"%"+str(other[2])+"%"+str(other[0])+"%' or  T200 like '%"+str(other[3])+"%"+str(other[2])+"%"+str(other[0])+"%"+str(other[1])+"%' or  T200 like '%"+str(other[3])+"%"+str(other[2])+"%"+str(other[1])+"%"+str(other[0])+"%')AND win='100' "
    hi2="select count(*) as total1 from df_game where (T200 like '%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[3])+"%' or T200 like '%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[2])+"%'or  T200 like '%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[3])+"%'or  T200 like '%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[1])+"%'or  T200 like '%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[2])+"%'or  T200 like '%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[1])+"%' or T200 like '%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[3])+"%'or  T200 like '%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[2])+"%'or  T200 like '%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[3])+"%'or  T200 like '%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[0])+"%'or  T200 like '%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[0])+"%' or  T200 like '%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[2])+"%' or T200 like '%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[3])+"%'or  T200 like '%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[3])+"%"+str(championid[1])+"%'or  T200 like '%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[3])+"%'or  T200 like '%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[3])+"%"+str(championid[0])+"%'or  T200 like '%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[1])+"%' or T200 like '%"+str(championid[2])+"%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[0])+"%'or  T200 like '%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[1])+"%"+str(championid[2])+"%'or  T200 like '%"+str(championid[3])+"%"+str(championid[0])+"%"+str(championid[2])+"%"+str(championid[1])+"%'or  T200 like '%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[0])+"%"+str(championid[2])+"%'or  T200 like '%"+str(championid[3])+"%"+str(championid[1])+"%"+str(championid[2])+"%"+str(championid[0])+"%' or  T200 like '%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[0])+"%"+str(championid[1])+"%' or  T200 like '%"+str(championid[3])+"%"+str(championid[2])+"%"+str(championid[1])+"%"+str(championid[0])+"%') and (T100 like '%"+str(other[0])+"%"+str(other[1])+"%"+str(other[2])+"%"+str(other[3])+"%' or T100 like '%"+str(other[0])+"%"+str(other[1])+"%"+str(other[3])+"%"+str(other[2])+"%'or  T100 like '%"+str(other[0])+"%"+str(other[2])+"%"+str(other[1])+"%"+str(other[3])+"%'or  T100 like '%"+str(other[0])+"%"+str(other[2])+"%"+str(other[3])+"%"+str(other[1])+"%'or  T100 like '%"+str(other[0])+"%"+str(other[3])+"%"+str(other[1])+"%"+str(other[2])+"%'or  T100 like '%"+str(other[0])+"%"+str(other[3])+"%"+str(other[2])+"%"+str(other[1])+"%' or T100 like '%"+str(other[1])+"%"+str(other[0])+"%"+str(other[2])+"%"+str(other[3])+"%'or  T100 like '%"+str(other[1])+"%"+str(other[0])+"%"+str(other[3])+"%"+str(other[2])+"%'or  T100 like '%"+str(other[1])+"%"+str(other[2])+"%"+str(other[0])+"%"+str(other[3])+"%'or  T100 like '%"+str(other[1])+"%"+str(other[2])+"%"+str(other[3])+"%"+str(other[0])+"%'or  T100 like '%"+str(other[1])+"%"+str(other[3])+"%"+str(other[2])+"%"+str(other[0])+"%' or  T100 like '%"+str(other[1])+"%"+str(other[3])+"%"+str(other[0])+"%"+str(other[2])+"%' or T100 like '%"+str(other[2])+"%"+str(other[0])+"%"+str(other[1])+"%"+str(other[3])+"%'or  T100 like '%"+str(other[2])+"%"+str(other[0])+"%"+str(other[3])+"%"+str(other[1])+"%'or  T100 like '%"+str(other[2])+"%"+str(other[1])+"%"+str(other[0])+"%"+str(other[3])+"%'or  T100 like '%"+str(other[2])+"%"+str(other[1])+"%"+str(other[3])+"%"+str(other[0])+"%'or  T100 like '%"+str(other[2])+"%"+str(other[3])+"%"+str(other[0])+"%"+str(other[1])+"%' or T100 like '%"+str(other[2])+"%"+str(other[3])+"%"+str(other[1])+"%"+str(other[0])+"%'or  T100 like '%"+str(other[3])+"%"+str(other[0])+"%"+str(other[1])+"%"+str(other[2])+"%'or  T100 like '%"+str(other[3])+"%"+str(other[0])+"%"+str(other[2])+"%"+str(other[1])+"%'or  T100 like '%"+str(other[3])+"%"+str(other[1])+"%"+str(other[0])+"%"+str(other[2])+"%'or  T100 like '%"+str(other[3])+"%"+str(other[1])+"%"+str(other[2])+"%"+str(other[0])+"%' or  T100 like '%"+str(other[3])+"%"+str(other[2])+"%"+str(other[0])+"%"+str(other[1])+"%' or  T100 like '%"+str(other[3])+"%"+str(other[2])+"%"+str(other[1])+"%"+str(other[0])+"%')AND win='200' "
    curs.execute(hi)
    rows= curs.fetchone()
    curs.execute(hi2)
    rows2= curs.fetchone()
    s= rows[0]+rows2[0]
    return s

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    if request.method == 'POST':
        return render_template('recommend.html')

@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
        return render_template('search.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/youtube', methods=['POST'])
def youtube():
    if request.method == 'POST':
        return render_template('youtube.html')

@app.route("/result", methods=['GET','POST'])
def result():
    if request.method == 'POST':


        # 파라미터를 전달 받습니다.
        team = request.form['team']

        pick = request.form['pick']

        bluecham1 = request.form['bluecham1']
        redcham1 = request.form['redcham1']
        bluecham2 = request.form['bluecham2']
        redcham2 = request.form['redcham2']
        bluecham3 = request.form['bluecham3']
        redcham3= request.form['redcham3']
        bluecham4 = request.form['bluecham4']
        redcham4 = request.form['redcham4']
        position=request.form['position']



        if team=="blue" and pick=="1" and position =="top":
            b=[] # blue 1픽일때 경우
            for i in range(len(top)):
                totalTemp = BLUE1totalGameCount([top[i]],[])
                if(totalTemp==0):
                    continue
                winTemp = BLUE1winCount([top[i]],[])
                s = [top[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<300:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price= b[:5]

        elif team=="blue" and pick=="1" and position=="jungle":
            b=[] # blue 1픽일때 경우
            for i in range(len(jungle)):
                totalTemp = BLUE1totalGameCount([jungle[i]],[])
                if(totalTemp==0):
                    continue
                winTemp = BLUE1winCount([jungle[i]],[])
                s = [jungle[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<300:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price= b[:5]

        elif team=="blue" and pick=="1" and position=="mid":
            b=[] # blue 1픽일때 경우
            for i in range(len(mid)):
                totalTemp = BLUE1totalGameCount([mid[i]],[])
                if(totalTemp==0):
                    continue
                winTemp = BLUE1winCount([mid[i]],[])
                s = [mid[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<300:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price= b[:5]

        elif team=="blue" and pick=="1" and position=="bottom":
            b=[] # blue 1픽일때 경우
            for i in range(len(bottom)):
                totalTemp = BLUE1totalGameCount([bottom[i]],[])
                if(totalTemp==0):
                    continue
                winTemp = BLUE1winCount([bottom[i]],[])
                s = [bottom[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<300:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price= b[:5]

        elif team=="blue" and pick=="1" and position=="sup":
            b=[] # blue 1픽일때 경우
            for i in range(len(sup)):
                totalTemp = BLUE1totalGameCount([sup[i]],[])
                if(totalTemp==0):
                    continue
                winTemp = BLUE1winCount([sup[i]],[])
                s = [sup[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<300:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price= b[:5]

        elif team=="red" and (pick=="1" or pick=="2") and position =="top": # red 1,2픽일때 경우
            b=[]
            for i in range(len(top)):
                totalTemp = RED12totalGameCount([bluecham1],[top[i]])
                if(totalTemp==0):
                    continue
                winTemp = RED12winCount([bluecham1],[top[i]])
                s = [top[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<300:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price= b[:5]

        elif team=="red" and (pick=="1" or pick=="2") and position =="jungle": # red 1,2픽일때 경우
            b=[]
            for i in range(len(jungle)):
                totalTemp = RED12totalGameCount([bluecham1],[jungle[i]])
                if(totalTemp==0):
                    continue
                winTemp = RED12winCount([bluecham1],[jungle[i]])
                s = [jungle[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<300:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price= b[:5]

        elif team=="red" and (pick=="1" or pick=="2") and position =="mid": # red 1,2픽일때 경우
            b=[]
            for i in range(len(mid)):
                totalTemp = RED12totalGameCount([bluecham1],[mid[i]])
                if(totalTemp==0):
                    continue
                winTemp = RED12winCount([bluecham1],[mid[i]])
                s = [mid[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<300:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price= b[:5]

        elif team=="red" and (pick=="1" or pick=="2") and position =="bottom": # red 1,2픽일때 경우
            b=[]
            for i in range(len(bottom)):
                totalTemp = RED12totalGameCount([bluecham1],[bottom[i]])
                if(totalTemp==0):
                    continue
                winTemp = RED12winCount([bluecham1],[bottom[i]])
                s = [bottom[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<300:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price= b[:5]

        elif team=="red" and (pick=="1" or pick=="2") and position =="sup": # red 1,2픽일때 경우
            b=[]
            for i in range(len(sup)):
                totalTemp = RED12totalGameCount([bluecham1],[sup[i]])
                if(totalTemp==0):
                    continue
                winTemp = RED12winCount([bluecham1],[sup[i]])
                s = [sup[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<300:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price= b[:5]
            

        elif team=="blue" and (pick=="2" or pick=="3") and position == "top": # blue 2,3픽 일 경우
            b=[]
            for i in range(len(top)):
                totalTemp = BLUE23totalGameCount([top[i],bluecham1],[redcham1,redcham2])
                if(totalTemp==0):
                    continue
                winTemp = BLUE23winCount([bluecham1,top[i]],[redcham1,redcham2])
                s = [top[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<100:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5]


        elif team=="blue" and (pick=="2" or pick=="3") and position == "jungle": # blue 2,3픽 일 경우
            b=[]
            for i in range(len(jungle)):
                totalTemp = BLUE23totalGameCount([jungle[i],bluecham1],[redcham1,redcham2])
                if(totalTemp==0):
                    continue
                winTemp = BLUE23winCount([bluecham1,jungle[i]],[redcham1,redcham2])
                s = [jungle[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<100:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5]


        elif team=="blue" and (pick=="2" or pick=="3") and position == "mid": # blue 2,3픽 일 경우
            b=[]
            for i in range(len(mid)):
                totalTemp = BLUE23totalGameCount([mid[i],bluecham1],[redcham1,redcham2])
                if(totalTemp==0):
                    continue
                winTemp = BLUE23winCount([bluecham1,mid[i]],[redcham1,redcham2])
                s = [mid[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<100:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5]


        elif team=="blue" and (pick=="2" or pick=="3") and position == "bottom": # blue 2,3픽 일 경우
            b=[]
            for i in range(len(bottom)):
                totalTemp = BLUE23totalGameCount([bottom[i],bluecham1],[redcham1,redcham2])
                if(totalTemp==0):
                    continue
                winTemp = BLUE23winCount([bluecham1,bottom[i]],[redcham1,redcham2])
                s = [bottom[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<100:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5]

        elif team=="blue" and (pick=="2" or pick=="3") and position == "sup": # blue 2,3픽 일 경우
            b=[]
            for i in range(len(sup)):
                totalTemp = BLUE23totalGameCount([sup[i],bluecham1],[redcham1,redcham2])
                if(totalTemp==0):
                    continue
                winTemp = BLUE23winCount([bluecham1,sup[i]],[redcham1,redcham2])
                s = [sup[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<100:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5]


        elif team=="red" and (pick=="3" or pick=="4") and position == "top": # red 3,4픽 일 경우
            b=[]
            for i in range(len(top)):
                totalTemp = RED34totalGameCount([bluecham1,bluecham2,bluecham3],[redcham1,redcham2,top[i]])
                if(totalTemp==0):
                    continue
                winTemp = RED34winCount([bluecham1,bluecham2,bluecham3],[redcham1,redcham2,top[i]])
                s = [top[i],winTemp/totalTemp,totalTemp,winTemp]
                
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5]

        elif team=="red" and (pick=="3" or pick=="4") and position == "jungle": # red 3,4픽 일 경우
            b=[]
            for i in range(len(jungle)):
                totalTemp = RED34totalGameCount([bluecham1,bluecham2,bluecham3],[redcham1,redcham2,jungle[i]])
                if(totalTemp==0):
                    continue
                winTemp = RED34winCount([bluecham1,bluecham2,bluecham3],[redcham1,redcham2,jungle[i]])
                s = [jungle[i],winTemp/totalTemp,totalTemp,winTemp]
                
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5]

        elif team=="red" and (pick=="3" or pick=="4") and position == "mid": # red 3,4픽 일 경우
            b=[]
            for i in range(len(mid)):
                totalTemp = RED34totalGameCount([bluecham1,bluecham2,bluecham3],[redcham1,redcham2,mid[i]])
                if(totalTemp==0):
                    continue
                winTemp = RED34winCount([bluecham1,bluecham2,bluecham3],[redcham1,redcham2,mid[i]])
                s = [mid[i],winTemp/totalTemp,totalTemp,winTemp]
                
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5]

        elif team=="red" and (pick=="3" or pick=="4") and position == "bottom": # red 3,4픽 일 경우
            b=[]
            for i in range(len(bottom)):
                totalTemp = RED34totalGameCount([bluecham1,bluecham2,bluecham3],[redcham1,redcham2,bottom[i]])
                if(totalTemp==0):
                    continue
                winTemp = RED34winCount([bluecham1,bluecham2,bluecham3],[redcham1,redcham2,bottom[i]])
                s = [bottom[i],winTemp/totalTemp,totalTemp,winTemp]
                
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5]

        elif team=="red" and (pick=="3" or pick=="4") and position == "sup": # red 3,4픽 일 경우
            b=[]
            for i in range(len(sup)):
                totalTemp = RED34totalGameCount([bluecham1,bluecham2,bluecham3],[redcham1,redcham2,sup[i]])
                if(totalTemp==0):
                    continue
                winTemp = RED34winCount([bluecham1,bluecham2,bluecham3],[redcham1,redcham2,sup[i]])
                s = [sup[i],winTemp/totalTemp,totalTemp,winTemp]
                
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5]


            
        elif team=="blue" and (pick=="4" or pick=="5") and position == "top": # blue 4,5픽 일 경우
            b=[]
            for i in range(len(top)):
                totalTemp = BLUE45totalGameCount([bluecham1,bluecham2,bluecham3,top[i]],[redcham1,redcham2,redcham3,redcham4])
                if(totalTemp==0):
                    continue
                winTemp = BLUE45winCount([bluecham1,bluecham2,bluecham3,top[i]],[redcham1,redcham2,redcham3,redcham4])
                s = [top[i],winTemp/totalTemp,totalTemp,winTemp]
                #if s[2]<50:
                 #   continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5]

        elif team=="blue" and (pick=="4" or pick=="5") and position == "jungle": # blue 4,5픽 일 경우
            b=[]
            for i in range(len(jungle)):
                totalTemp = BLUE45totalGameCount([bluecham1,bluecham2,bluecham3,jungle[i]],[redcham1,redcham2,redcham3,redcham4])
                if(totalTemp==0):
                    continue
                winTemp = BLUE45winCount([bluecham1,bluecham2,bluecham3,jungle[i]],[redcham1,redcham2,redcham3,redcham4])
                s = [jungle[i],winTemp/totalTemp,totalTemp,winTemp]
                #if s[2]<50:
                 #   continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5]   

        elif team=="blue" and (pick=="4" or pick=="5") and position == "mid": # blue 4,5픽 일 경우
            b=[]
            for i in range(len(mid)):
                totalTemp = BLUE45totalGameCount([bluecham1,bluecham2,bluecham3,mid[i]],[redcham1,redcham2,redcham3,redcham4])
                if(totalTemp==0):
                    continue
                winTemp = BLUE45winCount([bluecham1,bluecham2,bluecham3,mid[i]],[redcham1,redcham2,redcham3,redcham4])
                s = [mid[i],winTemp/totalTemp,totalTemp,winTemp]
                #if s[2]<50:
                 #   continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5]

        elif team=="blue" and (pick=="4" or pick=="5") and position == "bottom": # blue 4,5픽 일 경우
            b=[]
            for i in range(len(bottom)):
                totalTemp = BLUE45totalGameCount([bluecham1,bluecham2,bluecham3,bottom[i]],[redcham1,redcham2,redcham3,redcham4])
                if(totalTemp==0):
                    continue
                winTemp = BLUE45winCount([bluecham1,bluecham2,bluecham3,bottom[i]],[redcham1,redcham2,redcham3,redcham4])
                s = [bottom[i],winTemp/totalTemp,totalTemp,winTemp]
                #if s[2]<50:
                 #   continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5] 

        elif team=="blue" and (pick=="4" or pick=="5") and position == "sup": # blue 4,5픽 일 경우
            b=[]
            for i in range(len(sup)):
                totalTemp = BLUE45totalGameCount([bluecham1,bluecham2,bluecham3,sup[i]],[redcham1,redcham2,redcham3,redcham4])
                if(totalTemp==0):
                    continue
                winTemp = BLUE45winCount([bluecham1,bluecham2,bluecham3,sup[i]],[redcham1,redcham2,redcham3,redcham4])
                s = [sup[i],winTemp/totalTemp,totalTemp,winTemp]
                if s[2]<50:
                    continue
                b.append(s)
            b.sort(key=itemgetter(1),reverse=True)
            price=b[:5]
                               
                   
    return render_template('result.html',price=price)


@app.route("/character", methods=['GET','POST'])
def character():
    if request.method == 'POST':
        Name = request.form['Name']

        hdr = {'Accept-Language': 'ko_KR,en;q=0.8', 'User-Agent': (
            'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Mobile Safari/537.36')}
        Container = {}
        SummonerName = ""
        Ranking = ""
        Tier = []
        LP = []
        Wins = []
        Losses = []
        Ratio = []

        # url 요청
        url = 'https://www.op.gg/summoner/userName=' + Name
        req = requests.get(url, headers=hdr)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        # 여기서부터 크롤링
        # 크롤링 후에는 Container 변수에 담아서 저장
        for i in soup.select('div[class=SummonerName]'):
            SummonerName = i.text
        Container['SummonerName'] = SummonerName

        for i in soup.select('span[class=ranking]'):
            Ranking = i.text
        Container['Ranking'] = Ranking

        for j in soup.select('div[class=Tier]'):
            Tier.append(j.text.strip())
        Container['Tier'] = Tier

        for i in soup.select('div[class=LP]'):
            LP.append(i.text)
        Container['LP'] = LP

        for i in soup.select('span[class=Wins]'):
            if len(Wins) >= len(Tier):
                break
            Wins.append(i.text)
        Container['Wins'] = Wins

        for i in soup.select('span[class=Losses]'):
            if len(Losses) >= len(Tier):
                break
            Losses.append(i.text)
        Container['Losses'] = Losses

        for i in soup.select('span[class=Ratio]'):
            Ratio.append(i.text)
        Container['Ratio'] = Ratio



        # 모스트챔피언
        most_champion = soup.select('div.MostChampionContent div.ChampionBox', limit = 3)
        most_champion_list = []
        
        for champ in most_champion:
            champ_info = champ.select_one('div.ChampionInfo')
            champ_name = champ_info.select_one('div.ChampionName').attrs['title']

            champ_minon_kill = re.sub('(\n|\t)', '', champ_info.select_one('div.ChampionMinionKill').text).split(' ')
            avr_CS = champ_minon_kill[1]
            minute_CS = re.sub('(\(|\))', '', champ_minon_kill[2])

            persnal_kda = champ.select_one('div.PersonalKDA')
            kda = persnal_kda.select_one('div.KDA span.KDA').text
            kill = persnal_kda.select_one('div.KDAEach span.Kill').text
            death = persnal_kda.select_one('div.KDAEach span.Death').text
            assist = persnal_kda.select_one('div.KDAEach span.Assist').text

            champ_winratio = re.sub('(\n|\t)', '', champ.select_one('div.Played div.WinRatio').text)
            champ_play_count = champ.select_one('div.Played div.Title').text.replace(' Played', '')

            most_champ = {
            "ChampionName": champ_name, 
            "AverageCS": float(avr_CS), 
            "CSperMinute": float(minute_CS), 
            "KDA": kda, 
            "Kill": float(kill), 
            "Death": float(death), 
            "Assist": float(assist), 
            "ChampionWinRatio": champ_winratio, 
            "ChampionPlayCount": champ_play_count
            }
            most_champion_list.append(most_champ)

        Container['Most'] = most_champion_list

        # 최근 20경기 평균 kill, death, assist 크롤링
        recent20_kill = soup.select_one('div.KDA > span.Kill').text
        recent20_death = soup.select_one('div.KDA > span.Death').text
        recent20_assist = soup.select_one('div.KDA > span.Assist').text

        Container['Recent_20_Kill_Average'] = recent20_kill
        Container['Recent_20_Death_Average'] = recent20_death
        Container['Recent_20_Assist_Average'] = recent20_assist




        stock_list2=list(Container.values())
        Container1=stock_list2[7][2] #바꿀거    
        stock_list3=list(Container1.values())#바꿀거
        c=stock_list3[1]#바꿀거
        SummonerName= stock_list2[0]
        Tier=stock_list2[2][0]
        win=stock_list2[4][0]
        loss=stock_list2[5][0]
        winrate=stock_list2[6][0] 
        Most=stock_list2[7][0]
        Most1=stock_list2[7][1]
        Most2=stock_list2[7][2]
        Most=list(Most.values())
        Most1=list(Most1.values())
        Most2=list(Most2.values())
        Recent_20_Kill_Average=float(stock_list2[8])
        Recent_20_Death_Average=float(stock_list2[9])
        Recent_20_Assist_Average=float(stock_list2[10])
        if Recent_20_Kill_Average>=7:
            a= "W1Klze"
        elif Recent_20_Kill_Average<=5 and Recent_20_Assist_Average >=10:
            a="xNkX2M"
        else:
            a="NrujSE"

        return render_template('character.html',c=c,a=a,Most=Most,Most1=Most1,Most2=Most2,Tier=Tier,SummonerName=SummonerName,win=win,loss=loss,winrate=winrate)





if __name__ == '__main__':

   app.run(debug = True)