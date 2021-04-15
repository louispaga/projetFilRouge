#
#   Projet Fil Rouge 
#
#files upload project
#Louis Paganin Mastère Spé SIO CentraleSupélec
#
#app script

from flask import Flask, request, send_from_directory, jsonify
from flask_restful import Api, Resource, abort
from flask_swagger_ui import get_swaggerui_blueprint
import os
import json
import my_methods
import CONST
import boto3
import uuid

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
            with open(app.config['UPLOAD_FOLDER'] + 'temp.json', "w") as jsonFile:
                jsonFile.write(json_object)
            #we save the json file into the s3 bucket 
            with open(app.config['UPLOAD_FOLDER'] + 'temp.json', "rb") as jsondata:
                s3 = boto3.client('s3')
                json_name = str(uuid.uuid4())
                #check if the id is already used
                s3.upload_fileobj(jsondata, CONST.BUCKET_NAME,json_name + '.json')
            #we remove the temporary files
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], data.filename))
            os.remove(os.path.join(app.config['UPLOAD_FOLDER'], 'temp.json'))
            
            #we return the json object to the user
            return json_object
            
        else: 
            return {"error" : "the format is not correct, this API accepts .txt, .pdf, .csv, .jpeg"}

class swaggerjson(Resource):

    def get(self):
        f = open(CONST.SWAGGER_PATH + '/../swagger/swagger.json')
        data = json.load(f)
        return data

#run the app
if __name__ == '__main__':
    CONST.CURRENT_DIRECTORY = os.getcwd() 
    REPO_PATH = CONST.CURRENT_DIRECTORY + "/temprepository/"

    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = CONST.REPO_PATH
    api = Api(app)
    api.add_resource(upload, "/upload")
    api.add_resource(swaggerjson, "/swagger.json")

    CONST.SWAGGER_PATH = CONST.CURRENT_DIRECTORY
    print(CONST.SWAGGER_PATH)
    swaggerui_blueprint = get_swaggerui_blueprint(
        '/swagger',
        CONST.API_URL + '/swagger.json',
        config={'app_name': "API FIL ROUGE LOUIS"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix='/swagger')
    app.run(host=CONST.ADRESS, port=CONST.PORT)
