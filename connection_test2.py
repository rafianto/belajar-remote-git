# Tugas Akhir : PA.1.3 Tugas utama

import psycopg2 
import pandas as pd
import pandas.io.sql as psql
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

hostname = 'localhost'
database = 'hr'
username = 'hr'
pwd = 'hr'
port_id = 5432

try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    
    
    cur = conn.cursor()
    cur.execute("select distinct c.state_name, "+
        " count(c.consecutive_number) countdata, "+
        " sum(c.number_of_fatalities) fatalities, "+
        " sum(c.number_of_drunk_drivers) drunk_drivers, "+
        " sum(c.number_of_vehicle_forms_submitted_all) vehicle_forms_submit, "+
        " sum(c.number_of_motor_vehicles_in_transport_mvit) number_of_motor_vehicles "+ 
        " from crash c group by c.state_name ")
   
    row = cur.fetchall()
    
    for r in row:
        print(f" id {r[0]}  {r[1]}  {r[2]} {r[3]}")
    
    print("#---------------------------------------")    
    print("conecction to PostgreSQL succes and done")
    
    cur.close() 
    conn.close()
    
except Exception as error:
    print(error)