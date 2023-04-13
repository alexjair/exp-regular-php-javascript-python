import re #Traemos las expresiones regulares
"""
date,home_team,away_team,home_score,away_score,tournament,city,country,neutral
1872-11-30,Scotland,England,0,0,Friendly,Glasgow,Scotland,FALSE
"""
pattern = re.compile(r'^([\d]{4,4})\-\d\d-\d\d,(.+),(.+),(\d+),(\d+),.*$')

#filename = "expresion_regular/files/results.csv"

f = open("expresion_regular/files/results.csv", "r")

for line in f:
  res = re.match(pattern, line)
  if res:
    total = int(res.group(4)) + int(res.group(5))
    if total > 20:
      print(f"Goles: {total} - Fecha:{res.group(1)} | {res.group(2)} [{res.group(4)}] -{res.group(3)} [{res.group(5)}]")

f.close()