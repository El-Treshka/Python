import contact
import json


class Main:
    def __init__(self):
        self.__phone_book = list()
        self.__open_menu()

    def __open_menu(self):
        print("Menu")
        i = int(input("Select operation(1-all contacts, 2-add new contact):"))
        if i == 1:
            self.__show_all_contacts()
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
        self.__show_all_contacts()

    def __show_all_contacts(self):
        print("All contacts")
        for num, val in enumerate(self.__phone_book):
            print("Number: ", num + 1)
            print("\tName: ", val.get_name())
            print("\tMobile number: ", val.get_mobile_number())
            print("\tPersonal number: ", val.get_personal_number())
            print("\tAbout: ", val.get_about())
        i = int(input("Select operation(1-menu, 2-delete contact, 3-export contacts, 4-import contacts):"))
        if i == 1:
            self.__open_menu()
        elif i == 2:
            self.__delete_contact()
        elif i == 3:
            self.__export_contacts()
        elif i == 4:
            self.__import_contacts()
        else:
            self.__show_all_contacts()

    def __delete_contact(self):
        print("Deleting contact")
        i = int(input("Input contact number: ")) - 1
        if i >= 0 & i <= len(self.__phone_book):
            self.__phone_book.pop(i)
        else:
            print("Error")
            self.__show_all_contacts()
        print("Contact deleted")
        self.__show_all_contacts()

    def __export_contacts(self):
        data = {'contacts': []}
        for cont in self.__phone_book:
            data['contacts'].append({
                'name': cont.get_name(),
                'mobile number': cont.get_mobile_number(),
                'personal number': cont.get_personal_number(),
                'about': cont.get_about()
            })
        with open('contacts.json', 'w') as outfile:
            json.dump(data, outfile)
        self.__open_menu()

    def __import_contacts(self):
        with open('contacts.json') as json_file:
            data = json.load(json_file)
            self.__phone_book = list()
            for contacts_list in data['contacts']:
                cont = contact.Contact()
                cont.set_name(contacts_list['name'])
                cont.set_mobile_number(contacts_list['mobile number'])
                cont.set_personal_number(contacts_list['personal number'])
                cont.set_about(contacts_list['about'])
                self.__phone_book.append(cont)
        self.__open_menu()


Main()
