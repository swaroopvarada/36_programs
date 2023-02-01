from flask import Flask,request
import psycopg2

app = Flask(__name__)
# Connect to the database
conn = psycopg2.connect(host = 'localhost' , database ='postgres' ,
                            port= '5432', user ='postgres' , password ='database')              #connection for postgresql
cur = conn.cursor()

@app.route('/create_table', methods = ['POST','GET'])               
def create_tables(): 
    try:
        cur.execute("drop table IF EXISTS player")                  
        command = " create table player (Name varchar(20),Age int, Location varchar(20))"                   
        cur.execute(command)
        print('Table created')
    except Exception as error:
        print(error)
    return 'TABLE CREATED'

@app.route("/player1",methods = ['POST','GET'])              
def player1():
    try: 
        # Execute an INSERT statement with placeholders
        cur.execute('insert into player(Name,Age,Location)'
            'values (%s, %s,%s)',
            ('Dhoni', 38,'Ranchi'))
        print('Dhoni')
    except Exception as error:
        print(error)
    return 'player1 details'

@app.route("/player2",methods = ['POST','GET'])
def player2():
    try: 
        # Execute an INSERT statement with placeholders   
        cur.execute('insert into player(Name,Age,Location)'
                'values (%s,%s, %s)',
                ('Rohit', 35,'Nagpur'))
        print("Rohit")
    except Exception as error:
        print(error)
    return 'player2 details'
    
@app.route("/player3",methods = ['POST','GET'])
def player3():
    try:
        # Execute an INSERT statement with placeholders
        cur.execute('insert into player(Name,Age,Location)'
            'values (%s, %s,%s)',
            ('Kohli',34,'Delhi'))
        print('Kholi') 
    except Exception as error:
        print(error)
    return 'player3 details'

if __name__ == '__main__':
   app.run(debug = True)
#commiting all transactions made
conn.commit()
# Close the cursor
conn.close()