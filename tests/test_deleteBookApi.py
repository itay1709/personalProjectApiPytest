import requests

from configuration import getConfig
from resources.addBook import addBookResource, addBookNewBookBody
from resources.deleteBook import *


class TestDeleteBook:

    def test_deleteExistBookMsg(self):
        responseAddBook = requests.post(getConfig()['API']['host'] + addBookResource, json=addBookNewBookBody, )  #add new book
        responseAddBookJson = responseAddBook.json()
        response = requests.post(getConfig()['API']['host']+deleteBookResource, json=deleteBookBody(responseAddBookJson['ID']))
        responseJson = response.json()
        assert responseJson['msg'] == deleteBookMsgResponse
        assert response.status_code == 200

    def test_deleteNotExistBookMsg(self):
        response = requests.post(getConfig()['API']['host']+deleteBookResource, json=deleteBookBody("nnlkvlk"))
        responseJson = response.json()
        assert responseJson['msg'] == deleteBookFailMsgResponse
        assert response.status_code == 404