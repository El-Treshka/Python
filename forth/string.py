
# String that can have only 50 chars
class String(str):
    def __new__(cls, string: str):
        if len(string) != 50:
            raise Exception()
        return super().__new__(cls, string)
