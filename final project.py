class GenerateID:
    id = None

    def __init__(self, id):
        self.id = id

    def get_id(self):
        return self.id


class ClientLabririan(GenerateID):
    full_name = ""
    age = None
    id_number = None

    def __init__(self, id, full_name, age, id_number):
        super().__init__(id)
        self.full_name = full_name
        self.age = age
        self.id_number = id_number

    def get_full_name(self):
        return self.full_name

    def get_age(self):
        return self.age

    def get_id_number(self):
        return self.id_number


class Client(ClientLabririan):
    phone_number = None

    def __init__(self, id, full_name, age, id_number, phone_number):
        super().__init__(id, full_name, age, id_number)
        self.phone_number = phone_number

    def get_phone_number(self):
        return self.phone_number


class Labririan(ClientLabririan):
    employee_type = ""

    def __init__(self, id, full_name, age, id_number, employee_type):
        super().__init__(id, full_name, age, id_number)
        self.employee_type = employee_type

    def get_employee_type(self):
        return self.employee_type


class Book(GenerateID):
    title = ""
    description = ""
    author = ""
    status = ""

    def __init__(self, id, title, description, author, status):
        super().__init__(id)
        self.title = title
        self.description = description
        self.author = author
        self.status = status

    def get_title(self):
        return self.title

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status


class Borrowing_Order(GenerateID):
    date = None
    clint_id = None
    book_id = None
    status = "Active"

    def __init__(self, id, date, clint_id, book_id, status):
        super().__init__(id)
        self.date = date
        self.clint_id = clint_id
        self.book_id = book_id
        self.status = status

    def get_client_id(self):
        return self.clint_id

    def get_book_id(self):
        return self.book_id

    def get_status(self):
        return self.status

clients = []
labririans = []
books = []
borrow_orders = []
books.append(Book(1, "title1", "description1", "author1", "Active"))
books.append(Book(2, "title2", "description2", "author2", "Active"))
books.append(Book(3, "title3", "description3", "author3", "Active"))


def check_client_id(client_id):
    available = False
    for i in range(0, len(clients)):
        if client_id == int(clients[i].get_id()):
            available = True
            break
    return available


def check_book_id(book_id):
    available = False
    for i in range(0, len(books)):
        if book_id == int(books[i].get_id()):
            available = True
            break
    return available


def get_book(book_id):
    for i in range(0, len(books)):
        if book_id == int(books[i].get_id()):
            return books[i]
    return False

def check_book_availablity(book_id):
    for i in range(0, len(books)):
        if book_id == int(books[i].get_id()) and books[i].get_status() == "Active" :
            return books[i]
    return False

def total_borrowed_books():
    count = 0
    for i in range(0, len(books)):
        if books[i].get_status() == "In Active" :
            count = count + 1
    return count

def total_available_books():
    count = 0
    for i in range(0, len(books)):
        if books[i].get_status() == "Active" :
            count = count + 1
    return count

def total_borrowed_orders():
    return len(borrow_orders)

borrow_id = 1
while True:
    input_type = input(
        "Enter 1 to add new client , 2 to add new labririan , 3 to view list of books , 4 if you want to borrow a book , 0 to exit")
    if int(input_type) == 1:
        print("add new clint")
        clients.append(Client(input("add new id "), input("enter your full name "), input("enter your age "),
                              input("enter your id_number "), input("enter your phone_number ")))

    elif int(input_type) == 2:
        print("add new labririan")
        labririans.append(Labririan(input("add new id "), input("enter your full name "), input("enter your age "),
                                    input("enter your id_number "), input("enter your employee_type ")))

    elif int(input_type) == 3:
        print("Select id of book")
        for i in range(0, len(books)):
            print("id = " + str(books[i].get_id()) + " , title = " + books[i].get_title() + " , status = " + books[
                i].get_status() + "\n")

    elif int(input_type) == 4:
        client_id = input("Enter client id")
        book_id = input("Enter client id")
        if not check_client_id(int(client_id)):
            print("The entered client id not found")

        elif not check_book_id(int(book_id)):
            print("The entered client id not found")

        elif not check_book_availablity(int(book_id)):
            print("Sorry , The selected book is not active")


        else:
            borrow_orders.append(Borrowing_Order(borrow_id, "2022", client_id, book_id, "Active"))
            borrow_id = borrow_id + 1
            book = get_book(int(book_id))
            book.set_status("In Active")
            print("Your book has been reserved")

    elif int(input_type) == 0:
        break
    else:
        break


# clients.append(Client(input("add new id "), input("enter your full name "), input("enter your age "),
#                       input("enter your id_number "), input("enter your phone_number ")))

#


print(
    "-------------------------------------- Clients ---------------------------------------------------------------------")
for i in range(0, len(clients)):
    print("name = " + clients[i].get_full_name() + " , id_no = " + clients[i].get_id_number() + " , phone = " + clients[
        i].get_phone_number() + "\n")
print("-----------------------------------------------------------------------------------------------------------")

print(
    "------------------------------------------ labririans -----------------------------------------------------------------")
for i in range(0, len(labririans)):
    print("name = " + labririans[i].get_full_name() + " , id_no = " + labririans[i].get_id_number() + " , phone = " +
          labririans[i].get_employee_type() + "\n")
print("-----------------------------------------------------------------------------------------------------------")

print(
    "------------------------------------------ Books -----------------------------------------------------------------")
for i in range(0, len(books)):
    print("name = " + books[i].get_title() + " Status = "+ books[i].get_status() +"\n")
print("-----------------------------------------------------------------------------------------------------------")

print(
    "------------------------------------------ Borrow Orders -----------------------------------------------------------------")
for i in range(0, len(borrow_orders)):
    print("Client id = " + borrow_orders[i].get_client_id() + " Book id = "+ borrow_orders[i].get_book_id() + " Status = "+borrow_orders[i].get_status() +"\n")
print("-----------------------------------------------------------------------------------------------------------")

print("total_borrowed_books = " + str(total_borrowed_books()))
print("total_available_books = " + str(total_available_books()))
print("total_borrowed_orders = " + str( total_borrowed_orders()))