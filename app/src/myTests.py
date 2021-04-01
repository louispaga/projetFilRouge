import requests
import json
import unittest
import CONST
from PyPDF2 import PdfFileReader
from requests.auth import HTTPBasicAuth

#TEST_FILES_PATH = CURRENT_DIRECTORY + "/../testFiles/"
auth = HTTPBasicAuth('louis', 'paganin')

textfile = {"file" : open("/home/louis/filRouge/projetFilRouge/testFiles/testtext.txt", "r")}
r=requests.post(CONST.ADRESS_TEST + '/upload', auth=auth, files = textfile)
r = r.json()
print(r)

textfile = {"file" : open("/home/louis/filRouge/projetFilRouge/testFiles/.txt", "r")}
r=requests.post(CONST.ADRESS_TEST + "/upload", auth=auth, files = textfile)
r = r.json()
print(r)

pdf = {"file" : open("/home/louis/filRouge/projetFilRouge/testFiles/testpdf.pdf", "rb") }
r=requests.post(CONST.ADRESS_TEST + "/upload", auth=auth, files = pdf)
r = r.json()
#print(r)

csv = {"file" : open("/home/louis/filRouge/projetFilRouge/testFiles/airtravel.csv", encoding='utf-8') }
r=requests.post(CONST.ADRESS_TEST + "/upload", auth=auth, files = csv)
r = r.json()
#print(r)

jpg = {"file" : open("/home/louis/filRouge/projetFilRouge/testFiles/18.jpeg", 'rb') }
r=requests.post(CONST.ADRESS_TEST + "/upload", auth=auth, files = jpg)
r = r.json()
print(r)