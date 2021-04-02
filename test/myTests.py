import requests
import json
import os 
from requests.auth import HTTPBasicAuth

ADRESS_SRV =  'https://filrouge.louis.p2021.ajoga.fr'
TEST_FILES_PATH = os.getcwd() + "/testfiles/"
auth = HTTPBasicAuth('louis', 'paganin')

textfile = {"file" : open(TEST_FILES_PATH + "/text.txt", "r") }
r=requests.post(ADRESS_SRV + '/upload', auth=auth, files = textfile)
r = r.json()
print(r)

pdf = {"file" : open(TEST_FILES_PATH + "/testpdf.pdf", "rb") }
r=requests.post(ADRESS_SRV + "/upload", auth=auth, files = pdf)
r = r.json()
print(r)

csv = {"file" : open(TEST_FILES_PATH + "/airtravel.csv", encoding='utf-8') }
r=requests.post(ADRESS_SRV + "/upload", auth=auth, files = csv)
r = r.json()
print(r)

jpg = {"file" : open(TEST_FILES_PATH + "/sanglier_2.jpg", 'rb') }
r=requests.post(ADRESS_SRV + "/upload", auth=auth, files = jpg)
r = r.json()
print(r)

png = {"file" : open(TEST_FILES_PATH + "/cat.png", 'rb') }
r=requests.post(ADRESS_SRV + "/upload", auth=auth, files = png)
r = r.json()
print(r)