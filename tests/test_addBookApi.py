import requests
from schema import Schema
from configuration import *
from resources.addBook import *
from resources.deleteBook import *


class TestAddBook:

    def test_addBookExistMsg(self):
        response = requests.post(getConfig()['API']['host']+addBookResource, json=addBookExistBookBody,)
        responseJson = response.json()
        assert responseJson['msg'] == existBookMsgResponse
        assert response.status_code == 404

    def test_addBookNewBookMsg(self):
        response = requests.post(getConfig()['API']['host']+addBookResource, json=addBookNewBookBody,)
        responseJson = response.json()
        assert responseJson['Msg'] == newBookMsgResponse
        assert responseJson['ID'] == newBookIdResponse
        assert response.status_code == 200
        requests.post(getConfig()['API']['host']+deleteBookResource, json=deleteBookBody(responseJson['ID']))  #delete the book

    def test_addBookExistBookSchema(self):
        response = requests.post(getConfig()['API']['host']+addBookResource, json=addBookExistBookBody,)
        responseJson = response.json()
        assert addBookExistBookSchema.validate(responseJson)

    def test_addBookNewBookSchema(self):
        response = requests.post(getConfig()['API']['host']+addBookResource, json=addBookNewBookBody,)
        responseJson = response.json()
        assert addBookNewBookSchema.validate(responseJson)
        requests.post(getConfig()['API']['host'] + deleteBookResource, json=deleteBookBody(responseJson['ID']))


