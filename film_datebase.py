import sqlite3
from sqlite3 import Error
import os
from pprint import pprint
import json

database = os.path.join(os.getcwd(), "film1.db")
print(database)
try:
    conn = sqlite3.connect(database)
except Error as e:
    print(e)
# Creating a cursor to execute commands (queries)

curs = conn.cursor()

select = """SELECT* FROM film 
            where title like 'B%'
            order by length desc"""

result = curs.execute(select)
pprint(result.fetchone())
pprint(result.fetchall())


select1 = """select* from film"""

result1 = curs.execute(select1)
json_data = result1.fetchall()
new_list = []
for item in json_data:
    dict_ = {"id": item[0], "title": item[1], "description": item[2], "release_year":item[3], "rate":item[4], "length": item[5],"special_features":item[6]}
    new_list.append(dict_)
print(new_list)
with open("film_json.json", "w") as json_file:
     json.dump(new_list, json_file, indent=4)
