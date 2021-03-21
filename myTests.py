import requests
import json
import unittest
import CONST
from PyPDF2 import PdfFileReader
import pdfplumber




textfile = {"data" : open("/home/louis/filRouge/projetFilRouge/test.txt", "r")}
r=requests.post(CONST.ADRESS_TEST + "/upload", files = textfile)
r = r.json()
print(r)


pdf = {"data" : open("/home/louis/filRouge/projetFilRouge/test.pdf", "rb") }
r=requests.post(CONST.ADRESS_TEST + "/upload", files = pdf)
r = r.json()
print(r)