# Simple Library Management demo (console)
books = [{'id':1,'title':'Harry Potter','available':True},{'id':2,'title':'1984','available':True}]
def checkout(book_id):
    for b in books:
        if b['id']==book_id and b['available']:
            b['available']=False; return True
    return False
if __name__=='__main__':
    print('Books before:', books)
    print('Checkout 1 ->', checkout(1))
    print('Books after:', books)
