

deleteBookResource = '/Library/DeleteBook.php'


def deleteBookBody(deleteBookID):
    deleteBookBody = {
                        "ID": deleteBookID
                         }
    return deleteBookBody


deleteBookMsgResponse = "book is successfully deleted"
deleteBookFailMsgResponse = "Delete Book operation failed, looks like the book doesnt exists"