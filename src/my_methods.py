#
#   Python Project 
#
#Image API rep project
#Louis Paganin Mastère Spé SIO CentraleSupélec
#
#my_methods script

import os
import CONST
import json
import csv
import base64
from PyPDF2 import PdfFileReader
from PIL.ExifTags import TAGS
from PIL import Image

#return image meta data in json format
def getMetaDataAndData(path, extension):
    data = {}
    metadata = {}

    if extension == 'txt':
        f = open(path, "r", encoding='utf-8')
        #we first extract metadata
        metadata["file_name"] = os.path.basename(path).split('.')[0]
        metadata["type"] = "text file (.txt)"
        fulltext = f.read()
        byLines= fulltext.split("\n")
        metadata["number of characters"] =  len(fulltext)
        metadata["number of lines"] =  len(byLines) - 1
        metadata['size (bytes)'] = os.path.getsize(path)
        #then extract data
        data = fulltext
        f.close()

    if extension == 'pdf':
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
        metadata['size (bytes)'] = os.path.getsize(path)
        #then we extract data
        pdfencoded = base64.b64encode(f.read()).decode('utf-8')
        data = pdfencoded
        f.close()

    if extension == 'csv':
        f = open(path, encoding='utf-8')
        #we first extract metadata
        metadata["file_name"] = os.path.basename(path).split('.')[0]
        metadata["type"] = "Comma-Separated Values file (.csv)"
        #colones et lignes
        #then extract data
        csvArray = []
        csvReader = csv.DictReader(f) 
        for row in csvReader: 
            csvArray.append(row)
        #traiter l'exeption quand il n'y a pas de nom aux colones
        data = csvArray
        f.close()

    if extension == 'jpeg' or extension == 'jpg': #voir pour gif, png etc.
        im = Image.open(path)
        metadata["file_name"] = os.path.basename(path).split('.')[0]
        metadata["type"] = "jpeg Image (.jpeg)"
        metadata["width"] = im.width
        metadata["height"] = im.height
        im.close()
        #data
        with open(path, "rb") as im:
            img_64 = base64.b64encode(im.read()).decode('utf-8')
            data = img_64

    return metadata, data

def allowed_file(filename):
    print(filename)
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in CONST.ALLOWED_EXTENSIONS

def get_labeled_exif(exif):
    labeled = {}
    for (key, val) in exif.items():
        labeled[TAGS.get(key)] = val

    return labeled



