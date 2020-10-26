import contact


class Main:
    def __init__(self):
        self.__phone_book = list()
        self.__open_menu()

    def __open_menu(self):
        print("Menu")
        i = int(input("Select operation(1-all contacts, 2-add new contact):"))
        if i == 1:
            self.__all_contacts()
        elif i == 2:
            self.__add_new_contact()
        else:
            self.__open_menu()

    def __add_new_contact(self):
        print("Adding contact")
        cont = contact.Contact()
        cont.set_name(input("Input name:"))
        cont.set_mobile_number(input("Input mobile number:"))
        cont.set_personal_number(input("Input personal number:"))
        cont.set_about(input("Input about:"))
        self.__phone_book.append(cont)
        self.__all_contacts()

    def __all_contacts(self):
        print("All contacts")
        for num, val in enumerate(self.__phone_book):
            print("Number: ", num + 1)
            print("\tName: ", val.get_name())
            print("\tMobile number: ", val.get_mobile_number())
            print("\tPersonal number:", val.get_personal_number())
            print("\tAbout", val.get_about())
        i = int(input("Select operation(1-menu, 2-delete contact):"))
        if i == 1:
            self.__open_menu()
        elif i == 2:
            self.__delete_contact()
        else:
            self.__all_contacts()

    def __delete_contact(self):
        print("Deleting contact")
        i = int(input("Input contact number: ")) - 1
        if i >= 0 & i <= len(self.__phone_book):
            self.__phone_book.pop(i)
        else:
            print("Error")
            self.__all_contacts()
        print("Contact deleted")
        self.__all_contacts()

Main()
