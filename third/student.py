class Student:
    def __init__(self, name: str, last_name: str, age: int, phone_number: str):
        self.__name = name
        self.__last_name = last_name
        self.__age = age
        self.__phone_number = phone_number

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_last_name(self) -> str:
        return self.__last_name

    def set_last_name(self, last_name: str):
        self.__last_name = last_name

    def get_age(self) -> int:
        return self.__age

    def set_age(self, age: int):
        self.__age = age

    def get_phone_number(self) -> str:
        return self.__phone_number

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    def __str__(self):
        return "Student:\n" + \
               "\tName: " + self.__name + \
               "\n\tLast name: " + self.__last_name + \
               "\n\tAge: " + str(self.__age) + \
               "\n\tPhone number: " + self.__phone_number
