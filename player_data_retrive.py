import psycopg2
       
conn = psycopg2.connect(host = 'localhost' , database ='postgres' ,             
port= '5432', user ='postgres' , password = 'database')                                  

cursor = conn.cursor()                            

def details():
    try:
        cursor.execute('SELECT * from cricbuzz')     
        # Retrieve the results
        result = cursor.fetchall()
        p = result[3]                            
        print(p,'\n')    
        for row in result:          
            print(row)
    except Exception as error:
        print(error)
 
details()
#commiting all transactions made         
conn.commit()
#close the cursor object 
cursor.close()  
# Close the connection                 
conn.close()  