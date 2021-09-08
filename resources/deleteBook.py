

deleteBookResource = '/Library/DeleteBook.php'


def deleteBookBody(deleteBoodID):
    deleteBookBody = {
                        "ID": deleteBoodID
                         }
    return deleteBookBody

deleteBookMsgResponse = "book is successfully deleted"