import os
current_directory = os.getcwd()
print(current_directory)

print("-------------------------------------")

import re

#filename = "../files/results.csv"
#file = fopen("./results.csv", “r”);
#filename = "results.csv"
#

filename = "expresion_regular/files/results.csv"

pattern = re.compile(r'^([\d]{4,4})\-.*$')

with open(filename, "r", encoding="utf-8") as f:
    for line in f:
        res = re.match(pattern, line)
        if res:
            print(f"{res.group(1)}\n")
