import random
import string

import requests
from schema import Schema
from resources.addBook import addBookExistBookBody
from configuration import getConfig
from resources.getBook import *


class TestGetBook:

    def test_validateAuthBookName(self):
        response = requests.get(getConfig()['API']['host']+getBookResource, params={'AuthorName': 'zis'},)
        responseJson = response.json()
        for index in range(len(responseJson)):
            for key in responseJson[index].keys():
                if key == "book_name":
                    assert responseJson[index][key] == "Learn Appium Automation with Java"

    def test_validateGetBookAuthSchema(self):
        response = requests.get(getConfig()['API']['host']+getBookResource, params={'AuthorName': 'zis'},)
        responseJson = response.json()
        assert getBookByNameSchema.validate(responseJson)

    def test_validateGetBookIdSchema(self):
        response = requests.get(getConfig()['API']['host']+getBookResource, params={'ID': addBookExistBookBody['isbn']+addBookExistBookBody['aisle']},)
        responseJson = response.json()
        assert getBookByIdSchema.validate(responseJson)

    def test_validateGetBookAuthStatusCode(self):
        response = requests.get(getConfig()['API']['host'] + getBookResource, params={'AuthorName': 'zis'}, )
        assert response.status_code == 200

    def test_validateGetBookIdStatusCode(self):
        response = requests.get(getConfig()['API']['host'] + getBookResource,params={'ID': addBookExistBookBody['isbn']+addBookExistBookBody['aisle']},)
        assert response.status_code == 200

    def test_validateGetBookIdNotExistMsg(self):
        response = requests.get(getConfig()['API']['host']+getBookResource, params={'ID': ''.join(random.choice(string.ascii_lowercase) for i in range(4))},)
        responseJson = response.json()
        assert responseJson['msg'] == getBookIdNotExistMsg

    def test_validateGetBookIdNotExistStatusCode(self):
        response = requests.get(getConfig()['API']['host']+getBookResource, params={'ID': ''.join(random.choice(string.ascii_lowercase) for i in range(4))},)
        assert response.status_code == 404