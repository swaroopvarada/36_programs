import psycopg2
from flask import Flask,request

app = Flask(__name__)          

conn = psycopg2.connect(host = 'localhost' , database ='postgres' ,             
port= '5432', user ='postgres' , password = 'database')                                  

cursor = conn.cursor()                            

@app.route("/")              
def details():
    try:
        cursor.execute('SELECT * from cricbuzz')     
        # Retrieve the results
        result = cursor.fetchall()              
        p = result[2]                            
        print(p)
        print(result)
    except Exception as error:
        print(error)
    return 'excuted'

if __name__ == '__main__':              
    app.run(debug = True)  
#commiting all transactions made         
conn.commit() 
# Close the cursor                  
conn.close()               