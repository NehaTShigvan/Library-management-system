'''****Library management system****
Create a library class
display book
lend book - (who owns the book if not present)
add book
return book

HarryLibrary = Library(listofbooks, library_name)


dictionary (books-nameofperson)

create a main function and run an infinite while loop asking
users for their input   '''

#creating a class named library
class Library:
    #creating a constructor to set name of library and list of books
    def __init__(self,bookList, lib_Name):
        self.blist = bookList
        self.l_name = lib_Name
        self.lendDict = {}
        print(f"Welcome to {self.l_name}")

    #method to lend a book to a user
    def LendBook(self,uName): 
        self.displayBook()       
        book = input("Enter the name of the book you want: ")
        if book in self.blist:
            self.lendDict[book] = uName
            self.blist.remove(book)
            print("You can take this book. Please return the book within 7 days.")
        elif book in self.lendDict.keys():
            print("This book is already being used.")   
        else:
            print("Sorry! We don't have this book.")

    
    #method to display books available in the library
    def displayBook(self):
        print(f"We have following books:")
        for i in range(len(self.blist)):
            print(f"{(i+1)}. {self.blist[i]}")

    #method to add a book to the library 
    def addBook(self, uName):
        book = input("Please enter the name of book you want to add to the library:\n")
        self.blist.append(book)
        print(f"Thank you for your contribution {uName}")

    #method to return the book to the library
    def returnBook(self):
        book = input("Enter the name of the book you want to return: ")
        self.lendDict.pop(book)
        self.blist.append(book)
        print("Thank you for returning the book.")


if __name__ == "__main__":
    data_dict = {}
    
    listOfBooks = ["Rich Dad Poor Dad",'Atomic habits','Fear Not Be Strong','Ugly love','Varsity','The Psychology of money']
    user = Library(listOfBooks, 'Read Me Library')
    uName = input("Please enter your name: ")

    #infinite loop asking users for their input
    while(True):
        print("What would you like to do?")
        print('''1. Display books\n2. Lend a book\n3. Add a book to the library\n4. Return a book
choose one of the options from above options and enter the corresponding number: ''')
        num = int(input())
        if num == 1:
            user.displayBook()
        elif num == 2:
            user.LendBook(uName)
        elif num == 3:
            user.addBook(uName)
        elif num == 4:
            user.returnBook()

        yono = input("Do you want to continue?\nEnter y for yes and n for no: ")

        if yono == 'n':
            break
    # print(user.lendDict)   
    print(f"Thank you for visiting {user.l_name}")
