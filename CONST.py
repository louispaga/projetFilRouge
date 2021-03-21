#
#   Python Project 
#
#Image API rep project
#Louis Paganin Mastère Spé SIO CentraleSupélec
#
#const scrypt
import os 

#image extensions the API accepts
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'txt', 'pdf', 'csv'}
#desired thumbnail size 
SIZE_THUMBNAILS = (128,128)
#path to the storage location
CURRENT_DIRECTORY = os.getcwd() 
REPO_PATH = CURRENT_DIRECTORY + "/temprepository/"
TEST_FILES_PATH = CURRENT_DIRECTORY + "/testFiles/"
#IP adress and port to connect to the API
ADRESS = '127.0.0.1'
PORT = 5000
ADRESS_TEST = 'http://127.0.0.1:5000'
