#
#   Projet Fil Rouge 
#
#files upload project
#Louis Paganin Mastère Spé SIO CentraleSupélec
#
#app script

from flask import Flask, request, send_from_directory, jsonify
from flask_restful import Api, Resource, abort
import os
import json
import my_methods
import CONST

#create an instance of the class
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = CONST.REPO_PATH
api = Api(app)

class upload(Resource):
    
    def post(self):  
        if 'file' not in request.files:
            return {"error": "no file part, note that the file you wish to upload needs to be uploaded under a key named file"}
        data = request.files['file']  
        if data.filename == '':
            return {"error": "no selected file"}
        if data and my_methods.allowed_file(data.filename): 
            #we extract the file's extension and name
            extension = data.filename.rsplit('.', 1)[1].lower()
            filename = data.filename.rsplit('.', 1)[0].lower()
            if filename == '':
                return {"error": "no file name"}

            #we save the file temporary to facilitate manipulation
            data.save(os.path.join(app.config['UPLOAD_FOLDER'], data.filename))
            file_path = app.config['UPLOAD_FOLDER'] + data.filename

            #we extract data and meta data and we dump them into a json
            dicUser = {"metadata": None, "data": None}
            dicUser["metadata"], dicUser["data"] = my_methods.getMetaDataAndData(file_path, extension)
            if dicUser["metadata"] != {} or dicUser["data"] != {}:
                json_object = json.dumps(dicUser, indent = 4)
            else:
                json_object = {"error" : "a problem happened while extracting metadata and data"}
            #we save the json_object into a file
            with open(app.config['UPLOAD_FOLDER'] + filename + '.json', "w") as jsonFile:
                jsonFile.write(json_object)
            #we remove the temporary file
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], data.filename))
            
            #we return the json object to the user
            return json_object
            
        else: 
            return {"error" : "the format is not correct, this API accepts .txt, .pdf, .csv, .jpeg"}
    
api.add_resource(upload, "/upload")

#run the app
if __name__ == '__main__':
    app.run(host=CONST.ADRESS, port=CONST.PORT)
