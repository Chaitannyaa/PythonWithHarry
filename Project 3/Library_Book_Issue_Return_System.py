class library:

    def __init__(self, bookList):
        self.books = bookList

    def booksAvailable(self):
        print(f"These are the books available in this library: ")
        for i in self.books:
            print("*" + i)

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued '{bookName}' book, Please handle it carefully and return before 30 days")
            self.books.remove(bookName)
        else:
            print("This book is not available currently, Please check again after 30day")

    def returnBook(self, bookName):
        if len(bookName) > 4:
                print(f"You have successfully returned '{bookName}' book, Thank you! Visit Again")
                self.books.append(bookName)
        else:
            print("Please type a valid book name")


class student:
    def requestBook(self):
        self.book = input("Enter the name of book :")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of book :")
        return self.book

centralLib = library(["Amazon Web Services", "Microsoft Azure",
                     "Python Notes", "Kubernetes", "Docker", "Linux Commands"])
student = student()

while True:
    welcomeMsg = '''\n ====== Welcome to Central Library ======
    Please choose an option:
    1. List all the books
    2. Request a book
    3. Add/Return a book
    4. Exit the Library
    '''
    print(welcomeMsg)
    a = int(input("Choose the option to proceed: "))

    if a == 1:
        centralLib.booksAvailable()
    elif a == 2:
        centralLib.borrowBook(student.requestBook())
    elif a == 3:
        centralLib.returnBook(student.returnBook())
    elif a == 4:
        print("Thanks for choosing Central Library. Have a great day ahead!")
        exit()
    else:
        print("Enter the valid choice")
