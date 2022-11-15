
# Pembelajaran Python Connection
import psycopg2
import pandas as pd
import pandas.io.sql as psql
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

hostname = 'localhost'
database = 'the_look_ecommerce'
username = 'postgres'
pwd = 'sevillas123'
port_id = 5432

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    
    # buat cursor
    cur = conn.cursor()
    cur.execute("select * from leson4_view")
   
    row = cur.fetchall()
    
    for r in row:
        print(f" id {r[0]}  name {r[1]}  email {r[2]} accesorie {r[3]}")
        
    print("conecction succes and done")
    
    cur.close() 
    conn.close()
    
except Exception as error:
    print(error)