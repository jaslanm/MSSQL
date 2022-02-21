import pandas as pd
import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=RON\SQLEXPRESS;'
                      'Database=test_database;'
                      'Trusted_Connection=yes;')

sql_query = pd.read_sql_query(''' 
                              select * from test_database.dbo.product
                              '''
                              ,conn) # here, the 'conn' is the variable that contains your database connection information from step 2

df = pd.DataFrame(sql_query)
df.to_csv (r'C:\Users\Ron\Desktop\exported_data.csv', index = False) # place 'r' before the path name