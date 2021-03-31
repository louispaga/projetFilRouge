#
#   Python Project 
#
#projet fil rouge
#Louis Paganin Mastère Spé SIO CentraleSupélec
#
#const scrypt
import os 

#image extensions the API accepts
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'txt', 'pdf', 'csv'}
#path to the storage location
CURRENT_DIRECTORY = "" 
REPO_PATH = ""
#IP adress and port to connect to the API
ADRESS = '0.0.0.0'
PORT = 5000
#ADRESS_TEST = 'http://filrouge.louis.p2021.ajoga.fr:80'
#ADRESS_TEST = 'http://6hsidkopo9.execute-api.us-east-1.amazonaws.com/starting:80'
ADRESS_TEST = 'http://127.0.0.1:80'
#ADRESS_TEST = 'https://filrouge-gate-away.louis.p2021.ajoga.fr:443'
#ADRESS_TEST =  'https://filrougeapi.louis.p2021.ajoga.fr'
#ADRESS_TEST =  'https://x9j885x924.execute-api.us-east-1.amazonaws.com/prod'
#ADRESS_TEST =  'https://apifilrouge.louis.p2021.ajoga.fr'
#AWS
BUCKET_NAME = 'filrougestorage'
