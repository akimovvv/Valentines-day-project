class User:
    def __init__(self, phone, cur = 0, max = 2):
        self.__phone = phone
        self.__cur = cur
        self.__max = max

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def cur(self):
        return self.__cur

    @cur.setter
    def cur(self, cur):
        self.__cur = cur

    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, phone):
        self.__max = max

class Wishes:
    def __init__(self, text, sender_id, recipient_id):
        self.__text = text
        self.__sender_id = sender_id
        self.__recipient_id = recipient_id

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self,text):
        self.__text = text

    @property
    def sender_id(self):
        return self.__sender_id

    @sender_id.setter
    def sender_id(self, sender_id):
        self.__sender_id = sender_id

    @property
    def recipient_id(self):
        return self.__recipient_id

    @text.setter
    def text(self, recipient_id):
        self.__recipient_id = recipient_id