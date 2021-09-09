from schema import Schema

getBookResource = '/Library/GetBook.php'


# search by name
def searchByNameParam(authName):  #input for param name in the query parameter of the API
    name = authName
    return name


getBookByNameSchema = Schema([{
                            "book_name": str,
                            "isbn": str,
                            "aisle": str
                        }])


# search by ID
def searchByIdParam(id):  #input for param name in the query parameter of the API
    bookId = id
    return bookId


getBookByIdSchema = Schema([{
                            "book_name": str,
                            "isbn": str,
                            "aisle": str,
                            "author": str
                        }])

getBookIdNotExistMsg = "The book by requested bookid / author name does not exists!"





# validate not exist ID status code