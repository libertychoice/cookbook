#!/usr/bin/env python3

import psycopg2
import json
import os

DIR = "recipes"

conn = psycopg2.connect(dbname='cookbook_db', user='db_user', password='1', host='127.0.0.1')
cur = conn.cursor()
for file in os.listdir(DIR):
    # with open(DIR+"/"+file, 'r', encoding='utf-8') as json_data:
    json_data = open(DIR + "/" + file, 'r', encoding='utf-8')
    # print(eval(json_data.read()))
    print(json_data)
    # a = json_data.read()
    r = eval(json_data.read())
    # d = json.load(json_data)
    # info = json.loads(a)
    # print(d)
    values = (
    r['name'], 'masha', r['ingredients'], '1-11-11', r['description'], str(r['category']), str(r['calories']), r['image'])
    print(values)
    #values = ("aa","vv","ss","rr","rrr","ddd","saaa","aaaaa")
    for i in values:
        print(type(i))
    a = "INSERT INTO cookbook_recipe (name, author, ingredients, datetime, description, category, calories, image) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
    print(a)
    cur.execute(a, tuple(values))
# cur.fetchall()
# print(results)
conn.commit()
cur.close()
conn.close()
