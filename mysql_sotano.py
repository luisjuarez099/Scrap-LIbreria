import pymysql
import csv
import pandas as pd

data = pd.read_csv(r'LibreriaSotano.csv',encoding='utf-8')
df = pd.DataFrame(data)
#crear objeto de la conexion
con = pymysql.connect(host="localhost",port=3306,user="luisdb",passwd="1234",db="dbsotano")
cursor = con.cursor()
for row in df.itertuples():
    sql = "INSERT INTO libros (Titulo, Autor, Precio) VALUES (%s,%s,%s)"
    val = (row.Titulo,row.Autor,row.Precio)
    print(val)
    cursor.execute(sql,val)
    #print(row.Titulo,row.Autor,row.Precio)
    #print(type(row.Autor))
con.commit() #se guardan los datos
con.close()	