class Contact:
    def set_name(self, name: str):
        self.__name = name

    def set_about(self, about: str):
        self.__about = about

    def set_mobile_number(self, mobile_number: str):
        self.__mobile_number = mobile_number

    def set_personal_number(self, personal_number: str):
        self.__personal_number = personal_number

    def get_name(self) -> str:
        return self.__name

    def get_about(self) -> str:
        return self.__about

    def get_mobile_number(self) -> str:
        return self.__mobile_number

    def get_personal_number(self) -> str:
        return self.__personal_number
