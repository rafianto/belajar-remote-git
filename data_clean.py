# Pembelajaran Python Connection
import psycopg2
import pandas as pd
import pandas.io.sql as psql
import seaborn as sns
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

    data = pd.read_sql('select * from public.crash',conn)
 
    korelasi = data.corr();
    print(korelasi)
 
    smp = sns.heatmap(korelasi)
    plt.show()
    
    conn.close()   
except Exception as error:
    print(error)