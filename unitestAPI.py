#
#   Python Project 
#
#Image API rep project
#Louis Paganin Mastère Spé SIO CentraleSupélec
#
#unit test script 

import requests
import json
import unittest
import CONST

#test images noir et blanc

class testAPI(unittest.TestCase):
    
    #test post jpeg 
    def test_post(self):
        img = {"image" : open(CONST.TEST_FILES_PATH + "test.jpeg", 'rb')}
        r=requests.post(CONST.ADRESS_TEST + "/images", files = img)
        r = r.json()
        self.assertIsNotNone(r["id"])
   
    #test post text file 
    def test_post_text(self):
        img = {"image" : open(CONST.TEST_FILES_PATH + "test.txt", 'rb')}
        r=requests.post(CONST.ADRESS_TEST + "/images", files = img)
        r = r.json()
        self.assertEqual(r['error'],"the format is not correct")

    #test post pdf file 
    def test_post_pdf(self):
        img = {"image" : open(CONST.TEST_FILES_PATH + "test.pdf", 'rb')}
        r=requests.post(CONST.ADRESS_TEST + "/images", files = img)
        r = r.json()
        self.assertEqual(r['error'],"the format is not correct")

    #test post no extension 
    def test_post_no_extension(self):
        img = {"image" : open(CONST.TEST_FILES_PATH + "70", 'rb')}
        r=requests.post(CONST.ADRESS_TEST + "/images", files = img)
        r = r.json()
        self.assertEqual(r['error'],"the format is not correct")
    
    #test get metadata with a picture that does not contain meta data 
    def test_get_no_metadata(self):
        img = {"image" : open(CONST.TEST_FILES_PATH + "70.jpeg", 'rb')}
        r=requests.post(CONST.ADRESS_TEST + "/images", files = img)
        r = r.json()
        r = requests.get(CONST.ADRESS_TEST + "/images/" + r["id"])
        r = r.json()
        test = False
        if r['Name'] != None and r['link'] != None and str(r['metadata']) == "no metadata":
            test = True
        self.assertTrue(test)

    #test get metadata with a picture that does not contain meta data 
    def test_get_metada(self):
        img = {"image" : open(CONST.TEST_FILES_PATH + "isa.jpg", 'rb')}
        r=requests.post(CONST.ADRESS_TEST + "/images", files = img)
        r = r.json()
        r = requests.get(CONST.ADRESS_TEST + "/images/" + r["id"])
        r = r.json()
        test = False
        if r['Name'] != None and r['link'] != None and r['metadata'] != "no metadata":
            test = True
        self.assertTrue(test)
    
    #test get metadata with no ID
    def test_get_metadata_no_id(self):
        r = requests.get(CONST.ADRESS_TEST + "/images/")
        self.assertEqual(str(r),"<Response [404]>")

    #test get thumbnails
    def test_get_thumbnails(self):
        img = {"image" : open(CONST.TEST_FILES_PATH + "test.jpeg", 'rb')}
        r=requests.post(CONST.ADRESS_TEST + "/images", files = img)
        r = r.json()
        r = requests.get(CONST.ADRESS_TEST + "/thumbnails/" + r['id'])
        self.assertEqual(r.headers['Content-Type'], 'image/jpeg')

    #get thumbnail that does not exist
    def test_get_thumbnails_not_exist(self):
        r = requests.get(CONST.ADRESS_TEST + "/thumbnails/" + str(-1))
        self.assertEqual(str(r),"<Response [404]>")
    
    #get thumbnail with letter 
    def test_get_thumbnails_letter(self):
        r = requests.get(CONST.ADRESS_TEST + "/thumbnails/" + "ASZ")
        self.assertEqual(str(r),"<Response [404]>")

    #get thumbnail with no ID
    def test_get_thumbnails_no_id(self):
        r = requests.get(CONST.ADRESS_TEST + "/thumbnails/")
        self.assertEqual(str(r),"<Response [404]>")

if __name__ == '__main__':
    unittest.main()