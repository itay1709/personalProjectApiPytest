import requests

from configuration import *
from resources.addBook import *


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

