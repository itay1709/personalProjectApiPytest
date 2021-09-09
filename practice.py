import random
import string

import requests

from configuration import getConfig
from resources.getBook import getBookResource

"""
response = requests.post(getConfig()['API']['host']+'/Library/Addbook.php', json={
                             "name":"Learn Appium Automation with Java",
                            "isbn":"itay",
                            "aisle":"1986",
                            "author":"Itay Zis"
                            },)
responseJson = response.json()
print(responseJson['msg'])
print(''.join(random.choice(string.ascii_lowercase) for i in range(10)))
assert responseJson['msg'] == 'Add Book operation failed, looks like the book already exists'
"""
response = requests.get(getConfig()['API']['host']+getBookResource, params={'AuthorName': 'i'},)
responseJson = response.json()
bookName = []
#print(len(responseJson))

#1: list
#2:
for index in range(len(responseJson)):
    for key in responseJson[index].keys():
        if key == "book_name":
            print(responseJson[index][key])
