import requests

from configuration import getConfig
from resources.addBook import addBookResource, addBookNewBookBody
from resources.deleteBook import deleteBookResource, deleteBookBody, deleteBookMsgResponse


class TestDeleteBook:

    def test_deleteBookMsg(self):
        responseAddBook = requests.post(getConfig()['API']['host'] + addBookResource, json=addBookNewBookBody, )
        responseAddBookJson = responseAddBook.json()
        response = requests.post(getConfig()['API']['host']+deleteBookResource, json=deleteBookBody(responseAddBookJson['ID']))
        responseJson = response.json()
        assert responseJson['msg'] == deleteBookMsgResponse