import mysql.connector as mc
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)
class selectAll(Resource):
    def get(self):
        connection = mc.connect (host = "pillar.ciytc9mjujzp.us-east-2.rds.amazonaws.com",
                         user = "pillar",
                         passwd = "pillar2018",
                         db = "innodb")
        cursor = connection.cursor()
        cursor.execute ("SELECT * FROM innodb.pillar")
        result = cursor.fetchall()

        result = {'data': [dict(zip(tuple (i) ,i)) for i in result]}
        connection.commit()   
        cursor.close()
        connection.close()
        return jsonify(result)

# insert new row
class DonateNew(Resource):
    def get(self):
        sql_command = """INSERT INTO innodb.Persons (UserID, LastName, FirstName,Currency,ShelterID,DonorID,City)
        VALUES ("0988888888","george","john","25XLM","X1","D2","SF");"""
        cursor.execute(sql_command)
        connection.commit()
# udpate existing row
class UpdateMoney(Resource):
    def get(self):
        userid=request.args.get('userid', None)
        currency=request.args.get('currency', None)
        connection = mc.connect (host = "pillar.ciytc9mjujzp.us-east-2.rds.amazonaws.com",
                         user = "pillar",
                         passwd = "pillar2018",
                         db = "innodb")
        cursor = connection.cursor()
        command ="SELECT currency FROM innodb.pillar where UserID='"+userid+"';"
        cursor.execute (command)
    
        result = cursor.fetchall() 
        finalCurr = int(result[0][0].split("XLM")[0])+int(currency)
        sql_command = """SET SQL_SAFE_UPDATES = 0;update innodb.pillar set Currency = '"""+str(finalCurr)+"XLM"+"""' where UserID = '"""+userid+"""' ;"""
        cursor.execute(sql_command,multi=True)

        # never forget this, if you want the changes to be saved:
        connection.commit()   
        cursor.close()
        connection.close()
        return {'status':'success'}
api.add_resource(selectAll, '/selectall') # Route_1
#api.add_resource(Tracks, '/tracks') # Route_2
api.add_resource(UpdateMoney, '/updatemoney/') # Route_3


if __name__ == '__main__':
     app.run(port=5002)
     



