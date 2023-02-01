import psycopg2

conn = psycopg2.connect(host = '127.0.0.1' , database ='postgres' ,
       port = '5432', user = 'postgres' , password = 'database')
cur = conn.cursor()
     
cur.execute("DROP TABLE IF EXISTS cricbuzz ")
Table ='CREATE TABLE cricbuzz(Name varchar(100),Age int, Location varchar(100))'
cur.execute(Table)
print('ok')
     
cur.execute('INSERT into cricbuzz(Name,Age,Location)'
            'VALUES (%s, %s, %s)',
            ('Dhoni',
               38,
            'Ranchi'))
print('d1')

cur.execute('INSERT into cricbuzz(Name,Age,Location)'
            'VALUES (%s, %s, %s)',
            ('Rohit',
               35,
            'Nagpur'))
print('d2')
cur.execute('INSERT into cricbuzz(Name,Age,Location)'
            'VALUES (%s, %s, %s)',
            ('Kohli',
               34,
            'Delhi'))
print('d3')
cur.execute('INSERT into cricbuzz(Name,Age,Location)'
            'VALUES (%s, %s, %s)',
            ('Dravid',
               47,
            'Banglore'))
print('d4')
conn.commit()
cur.close()
conn.close()