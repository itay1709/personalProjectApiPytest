import random
import string

addBookResource = '/Library/Addbook.php'

# exist book
addBookExistBookBody = {
                             "name":"Learn Appium Automation with Java",
                            "isbn":"itay",
                            "aisle":"1986",
                            "author":"Itay Zis"
                            }
existBookMsgResponse ='Add Book operation failed, looks like the book already exists'

# new book
addBookNewBookBody = {
                             "name": "Learn Appium Automation with Java",
                            "isbn": ''.join(random.choice(string.ascii_lowercase) for i in range(10)),
                            "aisle": "1986",
                            "author": "Itay Zis"
                            }
newBookMsgResponse = 'successfully added'
newBookIdResponse = addBookNewBookBody['isbn']+addBookNewBookBody['aisle']





