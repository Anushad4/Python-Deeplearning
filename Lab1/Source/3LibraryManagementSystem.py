import sys


class Library:
    def __init__(self, listofbooks):
        self.availablebooks = listofbooks

    def DisplayAvailablebooks(self):
        print("The books we have in our library are as follows:")
        print("================================")
        for book in self.availablebooks:
            print(book)

    def RequestBook(self, requestedBook):
        if requestedBook in self.availablebooks:
            print("The book you requested has now been sanctioned")
            self.availablebooks.remove(requestedBook)
        else:
            print("Sorry the book you have requested is currently not in the library")

    def ReturnBook(self, returnedBook):
        self.availablebooks.append(returnedBook)
        print("Thanks for returning your borrowed book")


class Student:
    def __init__(self,listofstudents):
        self.listofstudents = listofstudents
    def requestBook(self):
        print("Enter the name of the book you'd like to borrow")
        self.book = input()
        return self.book

    def returnBook(self):
        print("Enter the name of the book you'd like to return")
        self.book = input()
        return self.book
class Faculty:
    def __init__(self, listoffaculty):  # this init method is the first method to be invoked when you create an object
        # what attributes does a library in general have? - for now, let's abstract and just say it has availablebooks (we're not going to program the shelves, and walls in!)
        self.listoffaculty = listoffaculty



def main():
    library = Library(["The Last Battle", "The Screwtape letters", "The Great Divorce"])
    faculty = Faculty(["Yugyang Lee","Saria Goudarvzand"])
    student = Student(['SaiKumar',"Neha"])
    Name = input("Please Enter your name ")
    if Name in  student.listofstudents or Name in faculty.listoffaculty:
        print(" You are Validated ")
    else:
        print("You are not authorized to use facilities of library :")
        sys.exit()


    done = False

    while done == False:
        print(""" ======LIBRARY MENU=======
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Exit
                  """)
        choice = int(input("Enter Choice:"))
        if choice == 1:
            library.DisplayAvailablebooks()
        elif choice == 2:
            library.RequestBook(student.requestBook())
        elif choice == 3:
            bookname = input("Enter the book to return ")
            if bookname in library.availablebooks:
                print(" You are returning the wrong Book !. Please Enter the correct Book ")
            else:

                library.ReturnBook(student.returnBook())
        elif choice == 4:
            sys.exit()


main()


