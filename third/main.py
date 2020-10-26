import student as s


class Main:
    def __init__(self):
        self.__student_list = list()
        self.__menu()

    def __menu(self):
        print("Menu")
        action = int(input("Input action (1-add student, 2-list of students):"))
        if action == 1:
            self.__add_student()
        elif action == 2:
            self.__view_all()
        else:
            self.__menu()

    def __add_student(self):
        print("Adding student")
        name = str(input("Input name:"))
        last_name = str(input("Input last name:"))
        age = int(input("Input age:"))
        number = str(input("Input number:"))
        student = s.Student(name, last_name, age, number)
        self.__student_list.append(student)
        print("Added", student)
        self.__menu()

    def __view_all(self):
        print("List of students")
        for idx, obj in enumerate(self.__student_list, start=1):
            print("Number", idx, obj)
        action = int(input("Select action (1-delete student, 2-menu, 3-add student):"))
        if action == 1:
            self.__delete_menu()
        elif action == 2:
            self.__menu()
        elif action == 3:
            self.__add_student()
        else:
            self.__view_all()

    def __delete_menu(self):
        print("Deleting student")
        action = int(input("Input student number (0-menu):"))
        if action == 0:
            self.__menu()
        elif 0 < action <= len(self.__student_list):
            self.__student_list.pop(action - 1)
            self.__view_all()
        else:
            self.__delete_menu()


Main()
