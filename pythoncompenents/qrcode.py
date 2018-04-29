#install pypng
#install pyqrcode
import pyqrcode
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify
#from flask.jsonpify import jsonify
from flask import send_file
#db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class generateQRCode(Resource):
    def get(self,userid):
        big_code = pyqrcode.create(userid, error='L', version=27, mode='binary')
        big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
        #big_code.show()
        return send_file("code.png", mimetype='image/png')

userid='0987654321'
print("Generating QRCode")
#generateQRCode(userid)
api.add_resource(generateQRCode, '/generatecode/<userid>') # Route_1


if __name__ == '__main__':
     app.run(port=5002)
