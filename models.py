import re
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    pattern = r'^\d{10}$'


    def __init__(self, phone):
        if not re.match(self.pattern, phone):
            raise ValueError("Phone should contains 10 digits only")
        self.phone = phone


class Record:
    __phone_not_exists = "Phone does not exist in the list."


    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone):
        if self.__if_phone_exists(self, phone):
            return "Phone exists in the list."
        self.phones.append(phone)
        return "Phone was added."


    def remove_phone(self, phone):
        if self.__if_phone_exists(self, phone):
            self.phones.remove(phone)
            return "Phone was removed."
        return self.__phone_not_exists


    def edit_phone(self, phone, new_phone):
        if self.__if_phone_exists(self, phone):
            self.phones.remove(phone)
            self.phones.append(new_phone)
            return "Phone was edited."
        return self.__phone_not_exists


    def find_phone(self, phone):
        if self.__if_phone_exists(self, phone):
            return phone
        return self.__phone_not_exists


    def __if_phone_exists(self, phone):
        return phone in self.phones
        

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    __name_not_exists = "Name not exists in the Address Book."
    

    def add_record(self, data):
        if data in self.data.values:
            return "Record has already exists in the Address Book."
        self.data[data.name] = data
        return "Record was added."


    def find(self, name):
        if self.__has_in_keys(self, name):
            return self.data[name]
        return self.__name_not_exists


    def delete(self, name):
        if self.__has_in_keys(self, name):
            self.data.pop(name)
            return "Record was removed."
        return self.__name_not_exists


    def __has_in_keys(self, value):
        return value in self.data.keys
