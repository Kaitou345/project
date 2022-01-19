import base64
from io import BytesIO
import json
from flask import Flask, request
from PIL import Image
import cita as ct
from cita import cita
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

class Register(Resource):
  def post(self):
    image = request.files.get("img1")
    pimg = Image.open(image)
    pimg.show()
    return request.form


class Check(Resource):
  def post(self):



api.add_resource(Register, "/register")



if __name__=="__main__":
  app.run(debug=True, port=5000)
