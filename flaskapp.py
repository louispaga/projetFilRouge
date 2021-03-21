#
#   Projet Fil Rouge 
#
#files upload project
#Louis Paganin Mastère Spé SIO CentraleSupélec
#
#app script

from flask import Flask, request, send_from_directory, jsonify
from flask_restful import Api, Resource, abort
import my_methods
import CONST
from PIL import Image
import piexif
import os
import json

#create an instance of the class
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = CONST.REPO_PATH
api = Api(app)

class upload(Resource):
    
    def post(self):  
        if 'data' not in request.files:
            return {"error": "no data part, note that the file you wish to upload needs to be uploaded under a key named data"}
        data = request.files['data']
        if not my_methods.allowed_file(data.filename):
            return {"error" : "the format is not correct, this API accepts .txt, .pdf, .csv, .jpeg"}
        if data.filename == '':
            return {"error": "no selected file"}
        if data and my_methods.allowed_file(data.filename): 
            #we extract the file's extension
            extension = data.filename.rsplit('.', 1)[1].lower()
            #we save the file temporary to facilitate manipulation
            data.save(os.path.join(app.config['UPLOAD_FOLDER'], data.filename))
            path = app.config['UPLOAD_FOLDER'] + data.filename
            
            json_object = my_methods.getMetaDataAndData(path, extension)
            
            return json_object
            
        else: return {"error"}
    
api.add_resource(upload, "/upload")

#run the app
if __name__ == '__main__':
    #CONST.CURRENT_DIRECTORY = os.getcwd()
    print("the current path working directory is : " + CONST.CURRENT_DIRECTORY)
    app.run(host=CONST.ADRESS, port=CONST.PORT)
