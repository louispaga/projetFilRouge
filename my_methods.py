#
#   Python Project 
#
#Image API rep project
#Louis Paganin Mastère Spé SIO CentraleSupélec
#
#my_methods script

import os
import CONST
import re
import json
import pdfplumber
from PyPDF2 import PdfFileReader
from PIL.ExifTags import TAGS
from PIL import Image

#return True if the image is in the repository, if not return False
def isImage(imageID):
    files = os.listdir(CONST.REPO_PATH)
    for file in files:
        idf, e = os.path.splitext(file)
        if imageID == int(idf):
            return True
    return False

#return image meta data in json format
def getMetaDataAndData(path, extension):
    dic = {"metadata": None, "data": None}
    data = {}
    metadata = {}
    if extension == 'txt':
        f = open(path, "r")
        #we first extract metadata
        metadata["file_name"] = os.path.basename(path).split('.')[0]
        metadata["type"] = "text file (.txt)"
        fulltext = f.read()
        byLines= fulltext.split("\n")
        metadata["number of characters"] =  len(fulltext)
        metadata["number of lines"] =  len(byLines) - 1
        metadata['size'] = os.path.getsize(path)
        dic["metadata"] = metadata
        #then extract data
        dic["data"] = fulltext
        f.close()
        json_object = json.dumps(dic, indent = 4)

    if extension == 'pdf':
        print("pdf" + path)
        f = open(path, "rb")
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        numPages = pdf.getNumPages()
        #we first extract metadata
        metadata["file_name"] = os.path.basename(path).split('.')[0]
        metadata["type"] = "PDF (.pdf)"
        metadata["author"] = information.author
        metadata["title"] = information.title
        metadata["number of pages"] = numPages
        metadata['size'] = os.path.getsize(path)
        print(metadata["size"])
        dic["metadata"] = metadata
        f.close()
        #then extract data
        text = ""
        with pdfplumber.open(path) as pdf:
            for i in range(numPages):
                page = pdf.pages[i]
                text += page.extract_text()
        print(text)
        dic["data"] = text
        json_object = json.dumps(dic, indent = 4)

        
    return json_object


#return the first availiable ID for an image as a string
#gérer chiffre dans nombre
def getAvaiID():
    files = os.listdir(CONST.REPO_PATH)
    ID = 1
    while(True):
        isIdPresent = 0
        ##probleme avec le point
        for file in files:
            idf, e = os.path.splitext(file)
            if ID == int(idf):
                isIdPresent = 1
                break
        if isIdPresent == 0:
            return str(ID)
        ID = ID + 1

def allowed_file(filename):
    print(filename)
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in CONST.ALLOWED_EXTENSIONS

def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled



