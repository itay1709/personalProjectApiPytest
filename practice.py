import random
import string

import requests

from configuration import getConfig

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