import requests
import json
import sqlite3

conn = sqlite3.connect("Anime.sqllite3")
cursor = conn.cursor()
url = "https://animechan.vercel.app/api/quotes/anime?"
print(requests.get(url).headers)
title = input("Enter the name of your anime:")
info = {'title': title,'character':'character','quote':'quote'}
r= requests.get(url, params=info)
print(r.status_code)
res = json.loads(r.text)

cursor.execute('''CREATE TABLE IF NOT EXISTS anime(
               anime VARCHAR(50),
               character VARCHAR(50));''')
try:
    cursor.execute("INSERT INTO anime VALUES (?,?,?)", (title, res[0]['character'], res[0]['quote']));
except:
    KeyError
conn.commit()
conn.close()







