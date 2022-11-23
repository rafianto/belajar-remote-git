# Pembelajaran Python Connection
import psycopg2
import pandas as pd
import pandas.io.sql as psql
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from sqlalchemy import create_engine

hostname = 'localhost'
database = 'datambs'
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

    # engine = create_engine("postgressql:///:memory:", echo=True, future=True)

    fdata = pd.read_sql('select tanggal,branch,supplier,cust_group,productgrp,sales_qty,hna,total_hna from sales2022',conn)
 
    cek1 = fdata.head()
    # cek korelasi data
    korelasi = fdata.corr();
    print(korelasi)
    print(fdata.info())
    # cek korelasi 
    smp = sns.heatmap(korelasi)
    #sns.boxplot(x='supplier',data=korelasi)
    plt.show()
   
    #menentukan q1,q3 batas bawah, batas atas dan selisih q3-q1 
    #cek outlier data
    q1,q3 = np.percentile(fdata['total_hna'], [25,75])
    s1 = q3-q1
    ba1 = q3+(1.5*s1) 
    bw1 = q1-(1.5*s1)
    print(q1)
    print(q3)
    print(s1)
    print(ba1)
    print(bw1)
    
    
    conn.close()   
except Exception as error:
    print(error)